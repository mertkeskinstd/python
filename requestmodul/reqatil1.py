import requests as r

#url="https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"


def crypto():
    response=r.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code==200:
        return response.json()

crypto_response = crypto()
user_input = input("Enter your favorite crypto: ")
for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])



