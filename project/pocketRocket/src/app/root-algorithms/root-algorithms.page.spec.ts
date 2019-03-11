import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RootAlgorithmsPage } from './root-algorithms.page';

describe('RootAlgorithmsPage', () => {
  let component: RootAlgorithmsPage;
  let fixture: ComponentFixture<RootAlgorithmsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RootAlgorithmsPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RootAlgorithmsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
