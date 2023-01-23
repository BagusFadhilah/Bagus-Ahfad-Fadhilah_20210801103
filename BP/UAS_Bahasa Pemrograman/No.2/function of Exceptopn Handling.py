try:
    x = int(input("Masukan Angka: "))
    y = int(input("Masukan Angka Lain: "))
    print(x/y)
except ValueError:
    print("Invalid input. Tolong Enter Angka.")
except ZeroDivisionError:
    print("Tidak dapat dibagi dengan nol")