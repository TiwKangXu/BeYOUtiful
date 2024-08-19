import boto3
import logging
import os
import json
from datetime import datetime

from constants import BEYOUTIFUL_PATH

def compare_faces(source_image_path, target_image_path, json_file_path, region_name='us-west-2'):
    # Initialize the Rekognition client
    client = boto3.client('rekognition', region_name=region_name)

    # Read the source image
    with open(source_image_path, 'rb') as source_image:
        source_image_bytes = source_image.read()
        print("Source:", source_image_path)

    # Read the target image
    with open(target_image_path, 'rb') as target_image:
        target_image_bytes = target_image.read()
        print("Target:", target_image_path)

    # Call Rekognition to compare faces
    try:
        response = client.compare_faces(
            SourceImage={'Bytes': source_image_bytes},
            TargetImage={'Bytes': target_image_bytes},
            SimilarityThreshold=0  # Adjust the threshold as needed
        )

        save_into_json(response, json_file_path)

        # Process and log results
        face_matches = response.get('FaceMatches', [])
        if face_matches:
            for face_match in face_matches:
                similarity = face_match['Similarity']
                logging.info('Similarity: %.2f%%', similarity)
                print("Similarity:", similarity)
        else:
            logging.info("No matching faces found.")

    except Exception as e:
        logging.error('Error occurred: %s', e)


    
def save_into_json(data, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def main():
    # Set the directory for logs
    log_dir = BEYOUTIFUL_PATH + '/logs/compare_faces'
    json_dir = BEYOUTIFUL_PATH + '/jsons/compare_faces'
    photo1_dir = BEYOUTIFUL_PATH + '/photos/twin'
    photo2_dir = BEYOUTIFUL_PATH + '/photos/twin'

    photo1_name = 'me1.jpg'
    photo2_name = 'me2.jpg'

    # Ensure the directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    date_time = datetime.now().strftime("%d%m%Y_%H%M%S")

    # Configure logging
    log_file_name = f"{date_time}_{photo1_name[:-4]}_{photo2_name[:-4]}.log"
    log_file_path = os.path.join(log_dir, log_file_name)

    json_file_name = f"{date_time}_{photo1_name[:-4]}_{photo2_name[:-4]}.json"
    json_file_path = os.path.join(json_dir, json_file_name)

    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Replace with the paths to your images
    source_image_path = os.path.join(photo1_dir, photo1_name)
    target_image_path = os.path.join(photo2_dir, photo2_name)

    compare_faces(source_image_path, target_image_path, json_file_path)

if __name__ == "__main__":
    main()