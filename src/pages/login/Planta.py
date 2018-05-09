class Planta:
	def __init__(self, conexion, cursor):
		self.con = conexion
		self.cur = cursor

	def crear(self, cultivo, fecha, id_Inv):
		try:
			insert = ("INSERT INTO planta(cultivo,fecha,id_invernadero) values (%s, NOW(), %s)")
			self.cur.execute(insert, (cultivo, id_Inv))
		except:
			raise ValueError("\nNo existe el invernadero.")
		self.con.commit()
	
	def modificar(self, cultivo, id_Plan):
		try:
			modificar = ("UPDATE planta SET cultivo = %s WHERE id = %s")
			self.cur.execute(modificar, (cultivo, id_Plan))
		except:
			raise ValueError("\nNo existe la planta.")
		self.con.commit()
	
	def eliminar(self, id_Inv):
		eliminar = ("DELETE FROM planta WHERE id = %s ")
		self.cur.execute(eliminar, (id_Inv, ))
		self.con.commit()

	def buscar(self, id_Inv):
		__busqueda = ("SELECT * FROM planta WHERE id_invernadero = %s")
		self.cur.execute(__busqueda, (id_Inv, ))
		resultados = self.cur.fetchall()
		lista = []
		for c in resultados:
			cultivo = {
				"id" : c[0],
				"nombre" : c[1],
				"fecha" :c[2].isoformat()
			}
			lista.append(cultivo)
		return lista

	def mostrar(self):
		select = ("SELECT * FROM planta")
		self.cur.execute(select)	
		resultados = self.cur.fetchall()
		return resultados
