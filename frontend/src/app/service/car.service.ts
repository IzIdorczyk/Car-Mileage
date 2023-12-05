import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable, Subscription} from "rxjs";
import { Cars } from '../interface/cars';
@Injectable({
  providedIn: 'root'
})
export class CarService {

  constructor(private http: HttpClient) {
  }

  getCars(): Observable<Cars[]> {
    return this.http.get<Cars[]>('http://127.0.0.1:8000/cars');
  }

  postCar(car: Observable<Cars>): Subscription{
    return this.http.post<Cars>('http://127.0.0.1:8000/car/', car).subscribe(
      (res => {
        console.log(res);
      })
    );
  }
}
