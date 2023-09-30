import requests

grafik_url="https://image-charts.com/chart"
#https://image-charts.com/chart?chs=700x190&chd=t:60,40&cht=p3&chl=Hello%7CWorld&chan&chf=ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1
payload={
    "chs":"700x190",
    "chd":"t:60,40",
    "cht":"p3",
    "chl":"Hello|World",
    "chan":None,
    "chf":"ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1"
}
response=requests.post(grafik_url,data=payload)
print(response.status_code)
print(response.content)         #bit tipinde oldugunu basimdaki b harfini aliyoruz bunu simdi gorsellestircez...
"""""
from PIL import Image
from io import BytesIO


image=Image.open(BytesIO(response.content))
image.show()
"""
"""""
#radar chart
from PIL import Image
from io import BytesIO
"""""
"""""
grafik_url="https://image-charts.com/chart"

payload={
    "chco":"3092de",
    "chd":"t:81,65,50,67,59,81",
    "chdl":"first",
    "chl":"hiz|sut|pas|fizik|top_surus|defans",
    "chdlp":"b",
    "chs":"480x480",
    "cht":"r",
    "chtt":"Futbolcu Özellikleri"
}
response=requests.post(grafik_url,data=payload)
image=Image.open(BytesIO(response.content) )
image.show()
"""""
"""
class Futbolcu():
    def __init__(self,isim,hiz,sut,pas,top_surme,defans,fizik):
        self.isim=isim
        self.hiz=hiz
        self.sut=sut
        self.pas=pas
        self.top_surme=top_surme
        self.defans=defans
        self.fizik=fizik
    def yetenek_hazirla(self):
        return ",".join([
        str(self.hiz),
        str(self.sut),
        str(self.pas),
        str(self.top_surme),
        str(self.defans),
        str(self.fizik),
        str(self.hiz)
            
        ]
            
        )
    def yetenek_gorsellestirme(self):
        grafik_url="https://image-charts.com/chart"
        payload={
    "chco":"3092de",
    "chd":"t:"+self.yetenek_hazirla(),
    "chdl":self.isim,
    "chl":"hiz|sut|pas|fizik|top_surus|defans",
    "chdlp":"b",
    "chs":"480x480",
    "cht":"r",
    "chtt":"Futbolcu Özellikleri",
    "chxl":"0:|0|20|40|60|80|100",
    "chxt":"x",
    "chxr":"0,0.0,100.0",
    "chm":"B,AAAAAABB,0,0,0"
}
        response=requests.post(grafik_url,data=payload)
        image=Image.open(BytesIO(response.content) )
        image.show()
    def yetenek_kiyasla(self,hedef_futbolcu):
        grafik_url="https://image-charts.com/chart"
        payload={
            "chco":"3092de,8654ef",
            "chd":"t:"+self.yetenek_hazirla()+ "|" + hedef_futbolcu.yetenek_hazirla(),
            "chdl":self.isim +"|" + hedef_futbolcu.isim,
            "chl":"hiz|sut|pas|fizik|top_surus|defans",
            "chdlp":"b",
            "chs":"480x480",
            "cht":"r",
            "chtt":"Futbolcu Özellikleri",
            "chxl":"0:|0|20|40|60|80|100",
            "chxt":"x",
            "chxr":"0,0.0,100.0",
            "chm":"B,AAAAAABB,0,0,0|B,09843243,1,1,2"
        }
        response=requests.post(grafik_url,data=payload)
        image=Image.open(BytesIO(response.content) )
        image.show()
        
    
ronaldo=Futbolcu("Ronaldo",81,92,78,85,34,75)
messi=Futbolcu("Messi",81,89,90,94,34,64)
messi.yetenek_kiyasla(ronaldo )
"""