import {Component} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {Observable} from "rxjs";
import {Cars} from "../../interface/cars";
import {CarService} from "../../service/car.service";

@Component({
    selector: 'app-add-car-form',
    standalone: true,
    imports: [
        FormsModule,
        ReactiveFormsModule
    ],
    templateUrl: './add-car-form.component.html',
    styleUrl: './add-car-form.component.scss'
})
export class AddCarFormComponent {
    car: any = [];

    constructor(private carService: CarService) {
    }

    createCar(car: Observable<Cars>): any {
        this.carService.postCar(car);
    }

}
