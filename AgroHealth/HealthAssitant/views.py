from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Crop, Animal, Disease, Treatment
from .serializers import CropSerializer, AnimalSerializer, DiseaseSerializer, TreatmentSerializer
from .ai_Algo import detect_crop_disease, detect_animal_disease, recommend_crop_treatment, recommend_animal_treatment
class CropImageUpload(generics.CreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        crop_serializer = self.serializer_class(data=request.data)
        if crop_serializer.is_valid():
            crop_serializer.save()
            return Response(crop_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(crop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalImageUpload(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiseaseDetection(generics.RetrieveAPIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)  # Include JSONParser for handling JSON requests

    def post(self, request, *args, **kwargs):
        data = request.data
        symptoms = data.get('symptoms', None)
        image_file = request.FILES.get('image', None)
        
        if not symptoms:
            return Response({'error': 'Symptoms are required for animal endpoint'}, status=status.HTTP_400_BAD_REQUEST)
        
        if image_file:
            # Save the uploaded image file if provided
            animal_instance = Animal(image=image_file)
            animal_instance.save()
        
        # Simulate detection based on symptoms
        try:
            disease_name, treatment = detect_animal_disease(symptoms)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'disease': disease_name,
            'treatment': treatment
        })

class TreatmentRecommendation(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        endpoint = kwargs['endpoint']
        if endpoint == 'crop':
            treatment = recommend_crop_treatment("Disease A")
        elif endpoint == 'animal':
            disease_name = request.query_params.get('disease_name', None)
            if disease_name:
                try:
                    treatment = recommend_animal_treatment(disease_name)
                except ValueError as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'disease_name parameter is required for animal endpoint'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid endpoint'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'treatment': treatment
        })