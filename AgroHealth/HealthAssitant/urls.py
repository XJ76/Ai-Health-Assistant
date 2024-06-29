from django.urls import path
from . import views


urlpatterns = [
    path('upload/crop/', views.CropImageUpload.as_view(), name='upload_crop_image'),
    path('upload/animal/', views.AnimalImageUpload.as_view(), name='upload_animal_image'),
    path('detect/disease/animal/', views.DiseaseDetectionAndTreatment.as_view(), name='detect_animal_disease'),
    path('detect/disease/crop/', views.CropDiseaseDetection.as_view(), name='detect_crop_disease'),
    path('recommend/treatment/<str:endpoint>/', views.TreatmentRecommendation.as_view(), name='recommend_treatment'),
]

