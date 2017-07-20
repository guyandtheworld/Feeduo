import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderOutComponent } from './header-out.component';

describe('HeaderOutComponent', () => {
  let component: HeaderOutComponent;
  let fixture: ComponentFixture<HeaderOutComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HeaderOutComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HeaderOutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
