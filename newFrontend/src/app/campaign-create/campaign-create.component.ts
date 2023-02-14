import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { QroptionsService } from '../qr/qroptions.service';
import { CampaignService } from './campaign.service';
import { Campaign } from './campaignInterface';

@Component({
  selector: 'app-campaign',
  templateUrl: './campaign.component.html',
  styleUrls: ['./campaign.component.css']
})

export class CampaignCreateComponent implements OnInit {

  campaign =  <Campaign>{};
  tempLink = "";
  campaignLinks: string[] = [];
  showCampaignLinksFlag = false;
  loadQRComponent = false;
  color2: any = {
    r: 100, g: 130, b: 150
  };

  constructor(
    private campaignService: CampaignService,
    private qrOptionService: QroptionsService
    ) { }

  ngOnInit(): void {
  }

  previewCampaign(): void{
    this.campaignService.setRepresentationLink(this.campaign.representationLink)
    this.loadQRComponent = true;
  }

  createCampaign(): void{
    this.campaign.links = this.campaignLinks
    this.campaignService.postCampaign(this.campaign)
  }

  addLink(): void{
    this.campaignLinks.push(this.tempLink)
    this.tempLink = "";
  }

  clearAll(): void{
    this.loadQRComponent = false;
    this.campaign.name = ""
    this.campaign.description = ""
    this.campaign.representationLink = ""
    this.campaign.links = []
    this.campaignLinks = []
  }

  showCampaignLinks(): void{
    this.showCampaignLinksFlag = true;
  }

  trackByIdx(index: number, obj: any): any {
    return index;
  }

  deleteCampaignLink(index: number):void{
    this.campaignLinks.splice(index,1)
  }
}
