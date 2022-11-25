'''
We have the dump() method for writing data to files.
We have the dumps() method (pronounced “dump-s”) for conversion to strings.
'''
import json

data = {
    'Microsoft': {
        'symbol': "msft",
        "ceo": "Satya Nadella",
        "market_cap": 2500000000000,
        "Quarterly Estimate ": None,
        "Publically-Traded": True
    }
}

with open("data_msft.json", "w") as write_file:
    json.dump(data, write_file)
#(what we will write,  where we will write it).

# Lets copy it to a string- not writing to a file
json_string = json.dumps(data, indent=10)
print(json_string)
print(type(json_string))

# https://realpython.com/python-json/
