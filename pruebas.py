import mysql.connector

#establish a connection
conexion = mysql.connector.connect(user='root', password='', host='localhost', database='projecte1', port='3306')

#create a cursor object
cursor = cnx.cursor()

#execute some SQL commands
cursor.execute("SELECT * FROM employees")
        
#fetch the result
result = cursor.fetchall()

#iterate through the result
for row in result:
    print(row)

#close the cursor and connection
cursor.close()
cnx.close()
