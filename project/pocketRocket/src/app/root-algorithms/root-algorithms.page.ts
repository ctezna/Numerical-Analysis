import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { ModalTemplatePage } from '../modal-template/modal-template.page';

@Component({
  selector: 'app-root-algorithms',
  templateUrl: './root-algorithms.page.html',
  styleUrls: ['./root-algorithms.page.scss'],
})
export class RootAlgorithmsPage implements OnInit {
  //bisection method vars
  eqBisection:string;
  aBisection:string;
  bBisection:string;
  tolBisection:string;
  nmaxBisection:string;
  precBisection:string;
  resultBisection:string;
  constructor(public modalController: ModalController) { }

  ngOnInit() {
  }
  async showModal(method){
    const modal = await this.modalController.create({
      component: ModalTemplatePage,
      componentProps: { method: method }
    });

    await modal.present();
  }

  public bisection(){
    let a = parseFloat(this.aBisection);
    let b = parseFloat(this.bBisection);
    let prec = parseFloat(this.precBisection);
    var c;
    let x = a;
    let eq = this.eqBisection;
    let tol = parseFloat(this.tolBisection);
    let nmax = parseFloat(this.nmaxBisection);
    let fa = eval(eq);
    x = b;
    let fb = eval(eq);
    if (Math.abs(fa) <= tol){
      this.resultBisection = a.toFixed(prec).toString();
    }else{
      if (Math.abs(fb) <= tol){
        this.resultBisection = b.toFixed(prec).toString();
      }else{
        let c = (a+b)/2;
        x = c;
        let fc = eval(eq);
        let count = 0;
        while (count < nmax && (Math.abs(a-b) > tol)){
          if((fa*fc) < 0){
            b = c;
            x = b;
            fb = eval(eq);
            c = (a+b)/2;
            x = c;
            fc = eval(eq);
          }
          if((fb*fc) < 0){
            a = c;
            x = a;
            fa = eval(eq);
            c = (a+b)/2;
            x = c;
            fc = eval(eq);
          }
          count++;
        }
        this.resultBisection = c.toFixed(prec).toString();
      }
    }
  }




}
