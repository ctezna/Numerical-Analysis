import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MatrixPage } from './matrix.page';

describe('MatrixPage', () => {
  let component: MatrixPage;
  let fixture: ComponentFixture<MatrixPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MatrixPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MatrixPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
