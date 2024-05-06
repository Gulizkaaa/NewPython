
# from pprint import pprint
# import requests, os

# api_key = os.getenv("DIGITALOCEAN_API_KEY")
# do_droplet_url = "https://api.digitalocean.com/v2/droplets"

# headers = {"Content-type": "application/json", "Authorization": f"Bearer {api_key}"}
# # req = {
# #     "name": "testserver",
# #     "region": "nyc3",
# #     "size": "s-1vcpu-1gb",
# #     "image": "centos-stream-8-x64",
# #     "ssh_keys": ["39737562"]
# # }

# # response = requests.post(url=do_droplet_url, json=req, headers=headers)

# # print(response.json())


# def getDropletIP(dropletID):
#     response = requests.get(url=do_droplet_url, headers=headers)
#     response_json = response.json()
#     # id_droplet = 401805528

#     for i in response_json["droplets"]:
#         if i["id"] == dropletID:
#             for j in (i["networks"]["v4"]):
#                 if j["type"] == "public":
#                     return j["ip_address"]
            
# print(getDropletIP(401805528))

# # response = requests.get(url=do_droplet_url, headers=headers)
# # response_json = response.json()

# # pprint(response_json)

# def getSSHId(ssh_name="")
#     pass
#     #do_droplet_url = "https://api.digitalocean.com/v2/accounts/keys"

#     # will be different ssh accounts/keys 
#     # if name == id get the id 


from pprint import pprint
import requests, os, inquirer


api_key = os.getenv("DIGITALOCEAN_API_KEY")
base_url = "https://api.digitalocean.com/v2/"


headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}


def getImage():
    image_url = f"{base_url}images"

    response = requests.get(url=image_url, headers=headers)
    response_json = response.json()["images"]

    pprint(response_json)  ## Get the desction of every image and put in in a list

getImage()