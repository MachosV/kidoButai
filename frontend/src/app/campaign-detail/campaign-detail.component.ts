import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CampaignService } from '../campaign-create/campaign.service';
import { Campaign } from '../campaign-create/campaignInterface';

@Component({
  selector: 'app-campaign-detail',
  templateUrl: './campaign-detail.component.html',
  styleUrls: ['./campaign-detail.component.css']
})
export class CampaignDetailComponent implements OnInit {

  loadedCampaignObject: Campaign | any;
  textArea: string = ""

  edit = false;
  editName: string = "";
  editDescription: string = "";
  editLinks: string[] = [];

  constructor(
    private campaignService: CampaignService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.campaignService.getCampaign(String(this.route.snapshot.paramMap.get('id')))
    .subscribe(campaign => {
      this.loadedCampaignObject = campaign;
      this.campaignService.setRepresentationLink(this.loadedCampaignObject.representationLink)
    });
  }

  editCampaign(){
    this.edit = true;
    this.textArea = "";
    this.loadedCampaignObject.links.map((item: { link: string; }) => this.textArea+=item.link+"\n")
  }

  saveCampaign(){
    this.edit = false;
    this.campaignService.updateCampaign(this.loadedCampaignObject,this.textArea.split("/n"))
    this.router.navigateByUrl("/campaigns/"+this.loadedCampaignObject.id)
  }

  revertCampaign(){
    
  }
}
