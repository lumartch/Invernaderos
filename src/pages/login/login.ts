import { Component } from '@angular/core';
import {AlertController, IonicPage, NavController, NavParams} from 'ionic-angular';
import { HomePage } from "../home/home";
import { Http } from '@angular/http';

/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {
  usuario:String = "";
  password:String = "";

  constructor(public navCtrl: NavController,
              public navParams: NavParams,
              private http: Http,
              private alerta: AlertController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
  }

  clickButton(){
  	console.log("Se hizo click");
    console.log(this.usuario);
    console.log(this.password);

    //this.navCtrl.setRoot(HomePage);

    this.http.get("/login/?user=" + this.usuario +
    "&pwd=" + this.password).subscribe(data =>{
      console.log("Exito");
      console.log(data.text());
      if(data.text() == "True"){
        this.navCtrl.setRoot(HomePage);
      }
      else{
        let a = this.alerta.create({
        title: "Error",
        subTitle: "El usuario no existe o la contraseña es incorrecta.",
        buttons: ["Ok"]
        });
        a.present();
      }
    }, error =>{
      console.log("ERROR.");
    });
  }
}
