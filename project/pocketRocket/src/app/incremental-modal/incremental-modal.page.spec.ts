import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IncrementalModalPage } from './incremental-modal.page';

describe('IncrementalModalPage', () => {
  let component: IncrementalModalPage;
  let fixture: ComponentFixture<IncrementalModalPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IncrementalModalPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IncrementalModalPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
