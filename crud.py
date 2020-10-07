from mysql.connector import connect

connection = connect(host='localhost',database='jw',user='root',password='123456',auth_plugin='mysql_native_password')

print('Intentando conectar con la MySql...')
if connection.is_connected():
	print("Conexion establecida con exito")

def agregar(datos):
	connection = connect(host='localhost',database='jw',user='root',password='123456',auth_plugin='mysql_native_password')
	sql_stmt = "INSERT INTO empleado (codempleado,nombres_empleado,apellidos_empleado,telefono_empleado,edad_empleado,salario_empleado,genero,cargo,civil,estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

	cursor = connection.cursor(prepared=True)
	cursor.execute(sql_stmt,datos)
	connection.commit()
	cursor.close()
	connection.close()

	print("Se registro con exito!")
#(codempleado,nombres_empleado,apellidos_empleado,telefono_empleado,edad_empleado,salario_empleado,genero,cargo,civil,estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
def modificar(datos2):
	connection = connect(host='localhost',database='jw',user='root',password='123456',auth_plugin='mysql_native_password')
	sql_stmt = "UPDATE empleado SET  nombres_empleado = %s, apellidos_empleado = %s, telefono_empleado = %s, edad_empleado= %s,salario_empleado = %s,estado = %s WHERE codempleado = %s"

	cursor = connection.cursor(prepared=True)
	cursor.execute(sql_stmt,datos2)
	connection.commit()
	cursor.close()
	connection.close()

	print("Se Actualizo con exito!")

def delete(iden):
	connection = connect(host='localhost',database='jw',user='root',password='123456',auth_plugin='mysql_native_password')
	sql_stmt = f"DELETE FROM empleado WHERE codempleado LIKE '%{(iden)}%'"
	cursor = connection.cursor(prepared=True)
	cursor.execute(sql_stmt)
	connection.commit()
	cursor.close()
	connection.close()

	print("Registro eliminado con exito")

