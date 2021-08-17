import { formatDate } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { setupTestingRouter } from '@angular/router/testing';
import { StatService } from './stats-service.service';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.css']
})
export class StatsComponent implements OnInit {

  @Input() id!: string;

  data: any;
  basicOptions: any;
  stats: any;
  dateValue: any;
  top: any;

  constructor(private statService: StatService) { }


  setupChart():void{
    this.data = {
      labels: this.stats.map((stat: { create_date: any; }) => stat.create_date),
      datasets: [
          {
              label: 'Views',
              data: this.stats.map((stat: { count: any; }) => stat.count),
              borderColor: '#42A5F5',
              //fill:false,
              backgroundColor: 'rgba(2, 117, 216, 0.31)',
              tension:0.4,
          }
      ],
    }

    var tempMax = Math.max.apply(null, this.data.datasets[0].data)
    tempMax = Math.floor(tempMax + (tempMax * 0.10))
    var tempMin = Math.min.apply(null, this.data.datasets[0].data)
    tempMin = Math.floor(tempMin - (tempMin * 0.10))

    this.basicOptions = {
        scales: {
          yAxes: [{
            ticks: {
              min: tempMin,
              max: tempMax,
              precision: 0
            }
          }]
        }
    };
  }

  loadStats(): void{
    this.statService.getStats(this.id,this.dateValue).subscribe(data =>{
      this.stats=data;
      this.setupChart()
    })
  }

  ngOnInit(): void {
    //this.dateValue = formatDate(new Date(), 'dd/MM/yyyy', 'en');
    //this.stats = this.statService.getStats(this.id)
    //this.loadStats()

  }

  dateChanged():void{
    this.top  = window.pageYOffset || document.documentElement.scrollTop
    this.dateValue = formatDate(this.dateValue,'dd/MM/yyyy',"en-UK")
    this.loadStats()
  }
}
