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
        "Disease A": "For Disease A, it is recommended to apply a nitrogen-based fertilizer such as urea or ammonium nitrate. Ensure proper soil pH by conducting a soil test and adjusting accordingly. Monitor for pest activity and take appropriate measures to control pests if necessary.",
        "Disease B": "For Disease B, use a fungicide treatment such as copper-based fungicides or sulfur. Rotate crops to prevent recurrence and improve soil health. Ensure proper spacing between plants to allow for adequate air circulation and reduce humidity levels.",
        "Disease C": "For Disease C, increase watering frequency to maintain consistent soil moisture levels. Mulch around the base of the plants to retain moisture and reduce evaporation. Consider using drip irrigation to provide a steady supply of water directly to the plant roots.",
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
        "Rabies": "For Rabies, administer a rabies vaccine immediately and consult a veterinarian. Ensure the animal is isolated to prevent the spread of the disease. Provide supportive care such as fluids and pain management as directed by the veterinarian.",
        "Foot-and-Mouth Disease": "For Foot-and-Mouth Disease, isolate the infected animal and consult a veterinarian. Disinfect the area thoroughly and monitor other animals for symptoms. Provide supportive care such as fluids and pain management as directed by the veterinarian.",
        "Avian Influenza": "For Avian Influenza, isolate the infected birds and consult a veterinarian. Implement biosecurity measures such as restricting access to the area and disinfecting equipment and clothing. Provide supportive care such as fluids and pain management as directed by the veterinarian.",
        "Bovine Spongiform Encephalopathy (Mad Cow Disease)": "For Bovine Spongiform Encephalopathy (Mad Cow Disease), consult a veterinarian immediately. Follow regulatory guidelines for handling and reporting the disease. Provide supportive care such as fluids and pain management as directed by the veterinarian.",
        "Canine Parvovirus": "For Canine Parvovirus, administer fluids to prevent dehydration and consult a veterinarian. Ensure proper sanitation to prevent the spread of the virus. Provide supportive care such as pain management and anti-nausea medication as directed by the veterinarian.",
        "Feline Leukemia Virus": "For Feline Leukemia Virus, consult a veterinarian for antiviral treatment options such as interferon or zidovudine. Provide supportive care such as fluids, nutritional support, and pain management as directed by the veterinarian. Monitor the animal's condition closely and provide a stress-free environment.",
        "Newcastle Disease": "For Newcastle Disease, isolate the infected birds and consult a veterinarian. Implement strict biosecurity measures such as restricting access to the area and disinfecting equipment and clothing. Provide supportive care such as fluids and pain management as directed by the veterinarian.",
        "Swine Influenza": "For Swine Influenza, isolate the infected pigs and consult a veterinarian. Monitor the herd for additional cases and implement biosecurity measures such as restricting access to the area and disinfecting equipment and clothing. Provide supportive care such as fluids and pain management as directed by the veterinarian.",
        "Equine Infectious Anemia": "For Equine Infectious Anemia, consult a veterinarian for supportive care such as fluids, nutritional support, and pain management. Follow regulatory guidelines for testing and reporting the disease. Monitor the animal's condition closely and provide a stress-free environment.",
        "Scrapie": "For Scrapie, consult a veterinarian for management options such as culling infected animals and implementing biosecurity measures. Follow regulatory guidelines for handling and reporting the disease. Provide supportive care such as fluids and pain management as directed by the veterinarian.",
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
