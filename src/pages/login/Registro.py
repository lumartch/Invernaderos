class Registro:
	def __init__(self, conexion, cursor):
		self.con = conexion
		self.cur = cursor

	def crear(self, ph, luz, humedad, co2, id_planta):
		try:
			insert = ("INSERT INTO registro(fecha, ph, luz, humedad, co2, id_planta) values (NOW(), %s ,%s, %s ,%s, %s)")
			self.cur.execute(insert, (ph, luz, humedad, co2, id_planta))
		except:
			raise ValueError("\nNo existe la planta.")
		self.con.commit()
	
	def modificar(self, cultivo, id_Plan):
		try:
			modificar = ("UPDATE registro SET cultivo = %s WHERE id = %s")
			self.cur.execute(modificar, (cultivo, id_Plan))
		except:
			raise ValueError("\nNo existe la planta.")
		self.con.commit()

	def eliminar(self, id_planta):
		eliminar = ("DELETE FROM planta WHERE id = %s ")
		self.cur.execute(eliminar, (id_planta, ))
		self.con.commit()

	def buscar(self, id_planta):
		__busqueda = ("SELECT * FROM registro WHERE id_planta = %s ORDER BY fecha DESC")
		self.cur.execute(__busqueda, (id_planta, ))
		resultados = self.cur.fetchall()
		lista = []
		for r in resultados:
			valores={
				"id": r[0],
				"fecha": r[1],
				"ph": r[2],
				"luz": r[3],
				"humedad": r[4],
				"co2": r[5]
			}
			lista.append(valores)
		return lista

	def mostrar(self):
		select = ("SELECT * FROM registro")
		self.cur.execute(select)	
		resultados = self.cur.fetchall()
		return resultados