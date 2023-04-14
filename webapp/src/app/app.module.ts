import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from "./home/home.component";
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { ReportComponent } from './report/report.component';
import { RouterModule, Router } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { GuidelinesComponent } from './guidelines/guidelines.component';
import { TrendsComponent } from './trends/trends.component';
import { PredictedDataComponent } from './predicted-data/predicted-data.component';
import { PowerbiComponent } from './powerbi/powerbi.component';



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    ReportComponent,
    AboutComponent,
    GuidelinesComponent,
    TrendsComponent,
    PredictedDataComponent,
    PowerbiComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot([
      { path: 'home', component: HomeComponent },
      { path: 'report', component: ReportComponent }
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
