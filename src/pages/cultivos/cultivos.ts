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
  id_invernadero: any;
  cultivos: any;
	valoresPage = ValoresPage;
	
  constructor(public navCtrl: NavController, public navParams: NavParams,
                                                    private http: Http) {
    this.id_invernadero = this.navParams.get("id_invernadero");
    this.getCultivos();
  }

  getCultivos(){
    this.http.post("/cultivos/", {id_invernadero : this.id_invernadero}).subscribe(
       data=>{
        console.log(data.json());
        this.cultivos = data.json();
    },  error1=>{
        console.log("Error");
    });
  }

  ionViewDidLoad() {
    console.log(this.id_invernadero);
  }

  cambiarValores(){
  	this.navCtrl.push(this.valoresPage);
  }

}
