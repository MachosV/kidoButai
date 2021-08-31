import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { MessagingService } from '../messages/messaging.service';

@Injectable({
  providedIn: 'root'
})
export class GatekeeperService {


  private loginURL: string = "api/auth";
  private checkAuthURL: string = "api/checkAuth";
  private date: number = 0;


  constructor(
    private http: HttpClient,
    private router: Router,
    private messageService: MessagingService,
  ) { }


  login(username:string,password: string){
    //var data = {username:username, password:password};

    var params = new HttpParams()
      .set('username', username)
      .set('password',password);
    //console.log("posting login data")
    this.http.post<any>(this.loginURL,params)

    .subscribe(
      data => {
        if (data.response){
          //console.log("Gatekeeper Service# login success")
          localStorage.setItem("authToken",data.response)
          localStorage.setItem("isLoggedIn_","true")
          localStorage.setItem("expires",new Date(new Date().getTime() + 1*60000).toString())
          this.messageService.addMessage("Welcome back!","success")
          this.router.navigateByUrl('/campaigns')
        }else{
          this.messageService.addMessage("Invalid username or password","error")
        }
      },
      error => {
        //console.log("An error occured",error)
        this.messageService.addMessage("Invalid username or password","error")
      })
  }

  logout(): void{
    localStorage.setItem("authToken","")
    localStorage.setItem("isLoggedIn_","false")
    localStorage.setItem("expires","")
    this.router.navigateByUrl('/login')
  }

  async isLoggedIn(): Promise<boolean>{
    this.date = Date.now()
    let login = false;

    var tempString = localStorage.getItem('expires')
    var backendAuth;
    
    if(localStorage.getItem("isLoggedIn_")==="true"){
      login = true
    }

    if (tempString){
      var parsedDate = Date.parse(tempString)
      if (this.date > parsedDate){
        backendAuth = await this.checkBackendAuth().toPromise() //await here
        if (!(backendAuth.message==="Authed")){
          //login = true
          login = false
        }
        //login = false
      }
        if(!login){
          localStorage.setItem("isLoggedIn_","false")
          localStorage.setItem("authToken","")
          localStorage.setItem("expires","")
          this.router.navigateByUrl("login")
          return Promise.resolve(false)
        }
        localStorage.setItem("expires",new Date(new Date().getTime() + 15*60000).toString())
          return Promise.resolve(true)
    }else{
      console.log("no temp string")
    }
    

    if(localStorage.getItem("isLoggedIn_")=='true'){
      return true
    }
    this.router.navigateByUrl("login")
    return false
  }

  getAuthToken():string | null{
    return localStorage.getItem('authToken')
  }


  checkBackendAuth(){
    // var data = await this.http.get<any>(this.checkAuthURL).toPromise()
    return this.http.get<any>(this.checkAuthURL);

  //   .then(data =>{
  //     if (data.message==="Authed"){
  //       console.log("We are authed")
  //       return true
  //     }
  //     console.log("We are not authed")
  //     return false
  //   })
  // }

}
}
