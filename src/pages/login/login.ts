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
  home = HomePage;

  constructor(public navCtrl: NavController,
              public navParams: NavParams,
              private http: Http,
              private alerta: AlertController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
  }

  clickButton(){

    this.http.get(`/login/?user=${this.usuario}&pwd=${this.password}`).subscribe(data =>{
      console.log("Exito");
      if(data.text() == "True"){
        this.navCtrl.setRoot(this.home, {user: this.usuario, pwd: this.password});
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
