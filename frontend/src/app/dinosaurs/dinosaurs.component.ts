import { Component, OnInit } from '@angular/core';
import {Dinosaur} from "../dinosaur";
import {DinosaurService} from "../services/dinosaur.service";
import {Observable} from "rxjs";

@Component({
  selector: 'app-dinosaurs',
  templateUrl: './dinosaurs.component.html',
  styleUrls: ['./dinosaurs.component.css']
})

export class DinosaursComponent implements OnInit {
  dinosaurs: Array<Dinosaur>;
  errorMsg: String;

  constructor(private dinosaurService: DinosaurService) {
    this.getDinosaurs()
  }

  ngOnInit(): void {
  }

  getDinosaurs(): void {
    this.dinosaurService.getDinosaursFromServer().subscribe(
      data => {
        if (!data.length) {
          this.errorMsg = 'No Dinosaurs found in the database';
          this.dinosaurs = [];
        } else {
          this.dinosaurs = data;
          this.errorMsg = '';
        }
      },
      error => {
        this.errorMsg = 'Server down: HTTP failure (api/dinosaur)'
      }
    );
  }

}
