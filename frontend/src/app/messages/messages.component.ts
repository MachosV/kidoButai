import { animate, state, style, transition, trigger } from '@angular/animations';
import { Component, OnInit } from '@angular/core';
import { Message } from './messageInterface';
import { MessagingService } from './messaging.service';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css'],
})
export class MessagesComponent implements OnInit {

  message: Message | any

  constructor(
    private messageService: MessagingService,
  ) { }

  ngOnInit(): void {
    this.message = this.messageService.getMessage().subscribe(
      message=>{
        this.message=message
      },
      error => console.log("An error occured",error)
      )
  }

}
