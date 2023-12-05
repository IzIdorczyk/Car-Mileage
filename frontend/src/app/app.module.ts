import {NgModule, OnInit} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {CarComponent} from './car/car.component';
import {HttpClientModule} from "@angular/common/http";
import {MenuComponent} from './menu/menu.component';
import {FormsModule} from "@angular/forms";
import 'flowbite';
import {AddCarButtonComponent} from "./car/add-car-button/add-car-button.component";
import {CarListComponent} from "./car/car-list/car-list.component";

@NgModule({
  declarations: [
    AppComponent,
    CarComponent,
    MenuComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    AddCarButtonComponent,
    CarListComponent,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule implements OnInit {

  ngOnInit(): void {

    // On page load or when changing themes, best to add inline in `head` to avoid FOUC
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark')
    }

  }
}


