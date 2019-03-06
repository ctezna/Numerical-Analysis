import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IncrementalPage } from './incremental.page';

describe('IncrementalPage', () => {
  let component: IncrementalPage;
  let fixture: ComponentFixture<IncrementalPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IncrementalPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IncrementalPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
