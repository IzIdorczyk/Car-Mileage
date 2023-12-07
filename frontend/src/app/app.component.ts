import {Component, OnInit} from '@angular/core';
import {initFlowbite} from "flowbite";
import {Router} from "@angular/router";

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
  }

  ngOnInit(): void {
    initFlowbite();
  }
}
