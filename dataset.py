import http.client
import json


RANDOM_DATA = True #на время выполнения дз можно поставить False,
                    #по умолчанию - True


conn = http.client.HTTPSConnection("pumpskill.ru")
conn.request("GET", f"/cases/api/python-basic/users-and-friends/{'?r=0' if not RANDOM_DATA else ''}")
response = conn.getresponse()
data = json.loads(response.read().decode("utf-8"))

users = data["users"]
countries = data["countries"]

