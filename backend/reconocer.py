import cv2
import joblib
import json
from insightface.app import FaceAnalysis

# Cargar clasificador entrenado
clf = joblib.load("models/face_classifier.pkl")

# Inicializar modelo de embeddings
app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0)

# Cargar información de estudiantes
with open("estudiantes.json", "r", encoding="utf-8") as f:
    info_estudiantes = json.load(f)

def reconocer(img_path):
    img = cv2.imread(img_path)
    faces = app.get(img)
    if not faces:
        return "No se detectó rostro"

    emb = faces[0].embedding.reshape(1, -1)
    pred = clf.predict(emb)[0]

    datos = info_estudiantes.get(pred, "No registrada")
    return f"Estudiante: {pred}, Información: {datos}"

# Ejemplo de uso
if __name__ == "__main__":
    resultado = reconocer("ruta/a/una/foto.jpg")
    print(resultado)
