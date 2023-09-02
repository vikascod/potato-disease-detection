from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
import io
from PIL import Image
from tensorflow import keras

app = FastAPI()

# Load the model
model = keras.models.load_model('potato_disease.h5')

def read_image(image):
    img = Image.open(io.BytesIO(image))
    img = img.resize((256, 256))
    img = np.array(img)
    return img

@app.get('/')
async def home():
    return "Welcome to Potato Disease detector app!"

@app.post('/predict')
async def detect(file: UploadFile = File(...)):
    image = read_image(await file.read())
    # our model takes image in batches
    # by the expanding of dimension it becomes - [1, 256, 256, 3]
    batch_image = np.expand_dims(image, 0)
    # Prediction
    prediction = model.predict(batch_image)
    # Convert to list
    pred = np.argmax(prediction.tolist())
    # print(pred)
    
    class_labels = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
    
    # Find the confidence probability
    confidence = float(np.max(prediction[0]))
    # print(confidence)
    
    # Map the class index to the class label
    predicted_class = class_labels[pred]

    return {"prediction": predicted_class, "confidence": confidence}


