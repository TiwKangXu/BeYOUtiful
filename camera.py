import cv2
import os 

from constants import GALLERY
from utils.utils import Utils

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.ret = None
        self.frame = None
        self.gallery = GALLERY
        self.photo_path = ""
        self.is_save_photo = True

    def camera_is_opened(self):
        if not self.cap.isOpened():
            print("Error: Could not access the webcam.")
            exit()
        print("Press 't' to take the photo or 'q' to quit.")

    def generate_photo_path(self):
        date_time = Utils.get_datetime_string()
        photo_path = os.path.join(self.gallery, date_time) + ".jpg"
        self.photo_path = photo_path
        return photo_path
    
    def take_photo(self):
        print("Press 's' to save the photo or 'd' to discard.")
        while True:
            key = cv2.waitKey(1)
            if key == ord('s'):
                self.is_save_photo = True
                photo_path = self.generate_photo_path()
                cv2.imwrite(photo_path, self.frame)
                print(f"Photo saved as '{photo_path}'.")
                break
            elif key == ord('d'):
                self.is_save_photo = False
                print("Discard photo.")
                break

    def quit_camera(self):
        print("Exiting...")

    def kill_process(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def launch_camera(self):
        while True:
            self.ret, self.frame = self.cap.read()
            if not self.ret:
                print("Error: Failed to grab self.frame.")
                break

            cv2.imshow("Camera", self.frame)

            key = cv2.waitKey(1)
            if key == ord('t'):
                self.take_photo()
                if self.is_save_photo:
                    break
            elif key == ord('q'):
                self.quit_camera()
                break                
    
    def get_photo_path(self):
        return self.photo_path
    
    def run(self):
        self.launch_camera()
        self.kill_process()

# camera = Camera()
# camera.run()