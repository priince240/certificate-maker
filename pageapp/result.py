import requests
import json
URL = "http://127.0.0.1:8000/listapi/"
headers = {
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwNjM0NzQ3LCJpYXQiOjE2OTA2MzQxMjEsImp0aSI6ImRmOGVjMmU5MjdkYTQ0M2M5ZjdmMzRhMjk2OTA1MTcwIiwidXNlcl9pZCI6MX0.RCk8GCuCn6XFYDfdgwEwcti0Kimyss0jLUR3kIsreWk'
}

response = requests.get(URL, headers=headers)
data = response.json()
print(data)
    