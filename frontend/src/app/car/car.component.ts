import {Component, OnInit} from '@angular/core';
import {CarService} from "../service/car.service";

@Component({
  selector: 'app-car',
  templateUrl: './car.component.html',
  styleUrls: ['./car.component.scss']
})
export class CarComponent implements OnInit {

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

