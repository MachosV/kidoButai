import { Component, OnInit } from '@angular/core';
import { CampaignService } from '../campaign-create/campaign.service';

@Component({
  selector: 'app-qr',
  templateUrl: './qr.component.html',
  styleUrls: ['./qr.component.css']
})
export class QrComponent implements OnInit {

  representationLink: string="";

  constructor(
    private campaignService: CampaignService
  ) { 
  }

  ngOnInit(): void {
    this.representationLink = this.campaignService.getRepresentationLink()
  }

  DownloadQRCode(): void{
    let canvas = document.getElementsByTagName("canvas");
    let data = canvas[0].toDataURL();

    let fileName = "MOCK"
    let link = document.createElement('a');
    link.download = fileName + '.png';
    canvas[0].toBlob(function(blob) {
      link.href = URL.createObjectURL(blob);
      link.click();
  });
  }

}
