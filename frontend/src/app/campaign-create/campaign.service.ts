import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Campaign } from './campaignInterface';
import { catchError } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CampaignService {

  private campaignURL = "api/campaign"
  private createCampaignURL = this.campaignURL+"/create"
  private representationLink = "";

  tempLinks: string = ""

  constructor(private http: HttpClient) { }

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


  getCampaignList() :Observable<Campaign[]>{
    return this.http.get<Campaign[]>(this.campaignURL)
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
