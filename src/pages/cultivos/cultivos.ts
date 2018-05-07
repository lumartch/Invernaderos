import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ValoresPage } from '../valores/valores';
import { Http } from '@angular/http';



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
  invernadero: any;
	valoresPage = ValoresPage;
	
  constructor(public navCtrl: NavController, public navParams: NavParams,
                                                    private http: Http) {
    this.invernadero = this.navParams.get("invernadero");
  }

  /*getCultivos(){
  this.http.post("/invernaderos/", {id_invernadero: this.usuario, pwd: this.password}).subscribe(
      data=>{
      console.log(data.json());
      this.invernaderos = data.json();
  },  error1=>{
      console.log("Error");
  });*/

  ionViewDidLoad() {
    console.log('ionViewDidLoad CultivosPage');
    console.log(this.invernadero);
  }

  cambiarValores(){
  	this.navCtrl.push(this.valoresPage);
  }

}
