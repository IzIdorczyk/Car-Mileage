import {Component, OnInit} from '@angular/core';
import {initFlowbite} from "flowbite";
import {Router} from "@angular/router";
import {environment} from "../environments/environment";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})



export class AppComponent implements OnInit{
  title = 'frontend';

  constructor(private readonly router: Router) {
    this.router.events.subscribe(() => {
      initFlowbite();
    });
    console.log(environment.apiUrl);
    console.log(`Is it prod: ${environment.production}`);
  }

  ngOnInit(): void {
    initFlowbite();
  }
}
