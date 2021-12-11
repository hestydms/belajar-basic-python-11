# Soal no 3
# Buatlah sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak. Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70. 
nilai_teori = float(input("Masukan nilai teori: "))
nilai_praktek = float(input("Masukan nilai praktek: "))

if nilai_teori >= 70 and nilai_praktek >= 70 :
    print("Selamat, Anda lulus!")
elif nilai_teori >= 70 and nilai_praktek < 70 :
    print("Anda harus mengulang ujian praktek.")
elif nilai_teori < 70 and nilai_praktek >= 70 :
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")