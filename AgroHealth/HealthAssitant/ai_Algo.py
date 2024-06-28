import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained models for disease detection
crop_disease_model = load_model('path_to_crop_disease_model.h5')
animal_disease_model = load_model('path_to_animal_disease_model.h5')

# Load pre-trained models for treatment recommendation
crop_treatment_model = load_model('path_to_crop_treatment_model.h5')
animal_treatment_model = load_model('path_to_animal_treatment_model.h5')

def preprocess_image(image_path):
    """
    Preprocess the image to be compatible with the model input.
    """
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def detect_crop_disease(image_path):
    """
    Detect disease in the crop image.
    """
    image = preprocess_image(image_path)
    prediction = crop_disease_model.predict(image)
    disease_index = np.argmax(prediction)
    return disease_index

def detect_animal_disease(image_path):
    """
    Detect disease in the animal image.
    """
    image = preprocess_image(image_path)
    prediction = animal_disease_model.predict(image)
    disease_index = np.argmax(prediction)
    return disease_index

def recommend_crop_treatment(disease_index):
    """
    Recommend treatment for the detected crop disease.
    """
    treatment = crop_treatment_model.predict(np.array([disease_index]))
    return treatment

def recommend_animal_treatment(disease_index):
    """
    Recommend treatment for the detected animal disease.
    """
    treatment = animal_treatment_model.predict(np.array([disease_index]))
    return treatment

def analyze_crop_image(image_path):
    """
    Analyze the crop image and provide disease detection and treatment recommendation.
    """
    disease_index = detect_crop_disease(image_path)
    treatment = recommend_crop_treatment(disease_index)
    return disease_index, treatment

def analyze_animal_image(image_path):
    """
    Analyze the animal image and provide disease detection and treatment recommendation.
    """
    disease_index = detect_animal_disease(image_path)
    treatment = recommend_animal_treatment(disease_index)
    return disease_index, treatment
