import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'welcome',
    pathMatch: 'full'
  },
  {
    path: 'home',
    loadChildren: './home/home.module#HomePageModule'
  },
  { path: 'welcome', loadChildren: './welcome/welcome.module#WelcomePageModule' },
  { path: 'incremental', loadChildren: './incremental/incremental.module#IncrementalPageModule' },
  { path: 'help', loadChildren: './help/help.module#HelpPageModule' },
  { path: 'matrix', loadChildren: './matrix/matrix.module#MatrixPageModule' },
  { path: 'root-algorithms', loadChildren: './root-algorithms/root-algorithms.module#RootAlgorithmsPageModule' },
  { path: 'modal-template', loadChildren: './modal-template/modal-template.module#ModalTemplatePageModule' },
  { path: 'incremental-modal', loadChildren: './incremental-modal/incremental-modal.module#IncrementalModalPageModule' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
