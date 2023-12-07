import { Component } from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {CarsService} from "../../../services/cars.service";
import {Observable} from "rxjs";
import {Cars} from "../../../interfaces/cars";

@Component({
  selector: 'app-car-add-form',
  standalone: true,
    imports: [
        FormsModule,
        ReactiveFormsModule
    ],
  templateUrl: './car-add-form.component.html',
  styleUrl: './car-add-form.component.scss'
})
export class CarAddFormComponent {
  car: any = [];

  constructor(private carService: CarsService) {
  }

  createCar(car: Observable<Cars>): any {
    this.carService.postCar(car);
  }
}
