sozlar = input("So‘zlar ro‘yxatini kiriting (bo'shliq bilan): ").split()
uzun_sozlar = [s for s in sozlar if len(s) > 5]
print("5 harfdan uzun so‘zlar:", uzun_sozlar)
