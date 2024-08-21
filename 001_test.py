import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100.")
    
    while True:

        tebakan = int(input("Masukkan tebakan Anda: "))
        percobaan += 1
        

        if tebakan < angka_rahasia:
            print("Terlalu rendah! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
            break

tebak_angka()