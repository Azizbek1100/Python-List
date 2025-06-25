sozlar = input("So‘zlar ro‘yxatini kiriting (bo'shliq bilan): ").split()

qisqa = []
orta = []
uzun = []

for s in sozlar:
    if len(s) <= 3:
        qisqa.append(s)
    elif 4 <= len(s) <= 6:
        orta.append(s)
    else:
        uzun.append(s)

print("<=3 harfli:", qisqa)
print("4-6 harfli:", orta)
print(">6 harfli:", uzun)
