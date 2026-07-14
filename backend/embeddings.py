import os
import numpy as np
import cv2
from insightface.app import FaceAnalysis

app = FaceAnalysis(name='buffalo_l')  # o 'antelopev2'
app.prepare(ctx_id=0)

input_dir = "../processed_dataset"
output_dir = "embeddings"

X, y = [], []

for student in os.listdir(input_dir):
    student_path = os.path.join(input_dir, student)
    for img_name in os.listdir(student_path):
        img_path = os.path.join(student_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            print(f"[WARNING] Imagen inválida: {img_name}")
            continue

        faces = app.get(img)
        if not faces:
            print(f"[WARNING] No se detectó rostro en: {img_name}")
            continue

        emb = faces[0].embedding
        X.append(emb)
        y.append(student)

np.save(os.path.join(output_dir, "embeddings.npy"), np.array(X))
np.save(os.path.join(output_dir, "labels.npy"), np.array(y))
