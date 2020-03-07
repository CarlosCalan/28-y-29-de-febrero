# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:04:22 2020

@author: CEC
"""
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "jIIWd6QKzYsvciIbRkWza7HIk0atf9hB"
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    jsonstatus = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")