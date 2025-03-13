import requests

class ApiClient:
    BASE_URL = "https://reqres.in/api/users"
    
    @staticmethod
    def create_user(payload):
        response = requests.post(ApiClient.BASE_URL, json=payload)
        return response
    
