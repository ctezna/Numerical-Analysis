import { Component, OnInit } from '@angular/core';
import { ModalController, NavParams } from '@ionic/angular';

@Component({
  selector: 'app-incremental-modal',
  templateUrl: './incremental-modal.page.html',
  styleUrls: ['./incremental-modal.page.scss'],
})
export class IncrementalModalPage implements OnInit {
  type;
  title;
  description;
  algorithm;
  examples;
  constructor(public modalController:ModalController, public navParams:NavParams) { 
    this.type = this.navParams.get('method');
    if (this.type == 'incremental'){
      this.title = 'Incremental Search';
      this.description = 'The incremental search method is a numerical method that is used when is needed to find an interval'+
                          ' of two values of ‘x’ that is meant to contain at least one root. '+
                          'The incremental search method starts with an initial value X0, a final value X1'+
                          ' (Lower and upper limits of the interval, respectively) and a constant called Delta. '+
                           'This constant is going to be added to the lower limit of the interval in each iteration' +
                           'in order to go from X0 to X1. ' +
                          'We can find the value of x1 easily with this equation:'+'<br><br>'+
                          '&emsp;&emsp;<strong>x1 = x0 + Delta</strong><br><br>'+'If we convert that equation into an iterative one we got:<br><br>'+
                          '&emsp;&emsp;<strong>xN = xN-1 + Delta</strong><br><br>'+ 'With the expression mentioned above, we have already a series'+
                          ' of values of ‘x’ that we can evaluate on the function.'+
                          ' The solution is to evaluate a pair of continue values of ‘x’ we obtained previously on'+
                          ' the function, multiply the images generated and see which sign we obtain:<br><br>&emsp;<strong>f(xN-1)* f(xN)'+
                          ' > 0</strong>: then there is no root between these two values of x.<br>'+
                          '&emsp;<strong>f(xN-1)* f(xN)  < 0</strong>: we can assure that a root exists between the interval <strong>[xN-1,xN]</strong>.';
      this.algorithm = '<code><font size="2">f: function to be evaluated<br>x0: initial x value<br>Delta: change in x<br>tol: desired tolerance<br> nMax: maximum number'+
                       ' of iterations<br><br><em>incrementalSearch(f,x0,Delta,tol,nMax)</em><br>begin<br>'+
                       'var r0 = f(x0)<br>if abs(r0) <= tol<br>&emsp;<strong>x0 is a root of f</strong><br>'+
                       'endif<br>var x1 = x0 + Delta<br>var count= 1<br>var r1 = f(x1)<br>'+
                       'if abs(r1) <= tol<br>&emsp;<strong>x1 is a root of f</strong><br>endif<br>'+
                       'while count < nMax<br>&emsp;if r0*r1 < 0<br>&emsp;&emsp;<strong>There is a root between x0 and x1</strong><br>'+
                       '&emsp;endif<br>&emsp;x0 = x1<br>&emsp;x1 = x1 + Delta<br>&emsp;r0 = f(x0)<br>&emsp;'+
                       'r1 = f(x1)<br>&emsp;count = count + 1<br>endwhile<br>end</font></code>';
      this.examples = 'Consider the equation <em>f(x) = x^(1/2) * cos(x) + 1</em><br><br>'+
                      'If we choose an initial x value of 1 and a Delta of 1 we can iterate through the function.' +
                      ' In each step evaluating x0 and x1 to see where we find a change in signs.<br><br>' +
                      'We start by solving f(x0): f(1) = 1^(1/2) * cos(1) + 1, we keep in mind that the answer is positive'+
                      'next we get x1 by x1 = x0 + Delta. (x1 = 2). We evalute f(x1): f(2) = positive. Since f(x0) and f(x1)'+
                      ' both gave positive results, we generate new x0 and x1 values. x0 = x1 and x1 = x1 + Delta, which results'+
                      'in x0 = 2 and x1 = 3. Next, x0 and x1 are reevaluated in f(). f(x0): positive, f(x1): negative.'+
                      ' Here since f(x0) and f(x1) gave different signs, we can assure that there is at least one root between' +
                      ' x0 and x1. In this case x0 = 2 and x1 = 3.';
    }
  }

  ngOnInit() {
  }


  dismiss(){
    this.modalController.dismiss();
  }
}
