import requests

## GET ##
resp=requests.get("https://reqres.in/api/users?page=2")
assert resp.status_code==220, "code didnt match"