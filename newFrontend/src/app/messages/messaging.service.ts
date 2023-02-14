import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MessagingService {

  private subject = new Subject<{}>();

  addMessage(message: string, type: any) {
    //console.log("Messaging service got message")
    this.subject.next({ "message": message, "type": type });
  }

  getMessage(): Observable<any> {
    return this.subject.asObservable();
  }

  constructor() { }
}
