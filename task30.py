sozlar = []
for i in range(5):
    soz = input(f"{i+1}-so'zni kiriting: ")
    sozlar.append(soz)

palindromlar = [s for s in sozlar if s == s[::-1]]
print("Palindrom so‘zlar:", palindromlar)
