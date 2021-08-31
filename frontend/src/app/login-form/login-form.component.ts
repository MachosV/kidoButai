import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { GatekeeperService } from '../auth/gatekeeper.service';
import { MessagingService } from '../messages/messaging.service';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.css']
})
export class LoginFormComponent implements OnInit {

  username: string = ""
  password: string = ""

  constructor(
    private gatekeeperService: GatekeeperService,
    private router: Router,
    ) { }

  ngOnInit(): void {
    // if(this.gatekeeperService.isLoggedIn()){
    //   this.router.navigateByUrl("/campaigns")
    // }
  }

  login(): void{
    this.gatekeeperService.login(this.username, this.password)
  }
}
