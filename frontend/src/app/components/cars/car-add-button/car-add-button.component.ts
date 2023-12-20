import {Component, EventEmitter, Output} from '@angular/core';
import {CarAddFormComponent} from "../car-add-form/car-add-form.component";
import {Cars} from "../../../interfaces/cars";

@Component({
  selector: 'app-car-add-button',
  standalone: true,
    imports: [
        CarAddFormComponent
    ],
  templateUrl: './car-add-button.component.html',
  styleUrl: './car-add-button.component.scss'
})

export class CarAddButtonComponent {

  @Output() addCar: EventEmitter<Cars> = new EventEmitter<Cars>();
  onAddCar(car: Cars) {
    this.addCar.emit(car);
  }

}
