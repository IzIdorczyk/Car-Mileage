import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {CarAddButtonComponent} from "../../components/cars/car-add-button/car-add-button.component";
import {CarListComponent} from "../../components/cars/car-list/car-list.component";
import {CarsService} from "../../services/cars.service";
import {Cars} from "../../interfaces/cars";
import {RecordPerModel} from "../../interfaces/record-per-model";
import {Observable} from "rxjs";

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
export class CarsComponent implements OnInit {
  // stan aplikacji, w duzych redux
  cars: Cars[] = [];
  records: RecordPerModel[] = [];
  //najpierw angularowe
  //kolejnosc te co uzywaja innych sa wyzej
  //popjular patern <nerd>

  constructor(private carService: CarsService) {
  }

  ngOnInit(): void {
    this.reloadCars();
  }

  updateCarList(): void {
    this.carService.getCars().subscribe((response) => {
      this.records = response;
    });
  }

  reloadCars(): void {
    this.updateCarList();
  }

  deleteCar(plate: string): void {
    this.carService.deleteCar(plate).subscribe(() => {
      this.reloadCars();
    });
  }

  addCar(car: Cars): void {
    this.carService.postCar(car).subscribe((response: Cars) => {
      console.log(response);
      this.reloadCars();
    });
  }
}
