import {Injectable} from '@angular/core';
import {HttpEvent, HttpInterceptor, HttpHandler, HttpRequest} from '@angular/common/http';
import { Observable } from 'rxjs/internal/Observable';

@Injectable()
export class APIInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    if(!req.url.startsWith("data")){
      return next.handle(req.clone({ url: `http://localhost:8000/${req.url}` }))
    }
    return next.handle(req);
  }
}