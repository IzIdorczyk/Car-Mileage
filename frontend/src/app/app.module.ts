import {NgModule} from '@angular/core';
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
import {DarkmodeToggleComponent} from "./menu/darkmode-toggle/darkmode-toggle.component";
import {RouterLinksComponent} from "./menu/router-links/router-links.component";

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
        DarkmodeToggleComponent,
        RouterLinksComponent,
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}


