import requests
import json
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# data_dictionary = json.loads(response)
# print(data_dictionary)

complete_detail = response.json()
list_users = []
for user_data in range(len(complete_detail)):
        list_users.append(complete_detail[user_data]["user"]["login"])

print(list_users)
