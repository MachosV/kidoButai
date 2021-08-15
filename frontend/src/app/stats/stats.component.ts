import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.css']
})
export class StatsComponent implements OnInit {

  data: any;

  //@ViewChild('chart') chart: any;


  constructor() { }

  ngOnInit(): void {
    /*setTimeout(() => {
      this.chart.refresh();
    }, 100);*/
    this.data = {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      datasets: [
          {
              label: 'Views',
              data: [65, 59, 80, 81, 56, 55, 40],
              borderColor: '#42A5F5',
              //fill:false,
              backgroundColor: 'rgba(2, 117, 216, 0.31)'
          }
      ]
      }
  }

}
