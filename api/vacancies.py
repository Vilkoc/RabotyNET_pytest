import requests

url = "http://localhost:8080/RabotyNET/vacancies"

response = requests.request("GET", url)

print(response.text)