import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { Http } from '@angular/http';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  usuario:string;
  password:string;
  invernaderos:any;
  constructor(public navCtrl: NavController,
  				public navParams: NavParams,
          private http: Http) {
          this.usuario = this.navParams.get('user');
          this.password = this.navParams.get('pwd');

          this.getInvernaderos();
  }

  getInvernaderos(){
    this.http.post("/invernaderos/", {user: this.usuario, pwd: this.password}).subscribe(
       data=>{
        console.log(data.json());
        this.invernaderos = data.json();
    },  error1=>{
        console.log("Error");
    });
  }
  
  cambiarCultivos(i){
    console.log(i);
    //this.navCtrl.push(this.culivosPage);
  }

}
