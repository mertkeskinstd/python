import re







"""""
cumle="mustafa kemal ataturk,turk asker,devlet adami ve turkiye cumhiriyetinin kurucusu."
patern="turk"
#print(re.search(patern,cumle))     # regular expression kutuphanesi icerisinde searh komutunu belirrli bir kelimeyi bir cumle icerisinde bulmak 
#icin kullanilir bize cumlenin tam neresinde oldugunu span ile tanimlar ve biz bunu ogrenebilirz yani match leşen kelimeyi secer


durum=re.search(patern,cumle)
print(durum.span())
print(dir(durum))                       #burda dir komutu ile re kutup icerisinde kullanabilegimiz ozellikleri gorebiliriz
print(durum.start())                    #mesela burada nerede match lesmeye basladigini bulabiliriz.
print(durum.end())


for eslesme in re.finditer(patern,cumle):        #burada findall kullanmamamızın sebebi direk str seklinde atamasi oyle yapssaydik hata alirdik
    print(eslesme.span(),eslesme.group())        # oyuzden obje seklinde tutarak finditer sekline yaptk
                                                #group burada ne uzerine arama yaptigımız gosteriyor

                                                #######  \d   #########   rakam  #######  base42  #########  base\d\d #########
                                                #######  \w   ########   karakter  #####   R2-D2  ######### \w\w\w\w\w ########
                                                #######  \s   ########    bosluk  ###### Ping Pong ######## Ping\sPong ########
                                                #######  \D   #######   rakam degil  #####  base  #########  \D\D\D\D #########
                                                #######  \W   #####   karakter degil  ###   R2D2  ######### \W\W\W\W ##########
                                                #######  \S   #####    bosluk degil ##### PingPong ### \S\S\S\S\S\S\S\S ###

ornek="sfdngjsn base42"                                                
patern="base\d\d"
print(re.search(patern,ornek))

                                                        #######  {5}   ########  adet  #######  aaaaa  #########    \w{5}     ##########
                                                        #######  {3,4} #######   veya  #######   abc  ##########   \w{3,4}     #########
                                                        #######  {2,}  ########  en az  ##### 198721321 ########    \d{2,}     #########
                                                        #######    *   ###  0 ya da fazla #######  x  ##########     \w*        ########
                                                        #######    +   ### 1 ya da fazla ######  Ahmet1  #######    \w+\d+     #########
                                                        #######    ?   #####  ya 1 ya hic ####### Mura #########     Murat?       ######       
cumle="selam benim telefon numaram:0553-1886734"
#patern=r"\d\d\d\d-\d\d\d\d\d\d\d"
#patern=r"\d{3,4}-\d{7}"                                #burada 5 karakterli veya daha fazla kelimeleri bulmak icin yapilan dongu...
#patern=r"\d+-\d+"
#patern=r"\s\w{5,}"
#patern=r"\d?"                                           #burada cumledekitum karakterlere sen sayimisin diye sorucak cunku ? isareti 1 yada 0 dir
patern=r"\d+"     
                                                            #bu durumda sayii bulana kadar yazdiricak yada yzdirmicak ? yerine + kullnsaydik ssadece sayilarin oldugu yeri gostercekti
for eslesme in re.finditer(patern,cumle):               
    print(eslesme.group(),eslesme.span())


### GSM Operatörleri:
# 54...         -> Vodafone
# 501,505,506   -> AVEA
# 53...         -> Turkcell

def gsm_op_bul(tel_no):
    patern=r"(\d{3})-(\d+)"
    eslesme=re.search(patern,tel_no)
    gsm=eslesme.group(1)
    print(gsm)
    if gsm.startswith("54"):
        return "vodofone sun sg"
    elif gsm.startswith("501") or gsm.startswith("501")or gsm.startswith("506"):
        return "aveasin"
    else:
        return " turkcell"
    

cumle="rwjgkwmsdmf:501-32542343"
print(gsm_op_bul(cumle)
"""         
#######    |   ########  veya  #######  slm  #########    selam|slm   ##########
#######    ^    ####### baslar  #######  Ahmet  ##########   ^\w+      #########
#######    $   ########  biter   ##### base42   ########     \d$       #########
#######    .   ######  herhangi  #####  abcdef  ########      .*       #########
#######    \   ########  esc     #####  (not)   ########   \(\w{3}\)   #########
#  ")" isaretinin bir anlami oldugu icin basina backslash koyarak anlamsizlistriyor
#! ve ? isretinen 2 veya 2 den fazla var ise ve cumlenin sonunda ise"$"
#^ cumlenin basinda ise 
# K veya k durumunda basliyorsa ikisinide dahil etmesi icin gerekn syntax




def mesaj_hissi_bul(mesaj):
    hisler = []

    pozitif_patern = r"(merhaba|selam|ask|sevgi|dost|kardes)"
    negatif_patern = r"(lan|aptal|abv|yeter|birak)"
    heyecanli_patern = r"(!|\?{2,}$)"
    sakin_patern = r"^(tabi+|hayhay)"
    emin_patern = r"(kesin|tabi|elbet)"
    kararsiz_patern = r"(belki|sanirim)"

    if re.search(pozitif_patern, mesaj):
        hisler.append("pozitif")
    if re.search(negatif_patern, mesaj):
        hisler.append("negatif")
    if re.search(heyecanli_patern, mesaj):
        hisler.append("heyecanli")
    if re.search(sakin_patern, mesaj):
        hisler.append("sakin")
    if re.search(emin_patern, mesaj):
        hisler.append("emin")
    if re.search(kararsiz_patern, mesaj):
        hisler.append("kararsiz")

    return hisler

cumle1 = "naber abi?  :)"
cumle2 = "tabi ki buyrun"
cumle3 = "sacmaamayi birak artik!"
cumle4 = "belki yarindan da yakin..."
cumle5 = "elbet bir gun bulusacaagiz"

cumleler = [cumle1, cumle2, cumle3, cumle4, cumle5]

for cumle in cumleler:
    print(cumle, "\t", mesaj_hissi_bul(cumle))
