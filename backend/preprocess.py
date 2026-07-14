import os
import cv2
from mtcnn import MTCNN

input_dir = "../dataset"
output_dir = "../processed_dataset"

detector = MTCNN()

for student in os.listdir(input_dir):
    student_path = os.path.join(input_dir, student)
    save_path = os.path.join(output_dir, student)
    os.makedirs(save_path, exist_ok=True)

    for img_name in os.listdir(student_path):
        img_path = os.path.join(student_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            print(f"[WARNING] Imagen inválida: {img_name}")
            continue

        faces = detector.detect_faces(img)
        if not faces:
            print(f"[WARNING] No se detectó rostro en: {img_name}")
            continue

        # Tomar el primer rostro detectado
        x, y, w, h = faces[0]['box']
        face = img[y:y+h, x:x+w]

        if face.size == 0:
            print(f"[WARNING] Recorte vacío en: {img_name}")
            continue

        face = cv2.resize(face, (112, 112))
        cv2.imwrite(os.path.join(save_path, img_name), face)
    