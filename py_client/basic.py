import requests


endpoints = "https://httpbin.org/"
endpoints = "https://gulrez.com/"

content = requests.get(endpoints)
print(content)

