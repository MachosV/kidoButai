import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QreditorComponent } from './qreditor.component';

describe('QreditorComponent', () => {
  let component: QreditorComponent;
  let fixture: ComponentFixture<QreditorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ QreditorComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QreditorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
