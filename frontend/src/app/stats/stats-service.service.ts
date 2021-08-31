import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Stat,StatDaily } from './statInterface';

@Injectable({
  providedIn: 'root'
})




export class StatService {
  stats: Stat[] = [
    {
      "create_date": "2021-08-13",
      "count": 0
      },
    {
      "create_date": "2021-08-14",
      "count": 350
      },
    {
    "create_date": "2021-08-15",
    "count": 50
    },
    {
    "create_date": "2021-08-16",
    "count": 2
    },{
      "create_date": "2021-08-17",
      "count": 60
      }
]

  statURL = "api/stats"

  constructor(private http: HttpClient) {
    
   }

   getStatsWeekly(id: string, date: string):Observable<Stat[]>{
    return this.http.get<Stat[]>(this.statURL+"/"+id+"/weekly?startDate="+date)
   }

   getStatsDaily(id: string, date:string):Observable<StatDaily[]>{
     return this.http.get<StatDaily[]>(this.statURL+"/"+id+"/daily?startDate="+date)
   }

   getStatsMonthly(id: string, date:string): void{
     console.log("Not yet implemented")
   }
}
