import requests
import json
import jsonpath


# API URL
url = "https://reqres.in/api/users?page=2"
# Send request
response = requests.get(url)
# Parse response to Json format

json_response = json.loads(response.text)

# Fetch value using json path

pages = jsonpath.jsonpath(json_response,'data')

for elem in pages[0]:
    for key, value in elem.items():
        if key == 'first_name':
            print("First Name is: ", value)

        elif key == 'last_name':
            print("Last Name is: ",value)


