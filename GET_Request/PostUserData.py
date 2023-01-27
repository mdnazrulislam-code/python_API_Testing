import requests
import json
import jsonpath

# API Url
url = "https://reqres.in/api/users"

# Read input JSON file

file = open("G:\\API Testing\\GET_Request\\User.json", 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with Json Input Body
response = requests.post(url,request_json)

# Vlidting response code
assert  response.status_code == 201

# Fecth Headers from the response

print(response.headers.get('Content-Length'))

# Parse respnse into a json format

response_json  = json.loads(response.text)

# Pick id using json path

id = jsonpath.jsonpath(response_json,'id')

print(id[0])