import { Component } from '@angular/core';
import QRCodeStyling from 'qr-code-styling';
import { QroptionsService } from '../qroptions.service';

@Component({
  selector: 'app-qrshow',
  templateUrl: './qrshow.component.html',
  styleUrls: ['./qrshow.component.css']
})
export class QrshowComponent {

  constructor(
    private qrOptionService: QroptionsService,
    ){}

  qr: QRCodeStyling |null = null;
  showPreviewBanner: boolean = true

  ngOnInit(): void {
    this.qrOptionService.qrChanged.subscribe(_ =>{
      if(this.qrOptionService.qrObject.options.data.length < 1){
        this.showPreviewBanner = true
      }
      else{
        this.showPreviewBanner = false
      }
      this.qr = new QRCodeStyling(this.qrOptionService.qrObject.options)
      var canvas = <HTMLElement> document.getElementById("qrCodeCanvas")
      canvas.innerHTML=""
      this.qr.append(canvas)
      })
  }

}
