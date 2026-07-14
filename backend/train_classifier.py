import numpy as np
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV
import joblib

# Cargar embeddings y etiquetas
X = np.load("embeddings/embeddings.npy")
y = np.load("embeddings/labels.npy")

# Entrenar modelo base
base_clf = SVC(kernel='linear')

# Calibrar para obtener probabilidades (reemplazo de probability=True)
clf = CalibratedClassifierCV(base_clf, ensemble=False)
clf.fit(X, y)

# Guardar modelo entrenado
joblib.dump(clf, "models/face_classifier.pkl")
