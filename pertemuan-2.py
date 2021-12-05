# user input
# nama = input("Masukkan nama Anda: ") #default tipe data input ialah string
# umur = int(input("Masukkan umur Anda: "))
# print (" umur saya adalah: "+ umur) # error karena int tidak bs ditambah dgn string
# print ("Nama saya adalah:"+nama)
# print (type(umur))


# menghitung luas persegi // using casting
# p = int(input("masukkan panjang: "))
# l = int(input("masukkan lebar: "))

# L = p*l
# print(L)

# string operation

# string formatting
# print("maka luas pp adalah {} cm persegi".format(L))
# print("maka luas pp nya ialah {} cm persegi".format(L))
# age = 36
# txt = "my name is ay, and i am a []."format

# 2 input
# p = int(input("masukkan panjang: "))
# l = int(input("masukkan lebar: "))

# L = p*l
# K = (p+l)*2

# print("maka luas pp nya ialah {} cm persegi, dan keliling pp ialah {}".format(L,K))


# x = "Indonesia"
# y = "AI"
# print(x+ " " +y)
# print(x+y)

# a = "Hallo, Dunia"
# print(a[2:8])
# print(len(a))
# print(a[0]+" "+a[2])

# merah
# warna = input("masukkan warna: ")
# print(warna[1])
# print(warna[-2:])

# quiz
# x = "Indonesia AI"
# print(x[2:4])
# print(len(x))

# x=str(123)
# print(x[2])

# booleans
# print(10>10)
# print(8>7)

# conditions
# a = 200
# b = 33
# if b < a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")


# nilai = int(input("masukkan nilai anda: "))
# kkm = 70

# if nilai < kkm:
#     print("anda harus mengulang")
# else:
#     print("selamat anda lulus")
#     print("anda akan wisuda")

# if nilai < kkm:
#     print("anda harus remedial")
# else:
#     print("selamat anda lulus")


# perbedaan if if dan if elif
# b = 200
# a = 33
# if b > a:
#     print("b is greater than a")
# if b >= a:
#     print("b is greater than or equal to a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")


# b = 200
# a = 33
# if b > a:
#     print("b is greater than a")
# elif b >= a:
#     print("b is greater than or equal to a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# list

# x = 7
# makanan = ["soto","mie ayam","sate"]
# print(x)
# print(type(makanan))
# print(len(makanan))
# print(makanan[0])

# y=[1,2,3,4,5]
# print(y[0]+y[1])

# makanan = ["soto","mie ayam","sate"]
# makanan.append("bakso")
# print(makanan)
# print(makanan[10])

# minuman = []
# harga = []

# minuman.append(input("masukkan nama minuman: "))
# minuman.append(input("masukkan nama minuman: "))
# minuman.append(input("masukkan nama minuman: "))

# harga.append(input("masukkan harga: "))
# harga.append(input("masukkan harga: "))
# harga.append(input("masukkan harga: "))

# print(minuman)
# print(harga)

# minuman = ["es teh","es jeruk","syrup"]
# print(minuman)
# minuman[0]=input("minuman pengganti: ")
# print(minuman)
# minuman.replace("es teh",input("minuman pengganti: "))
# print(minuman)


# hanya print bilangan genap
# angka = [1,2,3,4,5,6,7,8,9,10]
# for x in angka:
#     if x%2 == 0:
#         print(x)


# c = 3
# a = c
# b = c+1
# if b>a:
#     print("b is greater than a")
# elif c==b:
#     print("c is same like b")
# else:
#     print("other")

tinggi = int(input("masukkan tinggi badan anda: "))
berat = int(input("masukkan berat badan anda: "))
tinggi_normal = 160
berat_normal = 60

if tinggi >= tinggi_normal  & berat >= berat_normal:
    print("Anda sehat")
elif tinggi < tinggi_normal & berat >= berat_normal:
    print("Anda kurang tinggi")
elif tinggi >= tinggi_normal & berat < berat_normal:
    print("Anda kurang berat")
else:
    ("Anda kurang sehat")