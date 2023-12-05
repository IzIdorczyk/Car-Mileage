import {Component} from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent {
  links = [
    {name: 'Auta', link: '/auta'},
    {name: 'Przebieg', link: '/przebieg'},
    {name: 'Placeholder', link: '/auta'}
  ];

  selectedIndex = 0;

  setActiveClass(index: number){
    this.selectedIndex = index;
  }

}
