import {Component, Input} from '@angular/core';
import {DecimalPipe, NgForOf} from "@angular/common";
import {Mileages} from "../../../interfaces/mileages";
import {NgxPaginationModule} from "ngx-pagination";

@Component({
  selector: 'app-mileages-list',
  standalone: true,
  imports: [
    DecimalPipe,
    NgxPaginationModule,
    NgForOf
  ],
  templateUrl: './mileages-list.component.html',
  styleUrl: './mileages-list.component.scss'
})
export class MileagesListComponent {

  @Input() mileagesData: Mileages[] = [];
  @Input('data') meals: string[] = [];
  page: number = 1;
}
