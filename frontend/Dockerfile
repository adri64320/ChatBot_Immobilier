# Image Node légère
FROM node:20-alpine

# Dossier de travail
WORKDIR /app

# Copier les fichiers de config NPM
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste du code Angular
COPY . .

# Exposer le port utilisé par ng serve
EXPOSE 4200

# Lancer l'appli Angular accessible depuis l'extérieur du conteneur
CMD ["npm", "run", "start", "--", "--host", "0.0.0.0", "--port", "4200"]