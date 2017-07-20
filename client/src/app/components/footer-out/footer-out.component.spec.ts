import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FooterOutComponent } from './footer-out.component';

describe('FooterOutComponent', () => {
  let component: FooterOutComponent;
  let fixture: ComponentFixture<FooterOutComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FooterOutComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FooterOutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
