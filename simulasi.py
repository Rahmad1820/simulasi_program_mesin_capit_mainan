import random
import time

class MesinCapitMainan:
    def __init__(self):
        self.mainan = ["Boneka Beruang", "Mobil Mini", "Robot Kecil", "Topi Pesta", "Gelang Warna-warni","hp iphone"]

    def capit_mainan(self):
        print("Mesin Capit Mainan sedang berjalan...")
        time.sleep(2)
        hasil_capit = random.choice(self.mainan)
        print(f"Selamat! Anda mendapatkan: {hasil_capit}\n")

def main():
    mesin_capit = MesinCapitMainan()

    while True:
        input("Tekan Enter untuk mencapit mainan...")
        mesin_capit.capit_mainan()

        pilihan = input("Apakah Anda ingin mencapit lagi? (y/n): ")
        if pilihan.lower() != 'y':
            print("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    main()

