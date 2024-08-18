from camera import Camera
# from face_analysers.face_analyser import FaceAnalyser
from face_analysers.facepp_face_analyser import FacePPFaceAnalyser
from skin_analysers.facepp_skin_analyser import FacePPSkinAnalyser

import json
import tkinter as tk
from tkinter import messagebox

camera = Camera()

camera.run()

photo_path = camera.get_photo_path()

photo_dir = photo_path[:-20]
photo_name = photo_path[-19:]

face_analyser = FacePPSkinAnalyser(photo_dir, photo_name)

face_analyser.run()

json_file_path = face_analyser.get_json_file()

with open(json_file_path, 'r') as file:
    data = json.load(file)

forehead_wrinkle_value = data['result']['forehead_wrinkle']['value']
dark_circle_value = data['result']['dark_circle']['value']
skin_type_details = data['result']['skin_type']
skin_type = [key for key, value in skin_type_details.items() if value == 1]


def show_data():
    data_text = (f"Forehead Wrinkle Value: {forehead_wrinkle_value}\n"
                 f"Dark Circle Value: {dark_circle_value}\n"
                 f"Skin Type: {', '.join(skin_type)}")
    
    messagebox.showinfo("Extracted Data", data_text)

root = tk.Tk()
root.title("Data Display")

show_button = tk.Button(root, text="Show Data", command=show_data)
show_button.pack(pady=20)

root.mainloop()