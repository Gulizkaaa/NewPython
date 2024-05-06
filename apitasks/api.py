
from datetime import datetime
from pprint import pprint
import requests

def time_converter(time):
    timestamp_obj = datetime.fromisoformat(date.replace("Z", "+00:00"))
    formatted_timestamp = timestamp_obj.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_timestamp

url = "https://slack-status.com/api/v2.0.0/current"
head = {"Content-type": "application/json"}

response = requests.get(url, headers=head)
response_json = response.json()

print("Astive incidents:", len(response_json["active_incidents"]))
print("Created at:", time_converter(response_json["date_created"]))
print("Updated at:", time_converter(response_json["date_updated"]))
print("Status:", response_json["status"])



#pprint(response_json)

#json - is kind like a dictionary 
#yum 