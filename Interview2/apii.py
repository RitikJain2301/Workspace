# fetch('https://dummyjson.com/products')
# .then(res => res.json())
# .then(console.log);

import requests

## GET
resp=requests.get("https://dummyjson.com/products")
print(resp.json())

## POST
