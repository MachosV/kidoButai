import { Component, OnInit } from '@angular/core';
import { Table } from 'primeng/table';
import { CampaignService } from '../campaign-create/campaign.service';
import { Campaign } from '../campaign-create/campaignInterface';

@Component({
  selector: 'app-campaign-list',
  templateUrl: './campaign-list.component.html',
  styleUrls: ['./campaign-list.component.css']
})
export class CampaignListComponent implements OnInit {

  campaignList: Campaign[] = [];

  constructor(
    private campaignService: CampaignService
  ) { }

  ngOnInit(): void {
    this.campaignService.getCampaignList()
    .subscribe(data => this.campaignList=data)
  }

  clear(table: Table) {
    table.clear();
}

}
