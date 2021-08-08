import { Component } from '@angular/core';
import { GatekeeperService } from './auth/gatekeeper.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  isLoggedIn = false;
  gatekeeperService: GatekeeperService | any
  constructor(gatekeeperService: GatekeeperService){
    this.gatekeeperService = gatekeeperService
  }
  
  ngOnInit(){
    this.isLoggedIn = this.gatekeeperService.isLoggedIn()
  }
}
