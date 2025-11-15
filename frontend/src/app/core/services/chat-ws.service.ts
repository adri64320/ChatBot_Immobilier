import { Injectable, NgZone } from '@angular/core';
import { Subject } from 'rxjs';

export type Role = 'user' | 'assistant';

export interface ChatMessage {
  role: Role;
  content: string;
}

@Injectable({
  providedIn: 'root'
})
export class ChatWsService {
  private socket?: WebSocket;
  private conversationId = 'conv-1';

  public messages$ = new Subject<ChatMessage>();

  constructor(private zone: NgZone) {}   // 👈 Très important

  connect(): void {
    if (typeof window === 'undefined') {
      // SSR : pas de WebSocket côté serveur
      return;
    }

    if (
      this.socket &&
      (this.socket.readyState === WebSocket.OPEN ||
        this.socket.readyState === WebSocket.CONNECTING)
    ) {
      return;
    }
 
    const url = `ws://localhost:8000/ws/chat/${this.conversationId}`;
    this.socket = new WebSocket(url);

    this.socket.onopen = () => {
      console.log('[WS] connecté');
    };

    this.socket.onmessage = (event) => {
      const received = event.data as string;
      console.log('[WS] message reçu du backend:', received);

      // 👉 Ici on force Angular à se réveiller et rerender
      this.zone.run(() => {
        this.messages$.next({
          role: 'assistant',
          content: received,
        });
      });
    };

    this.socket.onerror = (err) => {
      console.error('[WS] erreur', err);
    };

    this.socket.onclose = () => {
      console.log('[WS] connexion fermée');
    };
  }

  sendUserMessage(text: string): void {
    console.log('[WS] envoi message:', text);

    if (!this.socket || this.socket.readyState !== WebSocket.OPEN) {
      console.warn("[WS] socket non ouverte, impossible d'envoyer");
      return;
    }

    this.socket.send(text);

    this.zone.run(() => {
      this.messages$.next({
        role: 'user',
        content: text,
      });
    });
  }
}