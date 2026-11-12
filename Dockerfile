# Dockerfile para Servir el Simulador Estático de Preguntas
FROM nginx:alpine

# Copiamos todos los archivos del sitio estático al directorio de Nginx
COPY site/ /usr/share/nginx/html/

# Exponer el puerto estándar HTTP
EXPOSE 80

# Iniciar servidor Nginx
CMD ["nginx", "-g", "daemon off;"]

