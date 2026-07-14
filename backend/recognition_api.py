import cv2
import joblib
import json
from flask import Flask, request, jsonify
from insightface.app import FaceAnalysis

app = Flask(__name__)

# Cargar clasificador entrenado
clf = joblib.load("models/face_classifier.pkl")

# Inicializar modelo de embeddings
face_app = FaceAnalysis(name='buffalo_l')
face_app.prepare(ctx_id=0)

# Cargar información de estudiantes
with open("estudiantes.json", "r", encoding="utf-8") as f:
    info_estudiantes = json.load(f)

@app.route("/reconocer", methods=["POST"])
def reconocer():
    file = request.files["imagen"]
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    faces = face_app.get(img)
    if not faces:
        return jsonify({"resultado": "No se detectó rostro"})

    emb = faces[0].embedding.reshape(1, -1)
    pred = clf.predict(emb)[0]

    datos = info_estudiantes.get(pred, "No registrado")
    return jsonify({"estudiante": pred, "informacion": datos})

if __name__ == "__main__":
    app.run(debug=True)
