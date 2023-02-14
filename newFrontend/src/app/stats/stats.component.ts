import { formatDate } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { StatDaily } from './statInterface';
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
  intervals: any;
  selectedInterval: any;
  labels: any;
  processedData: any;

  constructor(private statService: StatService) { }


  setupChart():void{

    this.data = {
      labels: this.labels,
      datasets: [
          {
              type:"bar",
              label: 'Views',
              data: this.processedData.map((stat: { count: any; }) => stat.count),
              //borderColor: '#42A5F5',
              borderColor: 'rgba(2, 117, 216, 1',
              fill:false,
              backgroundColor: 'rgba(2, 117, 216, 1',
              tension:0.2,
              borderWidth:3
          },
          /*{
            type:"bar",
            label: 'Views',
            data: this.processedData.map((stat: { count: any; }) => stat.count),
            borderColor: '#42A5F5',
            //fill:false,
            backgroundColor: 'rgba(2, 117, 216, 0.31)',
            tension:0.2,
        }*/
      ],
    }

    var tempMax = Math.max.apply(null, this.data.datasets[0].data)
    tempMax = Math.ceil(tempMax + (tempMax * 0.10))
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


  loadDailyStats():void{
    var hours = this.stats.map((stat: { hour: any; }) => stat.hour)
    for (let i = 0; i < 24; i++) {
      var hour = i+":00 - "+(i+1)+":00"
      if (hours.includes(i)){
        this.processedData.push({"hour":hour,"count":this.stats[this.stats.map((e: StatDaily) => e.hour).indexOf(i)].count})
        continue
      }
      this.processedData.push({"hour":hour,"count":0})
    }
    
    /*this.stats.sort(function(a: StatDaily, b: StatDaily) {
      return a.hour - b.hour;
    });*/
    this.labels = this.processedData.map((stat: { hour: any; }) => stat.hour)

  }

  loadWeeklyStats():void{
    //let startDate = new Date(parseInt(this.dateValue.split("/")[1],10),parseInt(this.dateValue.split("/")[0],10),parseInt(this.dateValue.split("/")[2],10))
    //console.log(this.dateValue.split("/")[2],this.dateValue.split("/")[1],this.dateValue.split("/")[0])
    //console.log(startDate)
    let processedDate = new Date(this.dateValue.split("/")[2]+" "+this.dateValue.split("/")[1]+" "+this.dateValue.split("/")[0])
    
    //for(let i = 0; i<7; i++){
      //console.log(processedDate+i)
    //}
    this.labels = this.stats.map((stat: { create_date: any; }) => stat.create_date)
  }

  loadStats(): void{
    this.processedData = [];
    switch(this.selectedInterval.code){
      case "we":
        this.statService.getStatsWeekly(this.id,this.dateValue).subscribe(data =>{
          this.stats = data;
          this.loadWeeklyStats()
          this.setupChart()
        })
        break;
      case "dy":
        this.statService.getStatsDaily(this.id,this.dateValue).subscribe(data =>{
          this.stats=data;
          this.loadDailyStats()
          this.setupChart()
        })
        break;
      /*case "mt":
        this.statService.getStatsMonthly(this.id,this.dateValue).subscribe(data =>{
          this.stats=data;
          this.setupChart()
        })*/
    }
  }

  ngOnInit(): void {
    this.intervals = [
      {name: 'Daily ', code: 'dy'},
      {name: 'Weekly ', code: 'we'},
      //{name: 'Monthly ', code: 'mt'},
    ]
    this.selectedInterval = this.intervals[0]
    var tempDate = new Date()
    this.dateValue = formatDate(tempDate, 'dd/MM/yyyy', 'en');
    this.loadStats()

  }

  dateChanged():void{
    //this.top  = window.pageYOffset || document.documentElement.scrollTop
    this.dateValue = formatDate(this.dateValue,'dd/MM/yyyy',"en-UK")
    this.loadStats()
  }

  intervalChanged():void{
    this.loadStats()
  }
}
