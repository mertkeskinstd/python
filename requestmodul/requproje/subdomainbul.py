import requests

def bul(url):
    
    try:
        print(requests.get(url))
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f"it'snt found:\t{url}")
        pass




with open("C:\\Users\\tahak\\Desktop\\piton\\modul_paket\\requestmodul\\requproje\\sumdomainlist.txt","r") as subdomainlist:

        for word in subdomainlist:
            word=word.strip()
        
            url=f"https://{word}.google.com.tr"
            res=bul(url)
            if res:
                print("found it..." +  url)    
            