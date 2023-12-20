import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {catchError, Observable, Subscription, tap, throwError} from "rxjs";
import {Cars} from '../interfaces/cars';
import {RecordPerModel} from "../interfaces/record-per-model";

const BASE_URL: string = 'http://127.0.0.1:8000/';


@Injectable({
  providedIn: 'root'
})


export class CarsService {

  constructor(private http: HttpClient) {
  }

  getCars(): Observable<RecordPerModel[]> {
    return this.http.get<RecordPerModel[]>(`${BASE_URL}last_record_per_model`).pipe(
      tap(record => console.log(record)),
      catchError(err => {
          console.error(err);
          return throwError(err)
        }
      ));
  }

  postCar(car: Cars): Observable<Cars> {
    return this.http.post<Cars>(`${BASE_URL}car/`, car);
  }

  deleteCar(car: string): Observable<void> {
    return this.http.delete<void>(`${BASE_URL}car/${car}`).pipe(
      catchError(error => {
        console.error('Error:', error)
        return throwError(error);
      })
    );
  }
}
