import {Component, EventEmitter, Input, Output} from '@angular/core';
import {DatePipe, NgForOf} from "@angular/common";
import {RecordPerModel} from "../../../interfaces/record-per-model";

@Component({
  selector: 'app-car-list',
  standalone: true,
  imports: [
    NgForOf,
    DatePipe
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

