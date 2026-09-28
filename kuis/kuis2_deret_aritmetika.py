print ("DERET ARITMETIKA")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n:"))

while n < 0:
    print("n harus bilangan bulat ppositif")
    n = int(input("Banyak suku n:"))


for i in range (n):
    total = 0
    suku = a + i * d
    total += suku
    print (f"Suku suku ke {i + 1}: {suku:.2f}")
print(f"Jumlah = {total:.2f}")

    