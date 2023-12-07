import { Component } from '@angular/core';
import {CarAddButtonComponent} from "../../components/cars/car-add-button/car-add-button.component";
import {CarListComponent} from "../../components/cars/car-list/car-list.component";

@Component({
  selector: 'app-cars',
  standalone: true,
  imports: [
    CarAddButtonComponent,
    CarListComponent
  ],
  templateUrl: './cars.component.html',
  styleUrl: './cars.component.scss'
})
export class CarsComponent {

}
