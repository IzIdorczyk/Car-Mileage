import { Injectable } from '@angular/core';
import {catchError, Observable, throwError} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";
import {Cars} from "../interfaces/cars";
import {Mileages} from "../interfaces/mileages";

const BASE_URL: string = environment.apiUrl;
@Injectable({
  providedIn: 'root'
})
export class CarService {

  constructor(private http: HttpClient) {
  }

  getCarData(plate: string | null): Observable<Cars[]> {
    return this.http.get<Cars[]>(`${BASE_URL}car/${plate}`).pipe(
      catchError(err => {
          console.error(err);
          return throwError(err)
        }
      ));
  }

  getMileagesData(plate: string | null): Observable<Mileages[]> {
    return this.http.get<Mileages[]>(`${BASE_URL}car/${plate}/mileages`).pipe(
      catchError(err => {
          console.error(err);
          return throwError(err)
        }
      ));
  }

}

