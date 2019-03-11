import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { IncrementalModalPage } from './incremental-modal.page';

const routes: Routes = [
  {
    path: '',
    component: IncrementalModalPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [IncrementalModalPage]
})
export class IncrementalModalPageModule {}
