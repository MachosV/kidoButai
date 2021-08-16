import { Component, OnInit } from '@angular/core';
import { Message } from './messageInterface';
import { MessagingService } from './messaging.service';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css'],
})
export class MessagesComponent implements OnInit {

  message: Message = {"message":"", "type":""}

  constructor(
    private messageService: MessagingService,
  ) { }

  ngOnInit(): void {
    this.messageService.getMessage().subscribe(
      message=>{
        this.message = message
        setTimeout(() => this.message.message="", 3000);
      },
      error => console.log("An error occured",error)
      )
  }

}
