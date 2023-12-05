import {Component, OnInit} from '@angular/core';
import {NgForOf} from "@angular/common";
import {CarService} from "../../service/car.service";
import {Observable} from "rxjs";
import {Cars} from "../../interface/cars";


@Component({
  selector: 'app-car-list',
  standalone: true,
    imports: [
        NgForOf
    ],
  templateUrl: './car-list.component.html',
  styleUrl: './car-list.component.scss'
})
export class CarListComponent implements OnInit {

  cars: any = [];

  constructor(private carService: CarService) {
  }

  onGetCars(): any {
    this.carService.getCars().subscribe((response) => {
        this.cars = response;
      }
    );
  }



  ngOnInit(): void {
    this.onGetCars();
  }
}
