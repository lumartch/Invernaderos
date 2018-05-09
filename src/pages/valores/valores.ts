import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { Http } from '@angular/http';

/**
 * Generated class for the ValoresPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-valores',
  templateUrl: 'valores.html',
})
export class ValoresPage {
  id_planta : any;
  valores: any;

  constructor(public navCtrl: NavController, public navParams: NavParams,private http: Http) {
    this.id_planta = this.navParams.get("id_planta");
    this.getValores();
  }

  getValores(){
    this.http.post("/valores/", { id_planta : this.id_planta}).subscribe(
       data=>{
        console.log(data.json());
        this.valores = data.json();
    },  error1=>{
        console.log("Error");
    });
  }
  ionViewDidLoad() {
    console.log(this.valores);
  }

}
