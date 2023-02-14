import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QrshowComponent } from './qrshow.component';

describe('QrshowComponent', () => {
  let component: QrshowComponent;
  let fixture: ComponentFixture<QrshowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ QrshowComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QrshowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
