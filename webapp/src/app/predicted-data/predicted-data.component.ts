import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';
import * as Papa from 'papaparse';

@Component({
  selector: 'app-predicted-data',
  templateUrl: './predicted-data.component.html',
  styleUrls: ['./predicted-data.component.scss']
})
export class PredictedDataComponent implements OnInit {
  constructor(private http: HttpClient,
    private router: Router){}
    headers?: string[] = [];
    rows: any[] = [];
  
    // constructor() { }
  
    ngOnInit(): void {
  
  
      
      this.http.get('assets\\Predicted_result.csv', { responseType: 'text' })
        .subscribe((response: string) => {
          const csv = response;
          const results = Papa.parse(csv, { header: true });
          this.headers = results.meta.fields;
          this.rows = results.data;
        }
        );
  
      
    }

}
