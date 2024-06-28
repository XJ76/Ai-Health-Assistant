from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Crop, Animal, Disease, Treatment
from .serializers import CropSerializer, AnimalSerializer, DiseaseSerializer, TreatmentSerializer
from .ai_Algo import analyze_crop_image, analyze_animal_image

class CropImageUpload(generics.CreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            image_path = file_serializer.data['image']
            disease_index, treatment = analyze_crop_image(image_path)
            return Response({
                'file_data': file_serializer.data,
                'disease_index': disease_index,
                'treatment': treatment
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalImageUpload(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            image_path = file_serializer.data['image']
            disease_index, treatment = analyze_animal_image(image_path)
            return Response({
                'file_data': file_serializer.data,
                'disease_index': disease_index,
                'treatment': treatment
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiseaseDetection(generics.RetrieveAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    def get_object(self):
        # Implement your logic to detect disease based on uploaded image
        # Example: image = self.request.data['image']
        # disease = detect_disease(image)
        # return disease
        pass

class TreatmentRecommendation(generics.RetrieveAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

    def get_object(self):
        # Implement your logic to recommend treatment based on detected disease
        # Example: disease_id = self.kwargs['disease_id']
        # treatment = get_treatment_recommendation(disease_id)
        # return treatment
        pass

