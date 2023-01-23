import mysql.connector

mysql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "",
)
if mysql.is_connected():
    print("Anda Berhasil Connect Ke Database")