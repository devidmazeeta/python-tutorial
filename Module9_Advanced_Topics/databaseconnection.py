import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # Default XAMPP MySQL username
    password="",  # Default XAMPP MySQL password
    database="your_database_name"  # Replace with your database name
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM your_table_name")  # Replace with your table name

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
