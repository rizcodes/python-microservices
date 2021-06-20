import { TestBed } from '@angular/core/testing';

import { DinosaurService } from './dinosaur.service';

describe('DinosaurService', () => {
  let service: DinosaurService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DinosaurService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
