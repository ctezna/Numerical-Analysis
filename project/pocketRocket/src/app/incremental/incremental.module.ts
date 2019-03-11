import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { IncrementalPage } from './incremental.page';
import { ModalTemplatePage } from '../modal-template/modal-template.page';

const routes: Routes = [
  {
    path: '',
    component: IncrementalPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [IncrementalPage, ModalTemplatePage],
  entryComponents: [ModalTemplatePage]
})
export class IncrementalPageModule {}
