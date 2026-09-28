print ("DERET ARITMETIKA")

#input data
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n:"))

#validasi nilai
while n < 0:
    print("n harus bilangan bulat ppositif")
    n = int(input("Banyak suku n:"))

#operasi deret aritmetika
total = 0
for i in range (n):
    suku = a + i * d
    total += suku
    print (f"Suku suku ke {i + 1}: {suku:.2f}")
print(f"Jumlah = {total:.2f}")

    