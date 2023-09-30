import requests
import json


#GET.....
#user_inp=input("enter id:")
url=f"https://jsonplaceholder.typicode.com/todos"

response=requests.get(url,params=None)

#print(response.json())


#POST....


payload={
    "userId":2,
    "title":"uewhfuhwehfj",
    "completed": False
}

header={"Content-Type":"application/json"}
res=requests.post(url,data=json.dumps(payload),headers=header)
print(res.json())

