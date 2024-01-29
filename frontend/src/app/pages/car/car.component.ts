import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {AsyncPipe, DatePipe, DecimalPipe, JsonPipe} from "@angular/common";
import {CarService} from "../../services/car.service";
import {Cars} from "../../interfaces/cars";
import {Mileages} from "../../interfaces/mileages";
import {MileagesListComponent} from "../../components/car/mileages-list/mileages-list.component";

@Component({
  selector: 'app-car',
  standalone: true,
  imports: [
    AsyncPipe,
    JsonPipe,
    DecimalPipe,
    DatePipe,
    MileagesListComponent
  ],
  templateUrl: './car.component.html',
  styleUrl: './car.component.scss'
})
export class CarComponent implements OnInit {

  //plate:Observable<string|null> = this.router.paramMap.pipe(map((params) => params.get('plate')));
  plate: string | null = this.router.snapshot.paramMap.get('plate');
  carData: Cars[] = [{model: 'ts', plate: 'xd'}];
  mileagesData: Mileages[] = [];

  constructor(private router: ActivatedRoute, private carService: CarService) {
  }

  ngOnInit(): void {
    this.getCarData();
    this.getMileagesData();
  }

  getCarData(): void {
    this.carService.getCarData(this.plate).subscribe((response) => {
      this.carData = Object.values(response);
      //this.carData = response;
      console.log(this.carData);
    });
  }

  getMileagesData(): void {
    this.carService.getMileagesData(this.plate).subscribe((response) => {
      //this.mileagesData = Object.values(response);
      this.mileagesData = [...response].reverse();
      console.log(this.mileagesData);
    });
  }

}
