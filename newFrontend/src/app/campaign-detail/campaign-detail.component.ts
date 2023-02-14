import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import QRCodeStyling from 'qr-code-styling';
import { CampaignService } from '../campaign-create/campaign.service';
import { Campaign } from '../campaign-create/campaignInterface';

@Component({
  selector: 'app-campaign-detail',
  templateUrl: './campaign-detail.component.html',
  styleUrls: ['./campaign-detail.component.css']
})
export class CampaignDetailComponent implements OnInit {

  campaign: Campaign | any;
  campaignLinks: string[] = [];
  editName: string = "";
  editDescription: string = "";
  edit = false;
  tempLink = "";
  newLinkFormFlag: boolean = false;
  qrObject: any = {
    filetype:"jpeg"
  }
  filetype: string = "jpeg"

  constructor(
    private campaignService: CampaignService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.campaignService.getCampaign(String(this.route.snapshot.paramMap.get('id')))
    .subscribe(campaign => {
      this.campaign = campaign;
      this.campaignService.setRepresentationLink(this.campaign.representationLink)
      this.campaign.links.map((item: { link: string; }) => {this.campaignLinks.push(item.link)})
    });
  }

  editCampaign(){
    this.edit = true;
  }

  deleteCampaign(){
    this.campaignService.deleteCampaign(this.campaign)
    //this.router.navigateByUrl("/campaigns/")
  }

  saveCampaign(){
    this.edit = false;
    this.campaignService.updateCampaign(this.campaign,this.campaignLinks)
    this.router.navigateByUrl("/campaigns/"+this.campaign.id)
  }

  downloadQR(){
    //console.log(JSON.parse(atob(this.campaign.options)))
    var qrCode = new QRCodeStyling(JSON.parse(atob(this.campaign.options))) 
    qrCode.download({ name: this.campaign.name.length > 0?this.campaign.name:"qr", extension: this.qrObject.filetype });
  }

  closeEdit(){
    this.edit=false
  }

  trackByIdx(index: number, obj: any): any {
    return index;
  }

  showNewLinkForm():void{
    this.newLinkFormFlag = true
  }

  addNewLink():void{
    this.campaignLinks.push(this.tempLink)
    this.tempLink = ""
    //this.newLinkFormFlag = false
  }

  deleteCampaignLink(index: number):void{
    this.campaignLinks.splice(index,1)
  }

}
