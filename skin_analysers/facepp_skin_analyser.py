import requests
import os
import json

from datetime import datetime
from utils.utils import Utils

class FacePPSkinAnalyser:    
    def __init__(self, photo_dir, photo_name, removed_attributes=[]):
        self.removed_attributes = removed_attributes
        self.json_dir = Utils.parse_json_dir_path('facepp_skin_features')
        self.photo_dir = photo_dir
        self.photo_name = photo_name
        self.source_image_path = os.path.join(self.photo_dir, self.photo_name)
        self.json_file_path = ""
        self.api_key = os.getenv('FACEPP_API_KEY')
        self.api_secret = os.getenv('FACEPP_API_SECRET')
        self.api_url = 'https://api-us.faceplusplus.com/facepp/v1/skinanalyze'
        self.response = None

    def analyse_skin(self):
        start_time = datetime.now()

        with open(self.source_image_path, 'rb') as source_image:
            source_image_bytes = source_image.read()
            print("Source:", self.source_image_path)
            
        try:
            self.response = self.send_request(source_image_bytes)
            print("Analyse complete.")
            self.save_into_json(self.response.json())
        except Exception as e:
            print('Error occurred:', e)
        end_time = datetime.now()
        print("Duration (s):", (end_time - start_time).total_seconds())
        
    def get_response(self):
        return self.response.json()
    
    def send_request(self, image_bytes):
        data = {
            "api_key": self.api_key,
            "api_secret": self.api_secret,
        }
        files = {'image_file': ('image.jpg', image_bytes)}

        response = requests.post(self.api_url, data=data, files=files)
        return response

    def save_into_json(self, data):
        with open(self.json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Saved as " + self.json_file_path)

    def get_json_file(self):
        return self.json_file_path

    def create_json_file_path(self, date_time):
        json_file_name = f"{date_time}_{self.photo_name[:-4]}.json"
        json_file_path = os.path.join(self.json_dir, json_file_name)
        return json_file_path
    
    def run(self):
        date_time = Utils.get_datetime_string()
        self.json_file_path = self.create_json_file_path(date_time)
        self.analyse_skin()

