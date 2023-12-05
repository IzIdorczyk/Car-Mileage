import { Component } from '@angular/core';
import {AddCarFormComponent} from "../add-car-form/add-car-form.component";

@Component({
  selector: 'app-add-car-button',
  standalone: true,
  imports: [
    AddCarFormComponent
  ],
  templateUrl: './add-car-button.component.html',
  styleUrl: './add-car-button.component.scss'
})
export class AddCarButtonComponent {

}
