import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-incremental',
  templateUrl: './incremental.page.html',
  styleUrls: ['./incremental.page.scss'],
})
export class IncrementalPage implements OnInit {
  eq:string;
  x0:string;
  delta:string;
  tol:string;
  nmax:string;
  prec:string;
  result:string;
  constructor() { }

  ngOnInit() {
  }

  public incremental(){
    let prec = parseFloat(this.prec);
    let eq = this.eq;
    let x = parseFloat(this.x0);
    let t = x;
    var a;
    let h = parseFloat(this.delta);
    let tol = parseFloat(this.tol);
    let nMax = parseFloat(this.nmax);
    let r0 = parseFloat(eval(eq));
    var roots = [];
    if (Math.abs(r0) <= tol){
      let a = "[" + t.toFixed(prec) + "," + t.toFixed(prec)  + "]";
      roots.push(a);
    }
    let t1 = t + h;
    let count = 0;
    x = t1;
    let r1 = parseFloat(eval(eq));
    if (Math.abs(r1) <= tol){
      let a = "[" + t1.toFixed(prec)  + "," + t1.toFixed(prec)  + "]";
      roots.push(a);
    }
    while (count < nMax){
      if ((r0*r1) < 0){
        let a = "[" + t.toFixed(prec)  + "," + t1.toFixed(prec)  + "]";
        roots.push(a);
      }
      t = t1;
      t1 = t1 + h;
      x = t;
      r0 = parseFloat(eval(eq));
      x = t1;
      r1 = parseFloat(eval(eq));
      count++;
    }
    this.result = roots.toString();
  }
}
