import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { RootAlgorithmsPage } from './root-algorithms.page';
import { ModalTemplatePage } from '../modal-template/modal-template.page';

const routes: Routes = [
  {
    path: '',
    component: RootAlgorithmsPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [RootAlgorithmsPage,ModalTemplatePage],
  entryComponents: [ModalTemplatePage]
})
export class RootAlgorithmsPageModule {}
