# python loop
# for loop: understanding how for loop works in py: range
# why loop: continue, break, nested loop

# buah = ["apel", "jeruk", "semangka", "nanas"]
# # print(buah)

# for x in buah:
#     print(x)


# range(start, stop, step)
# x = range(6)
# for n in x: #prints out 0,1,2,3,4,5
#     print(n)

# for x in range(5): # stop, default start = 0, default step = 1
#     print(x)

# for x in range(16,19): # start, stop
#     print(x)


# for x in range(3,20,10): # start, stop, step
#     print(x)

# for x in range(1,-5,-1): # start, stop, step
#     print(x)

# for x in range (10):
#     print("Hallo saya maria")

# for x in range(1.0,-5.0,-1.0): # start, stop, step # can not be done, bcs not an integer
#     print(x)

# for x in range(0,10,1):
#     print("a")

# nama = []
# nama.append(input("Masukan nama Anda: "))


# nama = []
# jumlah = int (input("Masukkan jumlah yang diinginnkan: "))

# for x in range(jumlah):
#     nama.append(input("Masukkan nama ke {}:".format(x+1)))

# for x in nama:
#     print(x)

##
# nama = []
# jumlah = int(input("Masukkan jumlah yang diinginkan: "))

# for x in range(jumlah):
#     nama.append(input("Masukkan nama ke {}:".format(x)))

# # for x in nama:
# #     print(x)

# for x in range(jumlah+1):
#     print(nama[x])


# buah = ["apel", "jeruk", "semangka", "nanas"]
# print(buah[:2])

## increment nama

# nama = []
# jumlah = int(input("Masukkan jumlah yang diinginkan: "))

# for x in range(jumlah):
#     nama.append(input("Masukkan nama ke {}:".format(x+1)))

# # for x in nama:
# #     print(x)

# for x in range(1, jumlah+1):
#     print(nama[0:x])

## quiz

# nama = []
# jumlah = int (input("Masukkan jumlah yang diinginnkan: "))

# for x in range(jumlah):
#     nama.append(input("Masukkan nama ke {}:".format(x+1)))

# for x in nama:
#     print(x)


## while loop: we can execute

# # kondisi while
# i = 1 # start
# while i < 6: # stop
#     print(i)
#     i+=1 # step

# kondisi for yg sama spt diatas
# for x in range(1,7):
#     print(x)


# infinite loop
# while True:
#     print("I Love You")

# i = 1 # start
# while i < 6: # stop
#     print(i)
#     i+=1.1 # step

# break

# case 1
# for x in range(7):
#     if x == 4:
#         break
#     print(x)

# case 2
# for x in range(7):
#     print(x)
#     if x == 4:
#         break

# case 3
# for x in range(7):
    # if x == 4:
    #     print(x)
    #     break


# continue # skip the specific condition
# for x in range(7):
#     if x == 4:
#         continue
#     print(x)


# nested loop

# for i in range(3):
#     for j in range(2):
#         print("ini baris ke {} dan kolom ke {}".format(i,j))


# for i in range(2):
#     for j in range(3):
#         print("i={},j={}".format(i,j), end=" ")
#     print()

# for x in range(3):
#     for y in range(2):
#         print(x,y)

# for x in range(3):
#     for y in range(2):
#         print(x,y)
#     print("###")

# for x in range(3):
#     for y in range(3):
#         print("baris ke {}, kolom ke {}".format(x,y), end=" ")
#     print()


# from string import ascii_lowercase
# for i in range(1,123):
#     print(chr(i))


x = [1,2,3,4,5]
y = [2,4,3,5,6]
z = 0

for i in x:
    for j in y:
        if i == j:
            z=z+1
print(z)