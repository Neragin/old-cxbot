import requests
url = f"https://api.mojang.com/user/profiles/<b51d393f51e348b5b24fb88c0552ef58>/names"
res = requests.get(url)
data = res.json()
print(data)