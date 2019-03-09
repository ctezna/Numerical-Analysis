import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})
export class AppComponent {
  public appPages = [
    {
      title: 'Grapher',
      url: '/home',
      icon: 'analytics'
    },
    {
      title: 'Incremental Search',
      url: '/incremental',
      icon: 'barcode'
    },
    {
      title: 'Bisection Method',
      url: '/bisection',
      icon: 'code-download'
    },
    {
      title: 'Help and Documentation',
      url: '/help',
      icon: 'book'
    },
  ];

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }
  
}
