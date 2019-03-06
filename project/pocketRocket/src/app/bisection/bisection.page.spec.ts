import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BisectionPage } from './bisection.page';

describe('BisectionPage', () => {
  let component: BisectionPage;
  let fixture: ComponentFixture<BisectionPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BisectionPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BisectionPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
