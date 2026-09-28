n = int(input("Nilai 1-100:"))
while n < 0 or n > 100:
    print(f"Nilai tidak valid")
    n = int(input("Nilai 1-100:"))
print(f"Nilai diterima: {n}")