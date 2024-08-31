import os
import requests
import configparser
from dataclasses import dataclass

DEFAULT_PATH = "Api_handling\src"

@dataclass
class config_default_path:
    api_config_path = os.path.join(DEFAULT_PATH,"config.ini")
class ApiHandler:
    def __init__(self):
        self.path =config_default_path()
        self.config = configparser.ConfigParser()
        self.config.read(self.path.api_config_path) 
            
    def fetch_random_user_freeapi(self):
        url = self.config['ENDPOINTS']['random_user_endpoint']
        
        response = requests.get(url)
        data = response.json()
        
        if data["success"] and "data" in data:
            user_data = data['data']
            username = user_data["login"]["username"]
            country = user_data['location']['country']
            return username, country
        else:
            raise Exception("Failed to fetch user data")
    
    def get_random_user(self):
        try :
            username, country = self.fetch_random_user_freeapi()
            print(f"Username:{username} \nCountry:{country}")
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    api_handler = ApiHandler()
    api_handler.get_random_user()   

        
    