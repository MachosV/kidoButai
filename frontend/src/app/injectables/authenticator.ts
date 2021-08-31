import {Injectable} from '@angular/core';
import {HttpEvent, HttpInterceptor, HttpHandler, HttpRequest} from '@angular/common/http';
import { Observable } from 'rxjs/internal/Observable';
import { GatekeeperService } from '../auth/gatekeeper.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(
    private gatekeeperService: GatekeeperService
  ){}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    //console.log("AuthInterceptor# Interceptor fired up")
    // if(this.gatekeeperService.isLoggedIn()){
    if(localStorage.getItem("isLoggedIn_")==="true"){

      //console.log("AuthInterceptor# We are logged in")
      const userToken = this.gatekeeperService.getAuthToken();
      const modifiedReq = req.clone({ 
        headers: req.headers.set('Authorization', `Token ${userToken}`),
      });
      return next.handle(modifiedReq);
    }else{
      //console.log("AuthInterceptor# Gatekeeper says we are not logged in")
      return next.handle(req)
    } 
  }
}