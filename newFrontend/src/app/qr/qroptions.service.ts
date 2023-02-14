import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QroptionsService {


  options: any = {
    width: 232,
    height: 232,
    margin: 14,
    //data: "http://192.168.1.123:8000/",
    data:"",
    image:
      "",
    dotsOptions: {
      color: "#4267b2",
      type: "rounded"
    },
    backgroundOptions: {
      color: "#ffffff"
    },
    imageOptions: {
      hideBackgroundDots: true,
      crossOrigin: "*",
      imageSize: 0.4,
      margin: 3,
    }
  }
  qrName:string = ""
  qrDescription: string = ""



  qrObject: any
  qrChanged = new EventEmitter<any>();

  optionsChanged = new EventEmitter<any>();

  constructor(private http: HttpClient) { }

  setQrObject(qrObject: any){
    this.qrObject = qrObject

    if(qrObject.size){
      this.qrObject.options.height = qrObject.size
      this.qrObject.options.width = qrObject.size
    }

    this.qrChanged.emit(this.qrObject.options)
  }

  getOptions():any{
    return this.qrObject.options
  }

  saveQR(): Observable<any> {
    var data = {
      name:this.qrObject.qrName,
      description:this.qrObject.qrDescription,
      representationLink:this.qrObject.options.data.split("/")[3],
      links:this.qrObject.links,
      //image:this.qrObject. TBD
      gtag:this.qrObject.qrAnalytics,
      options: btoa(JSON.stringify(this.qrObject.options))
    }
    return this.http.post<any>("api/campaign/create", data)
  }

}
