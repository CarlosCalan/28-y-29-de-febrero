# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:58:29 2020

@author: CEC
"""

import urllib.parse
import requests 
main_api= "https://www.mapquestapi.com/directions/v2/route?"
while True:
    orig=input("Starting location: ")
    dest=input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: "+(url))

key="jIIWd6QKzYsvciIbRkWza7HIk0atf9hB"
json_data=requests.get(url).json()
print(json_data)

json_data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]

if json_status==0:
    print("API Status: "+ str(json_status) + "= A succesful route call.\n")