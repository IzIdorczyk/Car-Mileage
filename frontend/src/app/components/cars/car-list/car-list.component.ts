import {Component, EventEmitter, Input, Output} from '@angular/core';
import {DatePipe, DecimalPipe, NgForOf} from "@angular/common";
import {RecordPerModel} from "../../../interfaces/record-per-model";
import {RouterLink} from "@angular/router";

@Component({
  selector: 'app-car-list',
  standalone: true,
  imports: [
    NgForOf,
    DatePipe,
    RouterLink,
    DecimalPipe
  ],
  templateUrl: './car-list.component.html',
  styleUrl: './car-list.component.scss',
})

export class CarListComponent {

  @Input() records: RecordPerModel[] = [];

  @Output() deleteCar: EventEmitter<string> = new EventEmitter<string>();

  onDeleteCar(plate: string) {
    this.deleteCar.emit(plate);
  }
}

