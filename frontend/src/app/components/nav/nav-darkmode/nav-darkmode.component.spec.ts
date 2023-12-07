import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavDarkmodeComponent } from './nav-darkmode.component';

describe('NavDarkmodeComponent', () => {
  let component: NavDarkmodeComponent;
  let fixture: ComponentFixture<NavDarkmodeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NavDarkmodeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(NavDarkmodeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
