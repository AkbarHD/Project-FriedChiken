print("        GEROBAK FRIED CHICKEN     ")
print("----------------------------------")
print(" Kode     jenisPotong     Harga   ")
print("----------------------------------")
print(" D         Dada           Rp 2500 ")
print(" P         Paha           Rp 2000 ")
print(" S         Sayap          Rp 1500 ")

banyak_jenis = int(input("banyak jenis : "))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []

i=0
while i < banyak_jenis:
    print("jenis ke-", i+1)
    kode_potong.append(input("kode potong [D/P/S]"))
    banyak_potong.append(int(input("banyak potong : ")))

    if kode_potong[i]=="D" or kode_potong[i]=="d":
        jenis_potong.append("dada")
        harga.append("2500")
        jumlah.append(banyak_potong[i]*int("2500"))
    elif kode_potong[i]=="P" or kode_potong[i]=="p":
        jenis_potong.append("paha")
        harga.append("2000")
        jumlah.append(banyak_potong[i]*int("2000"))
    elif kode_potong[i]=="S" or kode_potong[i]=="s":
        jenis_potong.append("sayap")
        harga.append("1500")
        jumlah.append(banyak_potong[i]*int("1500"))
    else:
        jenis_potong.append("kode salah")
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))
    i = i+1

print("           GEROBAK FRIED CHICKEN                ")
print("------------------------------------------------")
print(" No     Jenis     Harga     Banyak     Jumlah   ")
print("        Potong    Satuan    Beli       Harga    ")
print("------------------------------------------------")

jumlah_bayar = 0
a = 0
while a < banyak_jenis:
    jumlah_bayar = jumlah_bayar+jumlah[a]
    print("%i    %s     %s        %s          %i" % (a+i, jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
    a = a+1

print("------------------------------------------------")
pajak = jumlah_bayar*0.1
total_bayar = jumlah_bayar+pajak

print("jumlah bayar :  ", jumlah_bayar)
ubay = int(input("masukan uang bayar anda : "))
kembalian = ubay - jumlah_bayar
print("uang kembali : ",kembalian)
print("========================================================================")
print("+_+_+_+_+_+_+_+_ TERIMA KASIH DAN SAMPAI JUMPA +_+_+_+_+_+_+_+_+_+_+_+_+")
print("========================================================================")







