import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CampaignDetailComponent } from './campaign-detail/campaign-detail.component';
import { CampaignListComponent } from './campaign-list/campaign-list.component';
import { CampaignCreateComponent } from './campaign-create/campaign-create.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { AuthGuard } from './auth/auth.guard';

const routes: Routes = [
  { path: 'campaigns/create',canActivate: [AuthGuard], component: CampaignCreateComponent },
  { path: 'campaigns/:id',canActivate: [AuthGuard], component: CampaignDetailComponent},
  { path: 'campaigns',canActivate: [AuthGuard], component: CampaignListComponent },
  { path: 'login', component: LoginFormComponent },
  { path: '**', redirectTo: 'login', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
