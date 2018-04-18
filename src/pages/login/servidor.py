from flask import Flask, request
from Usuario import Usuario

import mysql.connector
conexion = mysql.connector.connect(user= 'lumart', password='', database= 'Invernadero')
cursor = conexion.cursor()

app = Flask(__name__)

usuarioBD = Usuario(conexion, cursor)

@app.route('/')
def hola():
	return "Hello friend"

@app.route('/login/', methods=['GET'])
def login():
	if request.method == 'GET':
		u = request.args.get('user')
		p = request.args.get('pwd')
		print(u)
		print(p)

	return str(usuarioBD.login(u, p))

app.run()