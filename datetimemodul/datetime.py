import datetime
from datetime import date
from datetime import time
import time
"""""
bugun=date.today()
print(bugun)
dun=date(2023,9,8)
a=bugun-dun 
print(a.days)              #sadece arada ki gunu hesaplamasi icin days komutuu kulandik...
yarin=bugun + datetime.timedelta(days=1)
print(yarin)

print(date.isocalendar(bugun))      #burada komutta weekday yani hangi gunde oldugumuzu syleyen durum 1 den baslar ama 
print(date.weekday(bugun))          #buradaki gibi sordugumuz zaman 0 pazartesi durumuna gelmis olur


zaman=.time(21,15,5)
print(zaman)
print(zaman.hour)
print(zaman.minute)
print(zaman.second)
dt=datetime.datetime(2023,9,9,17,12,54)
print(dt)
"""
baslangic_zamani=time.time()                #1694269139.9826107 bu 60 bolundugunde saniyeyi bolerek gittigindede saati verir yani bu zamandir...
print(f"baslama zamani:\t {baslangic_zamani}")
time.sleep(5)
bitis_zamani=time.time()
print(f"bitis zamani:\t {bitis_zamani}")
print(f"calisma suresi:\t {bitis_zamani-baslangic_zamani}")
