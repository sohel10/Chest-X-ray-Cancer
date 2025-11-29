import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):

        # Load trained model
        model = load_model(os.path.join("model", "model.h5"))

        # Preprocess input image
        img = image.load_img(self.filename, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        result = np.argmax(model.predict(img_array), axis=1)[0]
        print("Prediction index:", result)

        # Correct mapping for TWO classes
        class_labels = {
            0: "Adenocarcinoma Cancer",
            1: "Normal"
        }

        prediction = class_labels[result]
        return [{"image": prediction}]
