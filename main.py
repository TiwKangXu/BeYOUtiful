from camera import Camera
# from face_analysers.face_analyser import FaceAnalyser
from constants import PHOTO_DIR, PHOTO_NAME
from face_analysers.facepp_face_analyser import FacePPFaceAnalyser
from json_reader.skin_feature_json_reader import SkinFeatureJsonReader
from skin_analysers.facepp_skin_analyser import FacePPSkinAnalyser

import json

camera = Camera()

camera.run()

# photo_path = camera.get_photo_path()

# photo_dir = photo_path[:-20]
# photo_name = photo_path[-19:]

photo_dir = PHOTO_DIR
photo_name = PHOTO_NAME

face_analyser = FacePPSkinAnalyser(photo_dir, photo_name)

face_analyser.run()

json_file_path = face_analyser.get_json_file()

json_reader = SkinFeatureJsonReader(json_file_path)
json_reader.run()