import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";
import 'flowbite';
import {NavComponent} from "./components/nav/nav.component";
import {CarAddButtonComponent} from "./components/cars/car-add-button/car-add-button.component";
import {NavDarkmodeComponent} from "./components/nav/nav-darkmode/nav-darkmode.component";
import {RouterModule} from "@angular/router";
import {NgxPaginationModule} from 'ngx-pagination';

@NgModule({
    declarations: [
        AppComponent,
    ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    CarAddButtonComponent,
    NavDarkmodeComponent,
    RouterModule,
    NavComponent,
    NgxPaginationModule,
  ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}


