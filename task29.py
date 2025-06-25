sonlar = []
for i in range(10):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

noyob_sonlar = [x for x in sonlar if sonlar.count(x) == 1]
print("Takrorlanmaydigan sonlar:", noyob_sonlar)
