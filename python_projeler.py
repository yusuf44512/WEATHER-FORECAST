
import requests
import json


origin_url= "http://api.openweathermap.org/data/2.5/weather?q=Kocaeli,tr&APPID=ad6abd393eea444dfd268a76fe62606b"
response = requests.get(origin_url)
jsonResponse = json.loads(response.text)

print("Sıcaklık:" + str(jsonResponse["main"]["temp"]-273)+"'C")
print("Nem Oranı:"+ str(jsonResponse["main"]["humidity"])+"%")
print("Basınç:"+str(jsonResponse["main"]["pressure"])+"paskal.")
print("Rüzgar Hızı:"+str(jsonResponse["wind"]["speed"])+"m/s")






