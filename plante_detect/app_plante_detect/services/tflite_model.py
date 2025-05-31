import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite
import os

# Charger le modèle
interpreter = tflite.Interpreter(model_path=os.path.join("media", "model", "model_plante.tflite"))
interpreter.allocate_tensors()

CLASS_NAMES = {
    0: "Apple - Tavelure (scab)",
    1: "Apple - Pourriture noire",
    2: "Apple - Rouille du pommier",
    3: "Apple - Sain",
    4: "Fond - Sans feuilles",
    5: "Blueberry - Sain",
    6: "Cherry - Oïdium",
    7: "Cherry - Sain",
    8: "Corn - Tache grise",
    9: "Corn - Rouille commune",
    10: "Corn - Brûlure des feuilles du nord",
    11: "Corn - Sain",
    12: "Grape - Pourriture noire",
    13: "Grape - Rougeot noir",
    14: "Grape - Brûlure des feuilles",
    15: "Grape - Sain",
    16: "Orange - Greening (Haunglongbing)",
    17: "Peach - Tache bactérienne",
    18: "Peach - Sain",
    19: "Pepper - Tache bactérienne",
    20: "Pepper - Sain",
    21: "Potato - Brûlure précoce",
    22: "Potato - Sain",
    23: "Potato - Mildiou",
    24: "Raspberry - Sain",
    25: "Soybean - Sain",
    26: "Squash - Oïdium",
    27: "Strawberry - Sain",
    28: "Strawberry - Brûlure des feuilles",
    29: "Tomato - Tache bactérienne",
    30: "Tomato - Brûlure précoce",
    31: "Tomato - Sain",
    32: "Tomato - Mildiou",
    33: "Tomato - Moisissure des feuilles",
    34: "Tomato - Tache septorienne",
    35: "Tomato - Acariens (araignées rouges)",
    36: "Tomato - Tache cible",
    37: "Tomato - Virus de la mosaïque",
    38: "Tomato - Virus de l’enroulement jaune"
}


# Obtenir les détails d'entrée et de sortie
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess_image(image_file):
    img = Image.open(image_file).resize((224, 224)).convert('RGB')
    img = np.array(img).astype(np.float32) / 255.0
    return img.reshape(1, 224, 224, 3)

def predict(image_file):
    input_data = preprocess_image(image_file)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_index = int(np.argmax(output_data))
    predicted_class = CLASS_NAMES.get(predicted_index, "Inconnu")
    return predicted_class

