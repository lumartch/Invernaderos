import hashlib

class Usuario:
	def __init__(self, conexion, cursor):
		self.con = conexion
		self.cur = cursor
	
	def crear(self, username, password, tipo):
		insertar = ("INSERT INTO usuario(username, password, id_tipo) VALUES (%s, %s, %s)")
		h = hashlib.new('sha1', bytes(password, 'utf-8'))
		password = h.hexdigest(	)
		self.cur.execute(insertar, (username, password, tipo))
		self.con.commit()

	def modificar(self, password, username):
		modificar = ('UPDATE usuario SET password = %s WHERE username = %s')
		self.cur.execute(modificar, (password, username))
		self.con.commit()

	def login(self, username, password):
		pass_hash = hashlib.new('sha1', bytes(password, 'utf-8'))
		pass_hash = pass_hash.hexdigest()

		select = ("SELECT * FROM usuario WHERE username = %s and password = %s")
		self.cur.execute(select, (username, pass_hash))

		resultado = self.cur.fetchall();

		if resultado:
			return True;
		else:
			return False;

	def buscar(self, username):
		__busqueda = ("SELECT * FROM usuario WHERE username = %s")
		self.cur.execute(__busqueda, (username, ))
		resultados = self.cur.fetchall()

		return resultados