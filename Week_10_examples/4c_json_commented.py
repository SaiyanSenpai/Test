# https://pynative.com/python-json-load-and-loads-to-parse-json/
import json

print("Started Reading JSON file")
with open("data/janedoe.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file) #store as dict

    print("Decoded JSON Data From File")
    for key, value in developer.items(): #loop thru dict
        print(key, ":", value)
    print("Done reading json file")
