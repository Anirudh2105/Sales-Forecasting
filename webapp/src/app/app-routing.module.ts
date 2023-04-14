import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { ReportComponent } from './report/report.component';
import { AboutComponent } from './about/about.component';
import { TrendsComponent } from './trends/trends.component';
import { GuidelinesComponent } from './guidelines/guidelines.component';
import { PredictedDataComponent } from './predicted-data/predicted-data.component';
import { PowerbiComponent } from './powerbi/powerbi.component';

const routes: Routes = [
  {path:'', component: LoginComponent},
  {path:'home', component: HomeComponent},
  {path:'report',component: ReportComponent},
  {path: 'about', component: AboutComponent},
  {path:'trends', component:TrendsComponent},
  {path:'guidelines',component:GuidelinesComponent},
  {path:'predicted-data', component:PredictedDataComponent},
  {path:'powerbi-dashboard',component:PowerbiComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
