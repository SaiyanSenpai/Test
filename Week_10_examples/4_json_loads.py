#JSON Load - s creates a dict from a JSON string
import json
json_string = """
{
    "beatles": {
        "Paul": "bass",
        "John": "guitar",
        "George": "lead guitar",
        "Ringo":"drums",
        "albums": ["Rubber Soul","Abbey Road", "Let it Be"],
        "concert schedule": null
    }
}
"""
#print(type(json_string))
data = json.loads(json_string)
print(type(data))
print(data)
# Note the differences between the string and the JSON data
