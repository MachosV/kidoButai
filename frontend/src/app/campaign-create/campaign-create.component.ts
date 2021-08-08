import { Component, OnInit } from '@angular/core';
import { CampaignService } from './campaign.service';
import { Campaign } from './campaignInterface';

@Component({
  selector: 'app-campaign',
  templateUrl: './campaign.component.html',
  styleUrls: ['./campaign.component.css']
})
export class CampaignCreateComponent implements OnInit {

  campaign =  <Campaign>{};
  textArea = "";
  loadQRComponent = false;

  constructor(
    private campaignService: CampaignService
    ) { }

  ngOnInit(): void {
  }

  createCampaign(): void{
    this.campaign.links = this.textArea.split("\n")
    this.campaignService.postCampaign(this.campaign)
    this.campaignService.setRepresentationLink(this.campaign.representationLink)
    this.loadQRComponent = true;
  }

  mockButton(): void{
    console.log(this.campaign.name)
    console.log(this.campaign.description)
    console.log(this.campaign.representationLink)
    console.log(this.campaign.links)
    //console.log(this.textArea.split("\n"))
  }

  clearAll(): void{
    this.loadQRComponent = false;
    this.campaign.name = ""
    this.campaign.description = ""
    this.campaign.representationLink = ""
    this.campaign.links = []
    this.textArea = ""
  }
}
