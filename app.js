/**
 * SIMULADOR QUIZIZZ - BANCO DE 4,000 PREGUNTAS
 * DIRECTOR DE UNIDAD EDUCATIVA | ESTADO PLURINACIONAL DE BOLIVIA
 */

// ==========================================
// 1. ESTADO GLOBAL DE LA APLICACIÓN
// ==========================================
const AppState = {
  allQuestions: [],
  topics: [],
  topicsById: {},
  selectedTopicIds: new Set(),
  
  // Configuración de partida
  questionLimit: 50,
  quizMode: 'study', // 'study' (inmediato) o 'exam' (al final)
  shuffleQuestions: true,
  shuffleOptions: true,
  soundEnabled: true,
  stopwatchEnabled: true,
  
  // Estado de la partida en curso
  gameQuestions: [],
  currentIndex: 0,
  score: 0,
  streak: 0,
  maxStreak: 0,
  answersRecord: [], // { question, selectedKey, isCorrect, optionsOrder }
  
  // Cronómetro
  stopwatchSeconds: 0,
  stopwatchTimer: null,
  
  // Audio Web API
  audioCtx: null
};

// Formas de las 5 opciones estilo Quizizz
const OPTION_SHAPES = {
  a: '♦',
  b: '●',
  c: '▲',
  d: '■',
  e: '⬡'
};

// ==========================================
// 2. MOTOR DE SONIDO (WEB AUDIO API SINTETIZADO)
// ==========================================
function initAudio() {
  if (!AppState.audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) {
      AppState.audioCtx = new AudioContext();
    }
  }
}

function playTone(freq, type = 'sine', duration = 0.15, gainVal = 0.15) {
  if (!AppState.soundEnabled) return;
  try {
    initAudio();
    if (!AppState.audioCtx) return;
    if (AppState.audioCtx.state === 'suspended') {
      AppState.audioCtx.resume();
    }
    const osc = AppState.audioCtx.createOscillator();
    const gain = AppState.audioCtx.createGain();
    
    osc.type = type;
    osc.frequency.setValueAtTime(freq, AppState.audioCtx.currentTime);
    
    gain.gain.setValueAtTime(gainVal, AppState.audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, AppState.audioCtx.currentTime + duration);
    
    osc.connect(gain);
    gain.connect(AppState.audioCtx.destination);
    
    osc.start();
    osc.stop(AppState.audioCtx.currentTime + duration);
  } catch (e) {
    console.warn('Audio no disponible:', e);
  }
}

function playCorrectSound() {
  playTone(523.25, 'triangle', 0.1, 0.2); // C5
  setTimeout(() => playTone(659.25, 'triangle', 0.12, 0.22), 80); // E5
  setTimeout(() => playTone(783.99, 'triangle', 0.25, 0.25), 160); // G5
}

function playIncorrectSound() {
  playTone(280, 'sawtooth', 0.15, 0.18);
  setTimeout(() => playTone(220, 'sawtooth', 0.25, 0.18), 120);
}

function playStreakSound() {
  playTone(440, 'triangle', 0.08);
  setTimeout(() => playTone(554.37, 'triangle', 0.08), 70);
  setTimeout(() => playTone(659.25, 'triangle', 0.15), 140);
  setTimeout(() => playTone(880, 'triangle', 0.3), 210);
}

function playClickSound() {
  playTone(800, 'sine', 0.04, 0.08);
}

// ==========================================
// 3. MOTOR DE ANIMACIÓN DE CONFETI
// ==========================================
let confettiParticles = [];
let confettiAnimId = null;

function triggerConfetti(particleCount = 100) {
  const canvas = document.getElementById('confettiCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  
  const colors = ['#6c5ce7', '#fd79a8', '#00cec9', '#ffeaa7', '#00e676', '#e21b3c'];
  confettiParticles = [];
  
  for (let i = 0; i < particleCount; i++) {
    confettiParticles.push({
      x: canvas.width / 2 + (Math.random() - 0.5) * 400,
      y: canvas.height / 2 - 100,
      size: Math.random() * 8 + 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      vx: (Math.random() - 0.5) * 12,
      vy: Math.random() * -12 - 4,
      rotation: Math.random() * 360,
      vRot: (Math.random() - 0.5) * 10,
      gravity: 0.35,
      alpha: 1
    });
  }
  
  if (confettiAnimId) cancelAnimationFrame(confettiAnimId);
  
  function renderConfetti() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    let activeCount = 0;
    
    confettiParticles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.vy += p.gravity;
      p.rotation += p.vRot;
      p.alpha -= 0.008;
      
      if (p.alpha > 0 && p.y < canvas.height + 50) {
        activeCount++;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.globalAlpha = Math.max(0, p.alpha);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 1.4);
        ctx.restore();
      }
    });
    
    if (activeCount > 0) {
      confettiAnimId = requestAnimationFrame(renderConfetti);
    } else {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }
  
  renderConfetti();
}

// ==========================================
// 4. CARGA DE DATOS Y CONFIGURACIÓN INICIAL
// ==========================================
async function loadQuestionBank() {
  try {
    // 1. Verificar si ya fue inyectado por questions_data.js
    if (window.QUIZ_DATA && window.QUIZ_DATA.questions && window.QUIZ_DATA.questions.length > 0) {
      console.log('Banco cargado vía bundle local questions_data.js');
      setupDatabase(window.QUIZ_DATA);
      return;
    }
    
    // 2. Fallback a fetch questions.json
    console.log('Intentando cargar banco vía fetch questions.json...');
    const resp = await fetch('questions.json');
    if (!resp.ok) throw new Error('Error al solicitar questions.json');
    const data = await resp.json();
    setupDatabase(data);
  } catch (err) {
    console.error('Error cargando el banco de preguntas:', err);
    alert('No se pudo cargar el banco de preguntas. Asegúrate de ejecutar este sitio a través de un servidor local (o Docker) o tener questions_data.js presente.');
  }
}

function setupDatabase(data) {
  AppState.allQuestions = data.questions || [];
  AppState.topics = data.topics || [];
  AppState.topicsById = {};
  
  AppState.topics.forEach(t => {
    AppState.topicsById[t.id] = t;
    // Seleccionar por defecto los primeros 3 temas para arranque rápido
    AppState.selectedTopicIds.add(t.id);
  });
  
  renderTopicsGrid();
  updateSelectionCounters();
}

// ==========================================
// 5. RENDERIZADO DE TEMAS Y FILTROS
// ==========================================
function renderTopicsGrid(categoryFilter = 'all', searchQuery = '') {
  const container = document.getElementById('topicsGrid');
  if (!container) return;
  container.innerHTML = '';
  
  const query = searchQuery.trim().toLowerCase();
  
  AppState.topics.forEach(t => {
    // Filtro por categoría
    if (categoryFilter !== 'all' && t.category !== categoryFilter) return;
    
    // Filtro por búsqueda
    if (query) {
      const matchTitle = t.title.toLowerCase().includes(query);
      const matchCode = t.code.toLowerCase().includes(query);
      const matchCat = t.category.toLowerCase().includes(query);
      if (!matchTitle && !matchCode && !matchCat) return;
    }
    
    const isSelected = AppState.selectedTopicIds.has(t.id);
    
    const card = document.createElement('div');
    card.className = `topic-card ${isSelected ? 'selected' : ''}`;
    card.dataset.topicId = t.id;
    
    card.innerHTML = `
      <div class="topic-checkbox"></div>
      <div class="topic-content">
        <div class="topic-top-tags">
          <span class="topic-code">${t.code}</span>
          <span class="topic-category-tag">${t.category}</span>
        </div>
        <div class="topic-name">${t.short_title}</div>
        <div class="topic-footer">
          <span>${t.icon} Oficial</span>
          <span class="q-count-badge">200 preguntas</span>
        </div>
      </div>
    `;
    
    card.addEventListener('click', () => toggleTopicSelection(t.id, card));
    container.appendChild(card);
  });
}

function toggleTopicSelection(topicId, cardElement) {
  playClickSound();
  if (AppState.selectedTopicIds.has(topicId)) {
    AppState.selectedTopicIds.delete(topicId);
    cardElement.classList.remove('selected');
  } else {
    AppState.selectedTopicIds.add(topicId);
    cardElement.classList.add('selected');
  }
  updateSelectionCounters();
}

function updateSelectionCounters() {
  const count = AppState.selectedTopicIds.size;
  const totalAvailable = count * 200;
  
  const selCountEl = document.getElementById('selectedTopicsCount');
  const poolCountEl = document.getElementById('availableQuestionsPool');
  const startBtnSub = document.getElementById('startBtnSub');
  const slider = document.getElementById('customRangeSlider');
  
  if (selCountEl) selCountEl.textContent = count;
  if (poolCountEl) poolCountEl.textContent = totalAvailable.toLocaleString();
  
  // Actualizar slider máximo
  if (slider) {
    const maxVal = Math.max(10, Math.min(totalAvailable, 4000));
    slider.max = maxVal;
    if (parseInt(slider.value, 10) > maxVal) {
      slider.value = maxVal;
      updateRangeDisplay(maxVal);
    }
  }
  
  const limit = getEffectiveQuestionLimit();
  if (startBtnSub) {
    startBtnSub.textContent = count === 0 
      ? '(Selecciona al menos 1 tema)' 
      : `(${limit} preguntas de ${count} temas)`;
  }
}

function getEffectiveQuestionLimit() {
  const totalAvailable = AppState.selectedTopicIds.size * 200;
  if (AppState.questionLimit === 'all') {
    return totalAvailable;
  }
  return Math.min(parseInt(AppState.questionLimit, 10) || 50, totalAvailable);
}

function updateRangeDisplay(val) {
  const display = document.getElementById('rangeDisplayVal');
  if (!display) return;
  if (val === 'all') {
    display.textContent = 'Todas las seleccionadas';
  } else {
    display.textContent = `${val} preguntas`;
  }
}

// ==========================================
// 6. MOTOR DE JUEGO / PARTIDA
// ==========================================
function startQuiz(customQuestionsPool = null) {
  playClickSound();
  
  if (!customQuestionsPool) {
    if (AppState.selectedTopicIds.size === 0) {
      alert('Por favor selecciona al menos un tema de estudio.');
      return;
    }
    
    // Filtrar preguntas de los temas seleccionados
    const pool = AppState.allQuestions.filter(q => AppState.selectedTopicIds.has(q.topic_id));
    if (pool.length === 0) {
      alert('No hay preguntas disponibles para los temas seleccionados.');
      return;
    }
    
    // Aleatorizar orden si está activo
    let questionsToUse = [...pool];
    if (AppState.shuffleQuestions) {
      shuffleArray(questionsToUse);
    }
    
    // Limitar cantidad
    const limit = getEffectiveQuestionLimit();
    AppState.gameQuestions = questionsToUse.slice(0, limit);
  } else {
    // Si viene de "Repasar Incorrectas"
    AppState.gameQuestions = customQuestionsPool;
  }
  
  // Reiniciar métricas
  AppState.currentIndex = 0;
  AppState.score = 0;
  AppState.streak = 0;
  AppState.maxStreak = 0;
  AppState.answersRecord = [];
  
  // Cronómetro
  clearInterval(AppState.stopwatchTimer);
  AppState.stopwatchSeconds = 0;
  if (AppState.stopwatchEnabled) {
    document.getElementById('stopwatchHud').style.display = 'inline-flex';
    AppState.stopwatchTimer = setInterval(() => {
      AppState.stopwatchSeconds++;
      updateStopwatchDisplay();
    }, 1000);
  } else {
    document.getElementById('stopwatchHud').style.display = 'none';
  }
  
  // Cambiar a pantalla de juego
  switchScreen('quizScreen');
  renderCurrentQuestion();
}

function updateStopwatchDisplay() {
  const el = document.getElementById('stopwatchDisplay');
  if (!el) return;
  const mins = Math.floor(AppState.stopwatchSeconds / 60);
  const secs = AppState.stopwatchSeconds % 60;
  el.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}

function renderCurrentQuestion() {
  const q = AppState.gameQuestions[AppState.currentIndex];
  if (!q) {
    finishQuiz();
    return;
  }
  
  // Ocultar feedback si estaba abierto
  const fbPanel = document.getElementById('studyFeedbackPanel');
  if (fbPanel) fbPanel.classList.add('hidden');
  
  // Actualizar HUD
  document.getElementById('currentQuestionNum').textContent = AppState.currentIndex + 1;
  document.getElementById('totalQuestionsInGame').textContent = AppState.gameQuestions.length;
  
  const pct = Math.round(((AppState.currentIndex) / AppState.gameQuestions.length) * 100);
  document.getElementById('progressBarFill').style.width = `${pct}%`;
  document.getElementById('progressPercent').textContent = `${pct}%`;
  
  document.getElementById('liveScore').textContent = AppState.score;
  document.getElementById('streakCount').textContent = AppState.streak;
  
  const streakBadge = document.getElementById('streakBadge');
  if (AppState.streak >= 3) {
    streakBadge.classList.add('lit');
  } else {
    streakBadge.classList.remove('lit');
  }
  
  // Renderizar Título del Tema en la Pregunta (Requisito fundamental)
  const catTag = document.getElementById('qCategoryBadge');
  const titleTag = document.getElementById('qTopicTitle');
  if (catTag) catTag.textContent = q.category || 'Normativa';
  if (titleTag) titleTag.textContent = `${q.topic_code || ''} ${q.topic}`;
  
  // Texto de la Pregunta
  document.getElementById('questionText').textContent = q.question;
  
  // Opciones A, B, C, D, E
  const optsContainer = document.getElementById('optionsContainer');
  optsContainer.innerHTML = '';
  
  const rawOpts = Object.entries(q.options); // [['a','...'], ['b','...'], ...]
  let optionsToRender = rawOpts.map(([key, text]) => ({ originalKey: key, text }));
  
  if (AppState.shuffleOptions) {
    shuffleArray(optionsToRender);
  }
  
  // Guardar mapeo de esta pregunta
  q._renderedOptions = optionsToRender;
  
  optionsToRender.forEach((item, idx) => {
    const letter = ['a', 'b', 'c', 'd', 'e'][idx];
    const btn = document.createElement('button');
    btn.className = `quizizz-opt-btn opt-${letter}`;
    btn.dataset.originalKey = item.originalKey;
    
    btn.innerHTML = `
      <div class="opt-shape">${OPTION_SHAPES[letter] || letter.toUpperCase()}</div>
      <div class="opt-text">${item.text}</div>
    `;
    
    btn.addEventListener('click', () => handleOptionSelected(q, item.originalKey, btn));
    optsContainer.appendChild(btn);
  });
}

function handleOptionSelected(question, selectedKey, clickedBtn) {
  const isCorrect = (selectedKey === question.answer);
  
  // Deshabilitar todos los botones para evitar doble clic
  const allBtns = document.querySelectorAll('.quizizz-opt-btn');
  allBtns.forEach(b => b.disabled = true);
  
  // Registrar respuesta
  AppState.answersRecord.push({
    question,
    selectedKey,
    isCorrect
  });
  
  // Actualizar racha y puntaje
  if (isCorrect) {
    AppState.streak++;
    if (AppState.streak > AppState.maxStreak) {
      AppState.maxStreak = AppState.streak;
    }
    const bonus = Math.min(AppState.streak * 50, 300);
    AppState.score += 1000 + bonus;
    
    playCorrectSound();
    clickedBtn.classList.add('is-correct');
    
    if (AppState.streak >= 3) {
      playStreakSound();
      triggerConfetti(40);
    }
  } else {
    AppState.streak = 0;
    playIncorrectSound();
    clickedBtn.classList.add('is-incorrect');
    
    // Iluminar la respuesta correcta en verde
    allBtns.forEach(b => {
      if (b.dataset.originalKey === question.answer) {
        b.classList.add('is-correct');
      } else if (b !== clickedBtn) {
        b.classList.add('dimmed');
      }
    });
  }
  
  document.getElementById('liveScore').textContent = AppState.score;
  document.getElementById('streakCount').textContent = AppState.streak;
  
  // Manejo según el modo de juego
  if (AppState.quizMode === 'study') {
    // Mostrar panel de justificación legal y botón de avanzar
    showStudyFeedback(isCorrect, question);
  } else {
    // Modo examen continuo: breve pausa y pasar a la siguiente
    setTimeout(() => {
      advanceNextQuestion();
    }, 700);
  }
}

function showStudyFeedback(isCorrect, question) {
  const panel = document.getElementById('studyFeedbackPanel');
  const icon = document.getElementById('feedbackIcon');
  const title = document.getElementById('feedbackTitle');
  const subtitle = document.getElementById('feedbackSubtitle');
  const expText = document.getElementById('feedbackExplanationText');
  
  if (isCorrect) {
    icon.className = 'fb-icon correct';
    icon.textContent = '✓';
    title.textContent = '¡Correcto!';
    subtitle.textContent = `Respuesta acertada: Inciso ${question.answer.toUpperCase()}`;
  } else {
    icon.className = 'fb-icon incorrect';
    icon.textContent = '✕';
    title.textContent = 'Respuesta Incorrecta';
    subtitle.textContent = `La respuesta correcta era el inciso: ${question.answer.toUpperCase()}`;
  }
  
  expText.textContent = question.explanation || 'Conforme a la normativa boliviana vigente para el cargo de Director de Unidad Educativa.';
  panel.classList.remove('hidden');
}

function advanceNextQuestion() {
  AppState.currentIndex++;
  if (AppState.currentIndex < AppState.gameQuestions.length) {
    renderCurrentQuestion();
  } else {
    finishQuiz();
  }
}

// ==========================================
// 7. FINALIZACIÓN Y PANTALLA DE RESULTADOS
// ==========================================
function finishQuiz() {
  clearInterval(AppState.stopwatchTimer);
  switchScreen('resultScreen');
  
  const total = AppState.answersRecord.length;
  const correctCount = AppState.answersRecord.filter(r => r.isCorrect).length;
  const incorrectCount = total - correctCount;
  const percent = total > 0 ? Math.round((correctCount / total) * 100) : 0;
  
  // Asignar datos al sumario
  document.getElementById('finalPercent').textContent = `${percent}%`;
  document.getElementById('finalCorrectCount').textContent = correctCount;
  document.getElementById('finalIncorrectCount').textContent = incorrectCount;
  document.getElementById('finalMaxStreak').textContent = `${AppState.maxStreak} 🔥`;
  
  const mins = Math.floor(AppState.stopwatchSeconds / 60);
  const secs = AppState.stopwatchSeconds % 60;
  document.getElementById('finalTime').textContent = `${mins}m ${secs}s`;
  
  // Título y Trofeo según desempeño
  const emojiEl = document.getElementById('resultEmoji');
  const titleEl = document.getElementById('resultRankTitle');
  const subEl = document.getElementById('resultRankSubtitle');
  
  if (percent >= 85) {
    emojiEl.textContent = '🏆';
    titleEl.textContent = '¡Nivel: Maestro de la Normativa!';
    subEl.textContent = 'Has demostrado un dominio sobresaliente para el Examen de Director.';
    triggerConfetti(150);
  } else if (percent >= 60) {
    emojiEl.textContent = '⭐';
    titleEl.textContent = '¡Buen Desempeño!';
    subEl.textContent = 'Estás en un buen nivel, repasa las preguntas erradas para asegurar la máxima calificación.';
    triggerConfetti(60);
  } else {
    emojiEl.textContent = '📚';
    titleEl.textContent = '¡Sigue Practicando!';
    subEl.textContent = 'Te recomendamos repasar los temas de mayor debilidad con el Modo Estudio.';
  }
  
  // Botón de reintento de fallidas
  const retryBtn = document.getElementById('retryIncorrectBtn');
  const missedCountBtn = document.getElementById('missedCountBtn');
  if (missedCountBtn) missedCountBtn.textContent = incorrectCount;
  
  if (incorrectCount === 0) {
    retryBtn.style.display = 'none';
  } else {
    retryBtn.style.display = 'inline-flex';
  }
  
  // Renderizar Lista de Revisión Ítem por Ítem
  renderReviewList('all');
}

function renderReviewList(filter = 'all') {
  const container = document.getElementById('reviewQuestionsList');
  if (!container) return;
  container.innerHTML = '';
  
  const records = AppState.answersRecord;
  const correctCount = records.filter(r => r.isCorrect).length;
  const wrongCount = records.length - correctCount;
  
  document.getElementById('revAllCount').textContent = records.length;
  document.getElementById('revRightCount').textContent = correctCount;
  document.getElementById('revWrongCount').textContent = wrongCount;
  
  records.forEach((rec, idx) => {
    if (filter === 'correct' && !rec.isCorrect) return;
    if (filter === 'wrong' && rec.isCorrect) return;
    
    const q = rec.question;
    const card = document.createElement('div');
    card.className = `review-item ${rec.isCorrect ? 'is-correct' : 'is-incorrect'}`;
    
    const userAnsText = q.options[rec.selectedKey] || 'Sin respuesta';
    const correctAnsText = q.options[q.answer] || '';
    
    card.innerHTML = `
      <div class="rev-top-meta">
        <span class="rev-topic-badge">${q.topic_code || ''} ${q.short_title || q.topic}</span>
        <span class="rev-status-pill ${rec.isCorrect ? 'correct' : 'incorrect'}">
          ${rec.isCorrect ? '✓ Correcta' : '✕ Incorrecta'}
        </span>
      </div>
      <div class="rev-q-text">${idx + 1}. ${q.question}</div>
      <div class="rev-answers-box">
        ${!rec.isCorrect ? `
          <div class="rev-ans-row user-wrong">
            <span>Tu respuesta:</span>
            <strong>${rec.selectedKey.toUpperCase()}) ${userAnsText}</strong>
          </div>
        ` : ''}
        <div class="rev-ans-row correct-ans">
          <span>Respuesta oficial:</span>
          <strong>${q.answer.toUpperCase()}) ${correctAnsText}</strong>
        </div>
      </div>
      <div class="rev-explanation">
        <strong>📖 Justificación Legal / Técnica:</strong> ${q.explanation}
      </div>
    `;
    
    container.appendChild(card);
  });
}

// ==========================================
// 8. HELPERS Y NAVEGACIÓN
// ==========================================
function switchScreen(screenId) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(screenId);
  if (target) {
    target.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function shuffleArray(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ==========================================
// 9. EVENT LISTENERS E INICIALIZACIÓN
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  loadQuestionBank();
  
  // Búsqueda de temas
  const searchInput = document.getElementById('topicSearchInput');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const activeTab = document.querySelector('.cat-tab.active');
      const cat = activeTab ? activeTab.dataset.cat : 'all';
      renderTopicsGrid(cat, e.target.value);
    });
  }
  
  // Pestañas de categoría
  document.querySelectorAll('.cat-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      playClickSound();
      document.querySelectorAll('.cat-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const search = searchInput ? searchInput.value : '';
      renderTopicsGrid(tab.dataset.cat, search);
    });
  });
  
  // Seleccionar todos / deseleccionar todos
  document.getElementById('selectAllBtn').addEventListener('click', () => {
    playClickSound();
    AppState.topics.forEach(t => AppState.selectedTopicIds.add(t.id));
    document.querySelectorAll('.topic-card').forEach(c => c.classList.add('selected'));
    updateSelectionCounters();
  });
  
  document.getElementById('deselectAllBtn').addEventListener('click', () => {
    playClickSound();
    AppState.selectedTopicIds.clear();
    document.querySelectorAll('.topic-card').forEach(c => c.classList.remove('selected'));
    updateSelectionCounters();
  });
  
  // Presets de Rango de preguntas
  const slider = document.getElementById('customRangeSlider');
  document.querySelectorAll('.preset-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      playClickSound();
      document.querySelectorAll('.preset-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      const count = btn.dataset.count;
      AppState.questionLimit = count;
      if (count !== 'all') {
        if (slider) slider.value = count;
        updateRangeDisplay(count);
      } else {
        updateRangeDisplay('all');
      }
      updateSelectionCounters();
    });
  });
  
  if (slider) {
    slider.addEventListener('input', (e) => {
      document.querySelectorAll('.preset-btn').forEach(b => b.classList.remove('active'));
      AppState.questionLimit = parseInt(e.target.value, 10);
      updateRangeDisplay(AppState.questionLimit);
      updateSelectionCounters();
    });
  }
  
  // Modos de Juego
  document.querySelectorAll('input[name="quizMode"]').forEach(radio => {
    radio.addEventListener('change', (e) => {
      playClickSound();
      AppState.quizMode = e.target.value;
      document.querySelectorAll('.mode-card').forEach(c => c.classList.remove('selected'));
      e.target.closest('.mode-card').classList.add('selected');
    });
  });
  
  // Checkboxes de configuración
  document.getElementById('shuffleQuestionsCheck').addEventListener('change', e => {
    AppState.shuffleQuestions = e.target.checked;
  });
  document.getElementById('shuffleOptionsCheck').addEventListener('change', e => {
    AppState.shuffleOptions = e.target.checked;
  });
  document.getElementById('enableStopwatchCheck').addEventListener('change', e => {
    AppState.stopwatchEnabled = e.target.checked;
  });
  
  // Botón Iniciar Quiz
  document.getElementById('startQuizBtn').addEventListener('click', () => {
    startQuiz();
  });
  
  // Botón Siguiente Pregunta (Modo Estudio)
  document.getElementById('nextQuestionBtn').addEventListener('click', () => {
    playClickSound();
    advanceNextQuestion();
  });
  
  // Salir de partida en curso
  document.getElementById('exitQuizBtn').addEventListener('click', () => {
    if (confirm('¿Seguro que deseas salir del quiz actual? Se perderá el progreso de esta sesión.')) {
      clearInterval(AppState.stopwatchTimer);
      switchScreen('setupScreen');
    }
  });
  
  // Botón Repasar Incorrectas
  document.getElementById('retryIncorrectBtn').addEventListener('click', () => {
    const wrongQuestions = AppState.answersRecord.filter(r => !r.isCorrect).map(r => r.question);
    if (wrongQuestions.length > 0) {
      startQuiz(wrongQuestions);
    }
  });
  
  // Botón Reiniciar Mismo Quiz
  document.getElementById('playAgainBtn').addEventListener('click', () => {
    startQuiz([...AppState.gameQuestions]);
  });
  
  // Botón Volver a inicio / cambiar temas
  document.getElementById('backToHomeBtn').addEventListener('click', () => {
    switchScreen('setupScreen');
  });
  
  // Filtros de la lista de revisión
  document.querySelectorAll('.rev-filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      playClickSound();
      document.querySelectorAll('.rev-filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderReviewList(btn.dataset.filter);
    });
  });
  
  // Toggle de Sonido
  const soundBtn = document.getElementById('soundToggleBtn');
  const soundIcon = document.getElementById('soundIcon');
  if (soundBtn) {
    soundBtn.addEventListener('click', () => {
      AppState.soundEnabled = !AppState.soundEnabled;
      soundIcon.textContent = AppState.soundEnabled ? '🔊' : '🔇';
      soundBtn.style.opacity = AppState.soundEnabled ? '1' : '0.6';
    });
  }
  
  // Pantalla Completa
  const fullBtn = document.getElementById('fullscreenBtn');
  if (fullBtn) {
    fullBtn.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    });
  }
});

