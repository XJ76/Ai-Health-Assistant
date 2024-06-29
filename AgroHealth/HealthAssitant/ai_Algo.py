# ai_algo.py
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import json
from difflib import get_close_matches

def detect_crop_disease(image_path):
    # Simulate detection for crop diseases using a pre-trained ML model
    model = hub.load("https://tfhub.dev/google/imagenet/resnet_v2_50/classification/4")
    image = Image.open(image_path).resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    
    predictions = model(image)
    predicted_class = np.argmax(predictions, axis=-1)
    
    # Map the predicted class to a disease and treatment
    disease_mapping = {
        0: ("Disease A", "Apply nitrogen-based fertilizer"),
        1: ("Disease B", "Use fungicide treatment"),
        2: ("Disease C", "Increase watering frequency"),
    }
    
    disease, treatment = disease_mapping.get(predicted_class[0], ("Unknown Disease", "Consult an agricultural expert"))
    return disease, treatment
def detect_animal_disease(symptoms):
    # Simulate detection for animal diseases based on symptoms using a more comprehensive dataset
    dataset = {
        "Fever,headache": ("Rabies", "Administer rabies vaccine and consult a veterinarian. Ensure the animal is isolated to prevent the spread of the disease."),
        "Fever,blisters in the mouth and on feet": ("Foot-and-Mouth Disease", "Isolate the infected animal and consult a veterinarian. Disinfect the area and monitor other animals for symptoms."),
        "Coughing,sneezing,nasal discharge": ("Avian Influenza", "Isolate the infected birds and consult a veterinarian. Implement biosecurity measures to prevent further spread."),
        "Nervousness,aggression,lack of coordination": ("Bovine Spongiform Encephalopathy (Mad Cow Disease)", "Consult a veterinarian immediately. Follow regulatory guidelines for handling and reporting."),
        "Severe,bloody diarrhea,lethargy": ("Canine Parvovirus", "Administer fluids and consult a veterinarian. Ensure proper sanitation to prevent the spread of the virus."),
        "Loss of appetite,weight loss,poor coat condition": ("Feline Leukemia Virus", "Consult a veterinarian for antiviral treatment. Provide supportive care and monitor the animal's condition."),
        "Respiratory distress,nervous signs,greenish diarrhea": ("Newcastle Disease", "Isolate the infected birds and consult a veterinarian. Implement strict biosecurity measures."),
        "Coughing,nasal discharge,fever": ("Swine Influenza", "Isolate the infected pigs and consult a veterinarian. Monitor the herd for additional cases."),
        "Fever,depression,weight loss,anemia": ("Equine Infectious Anemia", "Consult a veterinarian for supportive care. Follow regulatory guidelines for testing and reporting."),
        "Itching,behavioral changes,weight loss": ("Scrapie", "Consult a veterinarian for management. Follow regulatory guidelines for handling and reporting."),
    }
    
    key = ','.join(symptoms)
    if key in dataset:
        return dataset[key]
    else:
        # Find the closest match for the given symptoms
        closest_match = get_close_matches(key, dataset.keys(), n=1, cutoff=0.6)
        if closest_match:
            return dataset[closest_match[0]]
        else:
            raise ValueError("No disease matched the given symptoms or image file")   

def recommend_crop_treatment(disease_name):
    # Placeholder for actual treatment recommendation logic
    treatments = {
        "Disease A": "Apply nitrogen-based fertilizer. Ensure proper soil pH and monitor for pest activity.",
        "Disease B": "Use fungicide treatment. Rotate crops to prevent recurrence and improve soil health.",
        "Disease C": "Increase watering frequency. Mulch around the base of the plants to retain moisture.",
    }
    
    if disease_name in treatments:
        return treatments[disease_name]
    else:
        # Find the closest match for the given disease name
        closest_match = get_close_matches(disease_name, treatments.keys(), n=1, cutoff=0.6)
        if closest_match:
            return treatments[closest_match[0]]
        else:
            raise ValueError("No treatment recommendation available for the disease, recommend you to contact an agricultural expert")

def recommend_animal_treatment(disease_name):
    # Treatment recommendations based on disease name with more comprehensive suggestions
    treatments = {
        "Rabies": "Administer rabies vaccine and consult a veterinarian. Ensure the animal is isolated to prevent the spread of the disease.",
        "Foot-and-Mouth Disease": "Isolate the infected animal and consult a veterinarian. Disinfect the area and monitor other animals for symptoms.",
        "Avian Influenza": "Isolate the infected birds and consult a veterinarian. Implement biosecurity measures to prevent further spread.",
        "Bovine Spongiform Encephalopathy (Mad Cow Disease)": "Consult a veterinarian immediately. Follow regulatory guidelines for handling and reporting.",
        "Canine Parvovirus": "Administer fluids and consult a veterinarian. Ensure proper sanitation to prevent the spread of the virus.",
        "Feline Leukemia Virus": "Consult a veterinarian for antiviral treatment. Provide supportive care and monitor the animal's condition.",
        "Newcastle Disease": "Isolate the infected birds and consult a veterinarian. Implement strict biosecurity measures.",
        "Swine Influenza": "Isolate the infected pigs and consult a veterinarian. Monitor the herd for additional cases.",
        "Equine Infectious Anemia": "Consult a veterinarian for supportive care. Follow regulatory guidelines for testing and reporting.",
        "Scrapie": "Consult a veterinarian for management. Follow regulatory guidelines for handling and reporting."
    }
    
    if disease_name in treatments:
        return treatments[disease_name]
    else:
        # Find the closest match for the given disease name
        closest_match = get_close_matches(disease_name, treatments.keys(), n=1, cutoff=0.6)
        if closest_match:
            return treatments[closest_match[0]]
        else:
            raise ValueError("No treatment recommendation available for the disease, recommend you to contact a veterinarian")

