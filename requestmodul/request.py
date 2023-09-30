import requests
from collections import Counter

bolgeler_url="https://data.police.uk/api/forces"

response=requests.get(bolgeler_url)

#print(response.status_code)
#print(response.url)
response.text
print(response.json())  

"""""
suc_kategori_url="https://data.police.uk/api/crime-categories"
payload={"date":"2023-08"}
response=requests.get(suc_kategori_url, params=payload)

print(response.status_code)
print(response.url)
print(response.json())

suc_url="https://data.police.uk/api/crimes-no-location"
payload={
    "category":"all-crime",
    "force":"city-of-london",
    "date":"2023-07"
}
response=requests.get(suc_url, params=payload)
data=response.json()
print(data)
"""
"""""
class SucRaporu():
    def __init__(self,bolge,tarih,suc_tipi="all-crime"):
        self.bolge=bolge
        self.tarih=tarih
        self.suc_tipi=suc_tipi
        self.suclar=self.suclari_bul()
    
    def suclari_bul(self):
        suc_url="https://data.police.uk/api/crimes-no-location"
        payload={
            "category":self.suc_tipi,
            "force":self.bolge,
            "date":self.tarih
        }
        response=requests.get(suc_url, params=payload)
        
        if response.status_code==200:
            data=response.json()
            return data
            
        else:
            return None
    def suclari_raporla(self):
        suclar_listesi=[]
        if self.suclar is not None:
            for suc in self.suclar:
                suclar_listesi.append(suc['category'])
                
            return Counter(suclar_listesi)

sr=SucRaporu("city-of-london","2023-06")

print(sr.suclari_raporla())

#sr.suclar
        
"""
