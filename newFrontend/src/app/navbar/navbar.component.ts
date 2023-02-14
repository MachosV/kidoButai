import { Component, OnInit } from '@angular/core';
import { GatekeeperService } from '../auth/gatekeeper.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(private gatekeeperService: GatekeeperService) { }

  ngOnInit(): void {
  }

  logout(): void{
    this.gatekeeperService.logout()
  }

}
