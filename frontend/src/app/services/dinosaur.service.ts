import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import {Dinosaur} from "../dinosaur";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class DinosaurService {

  constructor(private http: HttpClient) {}

  getDinosaursFromServer(): Observable<Array<Dinosaur>> {
    return this.http.get<Dinosaur[]>('http://127.0.0.1:8001/api/dinosaur');
  }

}
