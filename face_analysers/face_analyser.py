import boto3
import os
import json

from datetime import datetime
from utils.utils import Utils

class FaceAnalyser:
    ALL_ATTRIBUTES = ['AGE_RANGE', 'BEARD', 'EMOTIONS', 'EYE_DIRECTION',
                           'EYEGLASSES', 'EYES_OPEN', 'GENDER', 'MOUTH_OPEN', 
                           'MUSTACHE', 'FACE_OCCLUDED', 'SMILE', 'SUNGLASSES']
    
    def __init__(self, photo_dir, photo_name, removed_attributes=[]):
        self.removed_attributes = removed_attributes
        self.json_dir = Utils.parse_json_dir_path('face_features')
        self.photo_dir = photo_dir
        self.photo_name = photo_name
        self.source_image_path = os.path.join(self.photo_dir, self.photo_name)
        self.json_file_path = ""

    def get_required_attributes(self):
        required_attributes = []
        for attribute in FaceAnalyser.ALL_ATTRIBUTES:
             if attribute not in self.removed_attributes:
                 required_attributes.append(attribute)
        return required_attributes

    def initialize_rekognition_client(self, region_name='us-west-2'):
        client = boto3.client('rekognition', region_name=region_name)
        return client

    def analyse_face(self):
        start_time = datetime.now()
        client = self.initialize_rekognition_client()

        with open(self.source_image_path, 'rb') as source_image:
            source_image_bytes = source_image.read()
            print("Source:", self.source_image_path)
            
        try:
            response = client.detect_faces(
                Image={'Bytes': source_image_bytes},
                Attributes=self.get_required_attributes()
            )
            print("Analyse complete.")
            self.save_into_json(response)
        except Exception as e:
            print('Error occurred: %s', e)
        end_time = datetime.now()
        print("Duration (s):", (end_time - start_time).total_seconds())
        
    def save_into_json(self, data):
        with open(self.json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def create_json_file_path(self, date_time):
        json_file_name = f"{date_time}_{self.photo_name[:-4]}.json"
        json_file_path = os.path.join(self.json_dir, json_file_name)
        return json_file_path
    
    def run(self):
        date_time = Utils.get_datetime_string()
        self.json_file_path = self.create_json_file_path(date_time)
        self.analyse_face()
