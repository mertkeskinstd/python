from collections.abc import Callable, Iterable, Mapping
import time
import threading
from typing import Any
import requests
import asyncio
import aiohttp

"""""
def get_data(urls):
    st = time.time()
    json_array = []

    for url in urls:
        json_array.append(requests.get(url).json())
    et = time.time()
    response = et-st
    print(f"sonuc:{response}")

    return json_array


urls = ["https://postman-echo.com/delay/3"] * 10

get_data(urls)



class theradingofdata(threading.Thread):
    json_array = []

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        return self.json_array


def get_data_threading(urls):
    st = time.time()
    therds = []
    for url in urls:
        t = theradingofdata(url)
        t.start()
        therds.append(t)
    for t in therds:
        t.join()
        print(t)
    et = time.time()
    response = et-st
    print(f"sonuc:{response}")


urls = ["https://postman-echo.com/delay/3"] * 10
get_data_threading(urls)


#verimsizz async....
async def get_data_wrapper(urls):
    
    st = time.time()
    json_array=[]
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                json_array.append(await resp.json())     
    et = time.time()
    response = et-st
    print(f"sonuc:{response}")
    return json_array

urls = ["https://postman-echo.com/delay/3"] * 10
asyncio.run(get_data_wrapper(urls))
#verimli async
"""


async def get_data(url, session, json_array):
    async with session.get(url) as resp:
        json_array.append(await resp.json())


async def getdata_concurrently(urls):
        st = time.time()
        json_array = []
        
        async with aiohttp.ClientSession() as session:
            task = []
            for url in urls:
                task.append(asyncio.ensure_future(get_data(url, session, json_array)))
            await asyncio.gather(*task)
        et = time.time()
        response = et-st
        print(f"sonuc:{response}")
        return json_array

urls = ["https://postman-echo.com/delay/3"] * 10
asyncio.run(getdata_concurrently(urls))
