import { TestBed } from '@angular/core/testing';

import { QroptionsService } from './qroptions.service';

describe('QroptionsService', () => {
  let service: QroptionsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QroptionsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
