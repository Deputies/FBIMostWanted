import requests
print("lol")
headers ={
"accept":"application/json",
}
r = requests.get("https://api.fbi.gov/wanted/v1/list",headers=headers)
print(r.txt)
