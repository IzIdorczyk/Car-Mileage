import { Component } from '@angular/core';
import {CarAddFormComponent} from "../car-add-form/car-add-form.component";

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
}
