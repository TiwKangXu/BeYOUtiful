import pandas as pd
from constants import BEYOUTIFUL_PATH
from facepp_face_analyser import FacePPFaceAnalyser
import os

dir_path = BEYOUTIFUL_PATH + '/face_analysers/BeYOUtifulShapeDataset/training_set/Square'

csv_file_path = 'faces_data_square.csv'
file_exists = os.path.isfile(csv_file_path)
no_response_faces = {}

for i in range(200):
    photo_name = f"square{i}.jpg"
    face_analyser = FacePPFaceAnalyser(dir_path, photo_name)
    face_analyser.run()
    response = face_analyser.get_response()
    
    print(f"================================{i}================================")
    
    try:
        df_faces_i = pd.json_normalize(response["faces"])
        df_faces_i['image'] = photo_name
        df_faces_i['face_shape'] = 'square'
        
        df_faces_i.to_csv(csv_file_path, mode='a', header=not file_exists, index=False)
    except Exception as e:
        no_response_faces[f"{i}"] = e
    file_exists = True
    
    print(f"Data for image square{i}.jpg saved to faces_data_square.csv")

print(no_response_faces)

