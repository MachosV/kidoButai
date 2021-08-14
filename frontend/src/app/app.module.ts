import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CampaignCreateComponent } from './campaign-create/campaign-create.component';
import { FormsModule } from '@angular/forms';
import { QrCodeModule } from 'ng-qrcode';
import { QrComponent } from './qr/qr.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { APIInterceptor } from './injectables/apiBaseUrl';
import { CampaignListComponent } from './campaign-list/campaign-list.component';
import { CampaignDetailComponent } from './campaign-detail/campaign-detail.component';
import { CommonModule } from '@angular/common';
import {CardModule} from 'primeng/card';
import { CampaignUpdateComponent } from './campaign-update/campaign-update.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { AuthInterceptor } from './injectables/authenticator';
import { NavbarComponent } from './navbar/navbar.component';
import { TableModule } from 'primeng/table';
import {ProgressBarModule} from 'primeng/progressbar';
import {DataViewModule} from 'primeng/dataview';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MessagesComponent } from './messages/messages.component';


@NgModule({
  declarations: [
    LoginFormComponent,
    AppComponent,
    CampaignCreateComponent,
    QrComponent,
    CampaignListComponent,
    CampaignDetailComponent,
    CampaignUpdateComponent,
    LoginFormComponent,
    NavbarComponent,
    MessagesComponent,
  ],
  imports: [
    BrowserAnimationsModule,
    DataViewModule,
    ProgressBarModule,
    TableModule,
    CardModule,
    HttpClientModule,
    QrCodeModule,
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    CommonModule
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: APIInterceptor,
    multi: true,
  },
  {
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true,
  }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { 

}
