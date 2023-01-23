import mysql.connector
import tkinter as tk

# ngekoneksi ke database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="uas_bp"
)

# ngebuat cursor
cursor = conn.cursor()

# Function untuk insert data ke database
def insert_data():
    id = entry_id.get()
    name = entry_name.get()
    email = entry_email.get()
    cursor.execute("INSERT INTO users (id, name, email) VALUES (%s, %s, %s)", (id, name, email))
    conn.commit()
    label.config(text="Data inserted successfully!")

# Function untuk fetch data database
def fetch_data():
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    return results

# GUI
root = tk.Tk()
root.title("Database App")

label = tk.Label(root, text="Enter user information:")
label.grid(row=0, column=0, columnspan=2)

id_label = tk.Label(root, text="ID:")
id_label.grid(row=1, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=1, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=2, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=2, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

insert_button = tk.Button(root, text="Enter", command=insert_data)
insert_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
