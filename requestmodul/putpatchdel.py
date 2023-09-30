import requests
import json



url=f"https://jsonplaceholder.typicode.com/todos/1"
response=requests.get(url,params=None)

print(response.json())

#PUT

payload={
    "userId": 1,
    "title": "putput",
    "completed": False
}
res=requests.put(url,data=payload)
print(res.json())



payload1={
    
    "title": "patchpatch",
}
res1=requests.patch(url,data=payload1)
print(res1.json())

#DELETE
delete_response = requests.delete(url)
print(delete_response.json())
print(delete_response.status_code)