from flask import Flask, request, jsonify
import cv2
import numpy as np
import joblib
from flask_cors import CORS
from insightface.app import FaceAnalysis
import json

# Cargar el JSON externo con la información de estudiantes
with open("estudiantes.json", "r", encoding="utf-8") as f:
    estudiantes = json.load(f)

app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "http://localhost:3000"}})

# Cargar modelo entrenado
clf = joblib.load("models/face_classifier.pkl")

# Inicializar ArcFace
face_app = FaceAnalysis(name='buffalo_l')
face_app.prepare(ctx_id=0)


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No se envió ningún archivo"})

    file = request.files["file"]
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    faces = face_app.get(img)
    if not faces:
        return jsonify({"error": "No se detectó rostro"})

    emb = faces[0].embedding.reshape(1, -1)
    pred = clf.predict(emb)[0]   # ej. "estudiante_01"
    prob = clf.predict_proba(emb).max()

    threshold = 0.80
    if prob < threshold:
        return jsonify({"error": "Persona no registrada en el sistema"})

    # Buscar directamente en el JSON usando la etiqueta del modelo
    info = estudiantes.get(pred)
    if not info:
        return jsonify({"error": f"No se encontró información para {pred}"})

    return jsonify({
        "estudiante": pred,
        "confianza": float(prob),
        "nombre": info.get("nombre"),
        "codigo": info.get("codigo"),
        "carrera": info.get("carrera"),
        "ciclo": info.get("ciclo")
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
