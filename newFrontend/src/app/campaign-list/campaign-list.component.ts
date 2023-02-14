import { Component, OnInit } from '@angular/core';
import { Table } from 'primeng/table';
import QRCodeStyling from 'qr-code-styling';
import { Subject } from 'rxjs';
import { debounceTime } from 'rxjs/internal/operators/debounceTime';
import { distinctUntilChanged } from 'rxjs/operators';
import { CampaignService } from '../campaign-create/campaign.service';
import { Campaign } from '../campaign-create/campaignInterface';

@Component({
  selector: 'app-campaign-list',
  templateUrl: './campaign-list.component.html',
  styleUrls: ['./campaign-list.component.css']
})
export class CampaignListComponent implements OnInit {

  campaignList: Campaign[] = [];
  processedCampaignList: Campaign[] = [];
  nextPage: string ="";
  previousPage: string = "";


  searchString: string = "";
  searchStringObservable: Subject<string> = new Subject<string>();
  pageToLoad: string = "";

  constructor(
    private campaignService: CampaignService
  ) { }

  filterDataview():void {
    this.processedCampaignList = this.campaignList.filter(item => 
      item.name.toLowerCase().includes(this.searchString.toLowerCase()) || item.description.toLowerCase().includes(this.searchString.toLowerCase())
      )
  }

  ngOnInit(): void {
    this.campaignService.getCampaignList("",this.searchString)
    .subscribe(data => {
      this.campaignList = data.results;
      this.nextPage = data.next;
      this.previousPage = data.previous
      this.processedCampaignList = Object.assign([],this.campaignList)
    },
    error => console.log(error) )
    this.searchStringObservable.pipe(
      debounceTime(300), 
      distinctUntilChanged())
      .subscribe(value => {this.searchString = value;this.filterDataview()});
    }

  search(text: string):void {
    this.searchStringObservable.next(text); 
  }
  
  setPageToLoad(page: string):void{
    this.pageToLoad = page
    this.loadCampaignPage()
  }

  loadCampaignPage():void{
    this.campaignService.getCampaignList(this.pageToLoad,this.searchString)
    .subscribe(campaignPage => {
      this.campaignList = campaignPage.results;
      this.processedCampaignList = Object.assign([],this.campaignList)
      this.nextPage = campaignPage.next;
      this.previousPage = campaignPage.previous;
    });
  }

}
