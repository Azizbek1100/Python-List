list1 = input("1-ro‘yxat elementlarini kiriting: ").split()
list2 = input("2-ro‘yxat elementlarini kiriting: ").split()

if len(list1) == len(list2):
    for i in range(len(list1)):
        list1[i], list2[i] = list2[i], list1[i]
    print("Almashtirilgan list1:", list1)
    print("Almashtirilgan list2:", list2)
else:
    print("Ro‘yxatlar uzunligi teng emas!")
