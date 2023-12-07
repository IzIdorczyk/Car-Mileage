import { Component } from '@angular/core';
import {RouterLink} from "@angular/router";
import {NavDarkmodeComponent} from "./nav-darkmode/nav-darkmode.component";
import {RouterLinksComponent} from "./router-links/router-links.component";

@Component({
  selector: 'app-nav',
  standalone: true,
  imports: [
    RouterLink,
    NavDarkmodeComponent,
    RouterLinksComponent
  ],
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.scss'
})
export class NavComponent {

}
