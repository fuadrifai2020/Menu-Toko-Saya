from re import X
from prettytable import PrettyTable
tab = PrettyTable(['Menu', 'Jumlah'])
es_teh = 0
gurami = 0
print("Toko Saya")
while True:
      print("\nPilih Menu :")
      print("1. Es Teh -> Rp.7000")
      print("2. Gurami -> Rp.15000")
      print("3. Keluar")
      print("Beli 2 atau Lebih Dapat Diskon 20%")
      opsi = int(input("Pilih Menunya :"))
      if opsi == 1:
            jumlah = int(input("Jumlah :"))
            uang_kamu = int(input("Uang Kamu :"))
            harga = 7000
            diskon = 20/100
            total = jumlah*harga
            if total <= uang_kamu:
                  if jumlah == 1:
                        print("Kamu Akan Membeli Es Teh berjumlah :",jumlah,"dengan harga : ",harga)
                  elif jumlah == 2: 
                        print("Kamu Membeli Es Teh berjumlah :",jumlah,"dengan harga :",harga*jumlah*80/100,"Dan mendapatkan Diskon sebesar 20%")
                        print("Total Diskon :",harga*jumlah*diskon)
                  else :
                        x = uang_kamu - (harga*jumlah*20/100)
                        print("Kamu Akan Membeli Es Teh berjumlah : ",jumlah," dengan harga : ",harga*jumlah*80/100, " dan kembalian", x)
                  es_teh += jumlah
            else:
                  print("Uang anda kurang")

      elif opsi == 2:
            jumlah = int(input("Jumlah :"))
            uang_kamu = int(input("Uang Kamu :"))
            harga = 15000
            diskon = 20/100
            total = jumlah*harga
            if total <= uang_kamu:
                  if jumlah == 1:
                        print("Kamu Akan Membeli Gurami berjumlah :",jumlah,"dengan harga : ",harga)
                  elif jumlah == 2: 
                        print("Kamu Membeli Gurami berjumlah :",jumlah,"dengan harga :",harga*jumlah*80/100,"Dan mendapatkan Diskon sebesar 20%")
                        print("Total Diskon :",harga*jumlah*diskon)
                  else : 
                        x = uang_kamu - (harga*jumlah*20/100)
                        print("Kamu Akan Membeli Gurami berjumlah :",jumlah,"dengan harga : ",harga*jumlah*80/100, " dan kembalian", x)
                  gurami += jumlah
            else:
                  print("Uang anda kurang")

      elif opsi == 3:
            tab.add_row(['Es Teh', es_teh])
            tab.add_row(['Gurami', gurami])
            break
      
      else:
            print("Opsi anda salah\n")

print("\nDaftar pembelian hari ini")
print(tab)
a = input("\nTekan ENTER untuk keluar")
