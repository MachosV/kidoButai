import { Component, Input } from '@angular/core';
import QRCodeStyling from 'qr-code-styling';

@Component({
  selector: 'app-qr-preview',
  templateUrl: './qr-preview.component.html',
  styleUrls: ['./qr-preview.component.css']
})
export class QrPreviewComponent {

  @Input() item = ""; //
  @Input() id ="";

  constructor(
    ){}

  qr: QRCodeStyling |null = null;

  ngOnInit(): void {
    //this.item.width = 200
    //this.item.height = 200
    var options = JSON.parse(atob(this.item))
    options.height = 200
    options.width = 200
    this.qr = new QRCodeStyling(options)
    var canvas = <HTMLElement> document.getElementById("canvas"+this.id)
    canvas.innerHTML=""
    this.qr.append(canvas)
  }
}
