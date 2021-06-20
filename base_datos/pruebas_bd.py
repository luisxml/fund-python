import psycopg2

try:
    conexion = psycopg2.connect(user='postgres', password='Sql.123', host='127.0.0.1',port='5432', database='test_db')
    cursor = conexion.cursor()
    sentencia = 'SELECT * FROM persona'
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    print(registros)
    cursor.close()
    conexion.close()

except Exception as e:
    print("Ocurrió un error: ", e) 

