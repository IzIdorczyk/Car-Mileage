import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarAddButtonComponent } from './car-add-button.component';

describe('CarAddButtonComponent', () => {
  let component: CarAddButtonComponent;
  let fixture: ComponentFixture<CarAddButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CarAddButtonComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CarAddButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
