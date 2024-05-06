
from pprint import pprint 
import requests

headers = {"Content_Type": "applications/json"}
digitalocean_url = "https://status.digitalocean.com/api/v2/summary.json"

response = requests.get(url=digitalocean_url, headers = headers)
response_json = response.json()

#pprint(response_json)

print("WebSite Name:", response_json["page"]["name"])
print("Time Zone:", response_json["page"]["time_zone"])
print("Updated At:", response_json["page"]["updated_at"])
print("WebPage URL is:", response_json["page"]["url"])
print("Status:", response_json["status"]["description"])
