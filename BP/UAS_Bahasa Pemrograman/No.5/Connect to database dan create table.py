import mysql.connector

# ngekoneksi ke databasenya
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="uas_bp"
)

cursor = cnx.cursor()
# Membuat tabelnya
create_table = """
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
"""
cursor.execute(create_table)

# Menambahkan data
add_user = "INSERT INTO users (name, email) VALUES (%s, %s)"
user_data = ("Pozyomka", "pozye@example.com")
cursor.execute(add_user, user_data)
cnx.commit()

# Mengambil data
query = "SELECT * FROM users"
cursor.execute(query)

for (id, name, email) in cursor:
    print("ID: {}, Name: {}, Email: {}".format(id, name, email))

# Menutup koneksi
cursor.close()
cnx.close()