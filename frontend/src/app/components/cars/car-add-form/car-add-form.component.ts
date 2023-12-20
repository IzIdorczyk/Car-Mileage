import {Component, EventEmitter, Output} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
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



  @Output() addCar: EventEmitter<Cars> = new EventEmitter<Cars>();

  onAddCar(car: Cars) {
    this.addCar.emit(car);
  }
}
