import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderOutComponent } from './components/header-out/header-out.component';
import { FooterOutComponent } from './components/footer-out/footer-out.component';
import { SignupUserComponent } from './componets/signup-user/signup-user.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderOutComponent,
    FooterOutComponent,
    SignupUserComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
