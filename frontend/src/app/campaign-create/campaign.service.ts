import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Campaign, CampaignPage } from './campaignInterface';
import { catchError } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class CampaignService {

  private campaignURL = "api/campaign"
  private createCampaignURL = this.campaignURL+"/create"
  private representationLink = "";

  tempLinks: string = ""

  constructor(
    private http: HttpClient,
    private router: Router) { }

  postCampaign(campaign: Campaign){
    this.http.post<Campaign>(this.createCampaignURL,campaign)
    .subscribe(
      _=>_,
      error => console.log("An error occured",error))
  }

  updateCampaign(campaign: Campaign, links: string[]){
    var object = {
      "name":campaign.name,
      "description":campaign.description,
      "links": links
    }
    this.http.put<Campaign>(this.campaignURL+"/"+campaign.id+"/update",object)
    .subscribe(
      _=>_,
      error => console.log("An error occured",error))
  }

  deleteCampaign(campaign: Campaign): void{
    this.http.delete<Campaign>(this.campaignURL+"/"+campaign.id)
    .subscribe(
      _=>_,
      error => console.log("An error occured",error))
  }


  getCampaignList(page:string, search:string) :Observable<CampaignPage>{

    let params = new HttpParams();
    var tempCampaignURL = this.campaignURL
    if(page){
      tempCampaignURL = tempCampaignURL+page.split("/campaign")[1]
    }
    if(search){
      params = params.append('search', search);
    }
    return this.http.get<CampaignPage>(tempCampaignURL,{params:params})
  }

  getCampaign(id: string): Observable<Campaign> {
    return this.http.get<Campaign>(this.campaignURL+"/"+id)
  }

  setRepresentationLink(representationLink: string){
    this.representationLink = representationLink
  }
  
  getRepresentationLink(): string{
    return this.representationLink
  }

}
