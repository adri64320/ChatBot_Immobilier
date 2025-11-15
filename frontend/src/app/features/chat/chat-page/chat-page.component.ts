import { Component, OnInit, OnDestroy, ChangeDetectorRef } from '@angular/core';
import { NgFor, NgIf, NgClass } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Subscription } from 'rxjs';

import { ChatWsService, ChatMessage } from '../../../core/services/chat-ws.service';

@Component({
  selector: 'app-chat-page',
  standalone: true,
  imports: [NgFor, NgIf, NgClass, FormsModule],
  templateUrl: './chat-page.component.html',
  styleUrls: ['./chat-page.component.scss']
})
export class ChatPageComponent implements OnInit, OnDestroy {
  messages: ChatMessage[] = [];
  input = '';
  loading = false;

  private sub?: Subscription;

  constructor(
    private chatWs: ChatWsService,
    private cdr: ChangeDetectorRef,   // 👈 on injecte le ChangeDetector
  ) {}

  ngOnInit(): void {
    this.chatWs.connect();

    this.sub = this.chatWs.messages$.subscribe((msg) => {
      this.messages.push(msg);

      if (msg.role === 'assistant') {
        this.loading = false;
      }

      // 👇 on force Angular à rafraîchir ce composant
      this.cdr.detectChanges();
    });
  }

  send(): void {
    const text = this.input.trim();
    if (!text) return;

    this.loading = true;
    this.chatWs.sendUserMessage(text);
    this.input = '';
    this.cdr.detectChanges();  // optionnel mais safe
  }

  ngOnDestroy(): void {
    this.sub?.unsubscribe();
  }
}