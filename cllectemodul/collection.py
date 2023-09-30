from collections import Counter
import random




list1=random.sample(range(10),k=4)

list2=random.sample(range(10),k=4)
list3=random.sample(range(10),k=4)
list4=random.sample(range(10),k=4)

liste_listesi=[list1,list2,list3,list4]
list_toplam=list1+list2+list3+list4
print(liste_listesi)
print(list_toplam)

for index,liste in enumerate(liste_listesi):
    print(f"{index}. liste \t {liste}")

print(Counter(list_toplam))                     #burada counter objesi list_toplan icerisinde hangi sayidan kac tane oldugunu bize soyler yani sayac mantigi ile calisir
print(Counter("djfgjnsjdfjnjjnfsnfdkn"))

sarki="""Yine bana gel
Yana yana yine beni sev
Yine bana gel
Yana yana yine beni sev"""
print(Counter(sarki.split()))                   #burada counter icerisnde split komutu kullanmasaydik harfler uzerinden kac tane olduguu sayacakti...
                                                #split komutu ile bundan kurtulmus olduk ayni kelimelerin kac tane oldugunu bulmus olduk...
print(Counter(sarki.lower().split()))             #burada once tum harfleri kucuge dondurduk sonra dondurdugumuz objeleri kelimelere bolduk
print(Counter(sarki.lower().split()).most_common(1))       #burada most common komutu en cok tekrar edeni veya en cok tekrar eden ikinci kelimeyi goste1rir

