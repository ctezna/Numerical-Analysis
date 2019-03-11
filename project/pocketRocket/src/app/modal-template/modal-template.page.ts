import { Component, OnInit } from '@angular/core';
import { ModalController, NavParams } from '@ionic/angular';

@Component({
  selector: 'app-modal-template',
  templateUrl: './modal-template.page.html',
  styleUrls: ['./modal-template.page.scss'],
})
export class ModalTemplatePage implements OnInit {
  type;
  title;
  description;
  algorithm;
  examples;
  constructor(public modalController:ModalController, public navParams:NavParams) { 
    this.type = this.navParams.get('method');
    if (this.type == 'bisection'){
      this.title = 'Bisection Method'
      this.description = 'dessscpoxire';
      this.algorithm = '<code><font size="2">f: function to be evaluated<br>a: left side of interval<br>b: right side of interval<br>tol: desired tolerance<br> nMax: maximum number'+
                       ' of iterations<br><br><em>bisection(f,a,b,tol,nMax)</em><br>begin<br>'+
                       'var r0 = f(x0)<br>if abs(r0) <= tol<br>&emsp;<strong>x0 is a root of f</strong><br>'+
                       'endif<br>var x1 = x0 + Delta<br>var count= 1<br>var r1 = f(x1)<br>'+
                       'if abs(r1) <= tol<br>&emsp;<strong>x1 is a root of f</strong><br>endif<br>'+
                       'while count < nMax<br>&emsp;if r0*r1 < 0<br>&emsp;&emsp;<strong>There is a root between x0 and x1</strong><br>'+
                       '&emsp;endif<br>&emsp;x0 = x1<br>&emsp;x1 = x1 + Delta<br>&emsp;r0 = f(x0)<br>&emsp;'+
                       'r1 = f(x1)<br>&emsp;count = count + 1<br>endwhile<br>end</font></code>';
      this.examples = 'thilaejr';
    }
  }

  ngOnInit() {
  }


  dismiss(){
    this.modalController.dismiss();
  }

}
