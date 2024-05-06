
from pprint import pprint #importing modules 
import requests #is the library that will work with APIs.

headers = {"Content-Type": "application/json"}  #to specify api to give a json format
github_url = "https://www.githubstatus.com/api/v2/status.json"

response = requests.get(url=github_url, headers=headers)
response_json = response.json()
# print(response)
# print(response.json) #to get the contect 
#pprint(response_json)


print("WebSite Name:", response_json["page"]["name"])
print("Time Zone:", response_json["page"]["time_zone"])
print("Updated At:", response_json["page"]["updated_at"])
print("Status:", response_json["status"]["description"])