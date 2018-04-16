import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { CultivosPage } from '../cultivos/cultivos';
import { ValoresPage } from '../valores/valores';



/**
 * Generated class for the CultivosPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-cultivos',
  templateUrl: 'cultivos.html',
})
export class CultivosPage {
	valoresPage = ValoresPage;
	
  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad CultivosPage');
  }
  cambiarValores(){
  	this.navCtrl.push(this.valoresPage);
  }

}
