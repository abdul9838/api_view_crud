import requests
import json
URL = 'http://127.0.0.1:8000/studentapi/'
def get_data():
    headers  = {'content-type': 'application/json'}
    r = requests.get(url = URL, headers=headers)
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print("Error:", r.status_code)
# get_data()


def post_data():
    data = {
        'name': 'Abujar', 
        'roll': 105, 
        'city': 'Gorakh'
    }
    headers  = {'content-type': 'application/json'}
    data = json.dumps(data)
    r= requests.post(url=URL,headers=headers,data=data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
        'id':4,
        'city':'Kharjarwa'
    }
    headers  = {'content-type': 'application/json'}
    data = json.dumps(data)
    r= requests.put(url=URL,headers=headers,data=data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {'id': 1}
    json_data = json.dumps(data)
    headers  = {'content-type': 'application/json'}
    r = requests.delete(url=URL,headers=headers,data = json_data)
    print(r.status_code)
    if r.status_code <= 300:  
        print("Data deleted successfully")
    else:
        print("Failed to delete data")

delete_data()

