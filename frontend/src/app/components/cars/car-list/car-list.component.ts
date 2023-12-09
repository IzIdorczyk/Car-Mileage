import {Component, OnInit} from '@angular/core';
import {DatePipe, formatDate, NgForOf} from "@angular/common";
import {CarsService} from "../../../services/cars.service";

@Component({
  selector: 'app-car-list',
  standalone: true,
  imports: [
    NgForOf,
    DatePipe
  ],
  templateUrl: './car-list.component.html',
  styleUrl: './car-list.component.scss'
})

export class CarListComponent implements OnInit {
  cars: any = [];

  constructor(private carService: CarsService) {
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

  protected readonly formatDate = formatDate;
}

