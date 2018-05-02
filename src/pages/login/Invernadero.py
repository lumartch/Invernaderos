import hashlib
class Invernadero:
	def __init__(self, conexion, cursor):
		self.con = conexion
		self.cur = cursor

	def crear(self, ubicacion, nombre, id_duenio):
		try:
			insert = ("INSERT INTO invernadero(ubicacion,nombre,id_duenio) values (%s,%s,%s)")
			self.cur.execute(insert, (ubicacion, nombre, id_duenio))
			self.con.commit()
		except:
			raise ValueError("No existe el dueño.")
	
	def modificar(self, ubicacion, nombre, id_Inv):
		modificar = ("Update invernadero set ubicacion = %s, nombre = %s where id = %s")
		self.cur.execute(modificar, (ubicacion, nombre, id_Inv))
		self.con.commit()

	def eliminar(self, id_Inv):
		eliminar = ("DELETE FROM invernadero WHERE id = %s ")
		self.cur.execute(eliminar, (id_Inv, ))
		self.con.commit()

	def buscar(self, nombre):
		__busqueda = ("SELECT * FROM invernadero WHERE nombre LIKE %s")
		self.cur.execute(__busqueda, ('%' + nombre + '%', ))
		resultados = self.cur.fetchall()
		return resultados

	def mostrar(self):
		select = ("SELECT * FROM invernadero")
		self.cur.execute(select)	
		resultados = self.cur.fetchall()
		return resultados

	def agregarInvernaderoUsuario(self, id_usuario, id_invernadero):
		insertar = ("INSERT INTO usuario_invernadero(id_usuario, id_invernadero) VALUES(%s, %s)")
		self.cur.execute(insertar, (id_usuario, id_invernadero))
		self.con.commit()

	def getInvernaderos(self, user, password):
		pass_hash = hashlib.new('sha1', bytes(password, 'utf-8'))
		pass_hash = pass_hash.hexdigest()
		select_ususario = ("SELECT id FROM usuario WHERE username = %s AND password = %s")
		self.cur.execute(select_ususario, (user, pass_hash))
		id = self.cur.fetchall()
		print(id)

		lista = []
		if id:
			id = id[0][0]
			print("Id usuario: ", id)
			select_usr_inv = ("SELECT id_invernadero FROM usuario_invernadero WHERE id_usuario = %s")
			self.cur.execute(select_usr_inv, (id, ))
			invernaderos_id = self.cur.fetchall()
			print ("Id_Invernaderos", invernaderos_id)

			for i in invernaderos_id:
				inver = i[0]
				#obtener invernaderos
				select_invernadero = ("SELECT * FROM invernadero WHERE id = %s")
				self.cur.execute(select_invernadero, (inver, ))
				res = self.cur.fetchall()
				print (res)


				if res:
					select_plantas = "SELECT COUNT(id) FROM planta WHERE id_invernadero = %s"
					self.cur.execute(select_plantas, (res[0][0], ))
					plantas = self.cur.fetchall()
					invernadero = {
						"id": res[0][0],
						"ubicacion": res[0][1],
						"nombre": res[0][2],
						"cultivos": plantas
					}
					lista.append(invernadero)
			print(lista)
		return lista
			