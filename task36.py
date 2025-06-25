sozlar = input("So‘zlar ro‘yxatini kiriting (bo'shliq bilan): ").split()
eng_uzun = max(sozlar, key=len)
print("Eng uzun so‘z:", eng_uzun)
