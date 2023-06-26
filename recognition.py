import face_recognition
import os

def process_image():
    file = []
    unknown_image = []
    unknown_face_encoding = []
    unknown_path = "./static/unknown/"
    known_path = "./known/"

    for x in os.listdir(unknown_path):
        file.append(x)
    count = len(file)

    known_name=[]
    for x in os.listdir(known_path):
        known_name.append(x)
    print(known_name)
    obama_image = face_recognition.load_image_file(known_path + known_name[0])
    for i in file:
        unknown_image.append(face_recognition.load_image_file(unknown_path + i))

    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    for i in unknown_image:
        try:
            face_encoding = face_recognition.face_encodings(i)[0]
            unknown_face_encoding.append(face_encoding)
        except IndexError:
            # Skip the image if no face is found
            continue

    known_faces = [obama_face_encoding]

    matching_images = []
    for encoding, filename in zip(unknown_face_encoding, file):
        results = face_recognition.compare_faces(known_faces, encoding, tolerance=0.8)
        if results[0]:
            matching_images.append(filename)
    
    return matching_images