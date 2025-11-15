import { defineConfig } from 'vite';
import angular from '@analogjs/vite-plugin-angular';

// ⚠️ Mets ici ton vrai domaine Koyeb (copie-colle EXACT)
const allowedHost = "chatbot-immo-adrien64320-81c371cc.koyeb.app";

export default defineConfig({
  plugins: [angular()],

  server: {
    host: true, // nécessaire dans Docker
    port: 4200,

    allowedHosts: [
      'localhost',
      '127.0.0.1',
      allowedHost,   // 👈 Ici ton domaine de production Koyeb
    ],
  },

  preview: {
    host: true,
    port: 4200,
  }
});