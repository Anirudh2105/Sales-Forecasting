import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictedDataComponent } from './predicted-data.component';

describe('PredictedDataComponent', () => {
  let component: PredictedDataComponent;
  let fixture: ComponentFixture<PredictedDataComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PredictedDataComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PredictedDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
