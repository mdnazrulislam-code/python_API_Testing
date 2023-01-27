import requests

url = f"https://reqres.in/api/users/"

user_id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for users in user_id_list:
    response = requests.delete(url+str(users))
    # Feth response code
    print(response.status_code)
    assert response.status_code == 204
