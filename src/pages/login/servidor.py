from flask import Flask, request, jsonify
from Usuario import Usuario
from Invernadero import Invernadero

import mysql.connector
conexion = mysql.connector.connect(user= 'lumart', password='', database= 'Invernadero')
cursor = conexion.cursor()

app = Flask(__name__)

usuarioBD = Usuario(conexion, cursor)
invernaderoBD = Invernadero(conexion, cursor)

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

@app.route('/invernaderos/', methods=['POST'])
def invernaderos():

	if request.is_json:
		json = request.get_json()
		u = json['user']
		p = json['pwd']
	return jsonify(invernaderoBD.getInvernaderos(u, p))

#@app.route('/cultivos/', methods=['POST'])
#def cultivos():
#	if request.is_json:
#		json = request.get_json()
#		id_invernadero = json['id_invernadero']
	#return jsonify()
app.run()
