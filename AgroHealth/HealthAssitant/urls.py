from django.urls import path
from . import views


urlpatterns = [
    path('upload/crop/', views.CropImageUpload.as_view(), name='upload_crop_image'),
    path('upload/animal/', views.AnimalImageUpload.as_view(), name='upload_animal_image'),

path('detect/disease/animal', views.DiseaseDetection.as_view(), name='detect_disease'),
    path('recommend/treatment/<str:endpoint>/', views.TreatmentRecommendation.as_view(), name='recommend_treatment'),
]



