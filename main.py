from camera import Camera
# from face_analysers.face_analyser import FaceAnalyser
from face_analysers.facepp_face_analyser import FacePPFaceAnalyser

camera = Camera()

camera.run()

photo_path = camera.get_photo_path()

photo_dir = photo_path[:-20]
photo_name = photo_path[-19:]

face_analyser = FacePPFaceAnalyser(photo_dir, photo_name)

face_analyser.run()