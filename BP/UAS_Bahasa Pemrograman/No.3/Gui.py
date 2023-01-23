import tkinter as tk

def on_select(v):
    label.config(text="Kamu punya pilihan " + v)

root = tk.Tk()
root.title("Advanced GUI")

label = tk.Label(root, text="Pilih:")
label.pack()

var = tk.StringVar(value='Opsi 1')

option1 = tk.Radiobutton(root, text='opsi 1', variable=var, value='Opsi 1', command=lambda: on_select(var.get()))
option1.pack()

option2 = tk.Radiobutton(root, text='Opsi 2', variable=var, value='Opsi 2', command=lambda: on_select(var.get()))
option2.pack()

option3 = tk.Radiobutton(root, text='Opsi 3', variable=var, value='Opsi 3', command=lambda: on_select(var.get()))
option3.pack()

submit = tk.Button(root, text="Submit", command=root.quit)
submit.pack()

root.mainloop()
