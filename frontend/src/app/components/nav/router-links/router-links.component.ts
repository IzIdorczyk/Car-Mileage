import {Component} from '@angular/core';
import {NgForOf} from "@angular/common";
import {RouterLink} from "@angular/router";

@Component({
  selector: 'app-router-links',
  standalone: true,
  imports: [
    NgForOf,
    RouterLink
  ],
  templateUrl: './router-links.component.html',
  styleUrl: './router-links.component.scss'
})
export class RouterLinksComponent {

  links = [
    {name: 'Home', link: ''},
    {name: 'Auta', link: '/car'},
    {name: 'Przebieg', link: '/mileages'},

  ];

  selectedIndex = 0;

  setActiveClass(index: number) {
    this.selectedIndex = index;
  }
}

