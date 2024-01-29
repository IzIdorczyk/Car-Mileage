import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MileagesListComponent } from './mileages-list.component';

describe('MileagesListComponent', () => {
  let component: MileagesListComponent;
  let fixture: ComponentFixture<MileagesListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MileagesListComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MileagesListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
