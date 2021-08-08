import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GatekeeperService {


  private loginURL: string = "api/auth"
  private date: number = 0


  constructor(
    private http: HttpClient,
    private router: Router
  ) { }


  login(username:string,password: string){
    //var data = {username:username, password:password};

    var params = new HttpParams()
      .set('username', username)
      .set('password',password);

    this.http.post<any>(this.loginURL,params)
    .subscribe(
      data => {
        if (data.response){
          console.log("Gatekeeper Service# login success")
          localStorage.setItem("authToken",data.response)
          localStorage.setItem("isLoggedIn_","true")
          localStorage.setItem("expires",data.expires)
          this.router.navigateByUrl('/campaigns')
        }
      },
      error => console.log("An error occured",error))
  }

  logout(): void{
    localStorage.setItem("authToken","")
    localStorage.setItem("isLoggedIn_","false")
    localStorage.setItem("expires","")
    this.router.navigateByUrl('/login')
  }

  isLoggedIn(): boolean{
    this.date = Date.now()
    
    var tempString = localStorage.getItem('expires')
    if (tempString){
      var parsedDate = Date.parse(tempString)
      if (this.date > parsedDate){
        localStorage.setItem("isLoggedIn_","false")
        localStorage.setItem("authToken","")
        localStorage.setItem("expires","")
        return false
      }
    }

    if(localStorage.getItem("isLoggedIn_")=='true'){
      return true
    }
    return false
  }

  getAuthToken():string | null{
    return localStorage.getItem('authToken')
  }

}
