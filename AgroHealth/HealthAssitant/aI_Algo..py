import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class DiseaseDetectionAndClassification:
    def __init__(self, image_shape=(128, 128, 3), num_classes=10):
        self.image_shape = image_shape
        self.num_classes = num_classes
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=self.image_shape),
            MaxPooling2D((2, 2)),
            Dropout(0.25),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Dropout(0.25),
            Conv2D(128, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Dropout(0.25),
            Flatten(),
            Dense(128, activation='relu'),
            Dropout(0.5),
            Dense(self.num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train_model(self, images, labels, batch_size=32, epochs=20, validation_split=0.2):
        images = np.array(images)
        labels = np.array(labels)
        labels = LabelEncoder().fit_transform(labels)
        labels = tf.keras.utils.to_categorical(labels, num_classes=self.num_classes)
        
        X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=validation_split)
        
        datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
            zoom_range=0.2
        )
        train_generator = datagen.flow(X_train, y_train, batch_size=batch_size)
        val_generator = datagen.flow(X_val, y_val, batch_size=batch_size)
        
        self.model.fit(train_generator, epochs=epochs, validation_data=val_generator)

    def evaluate_model(self, images, labels):
        images = np.array(images)
        labels = np.array(labels)
        labels = LabelEncoder().fit_transform(labels)
        labels = tf.keras.utils.to_categorical(labels, num_classes=self.num_classes)
        
        images = images / 255.0
        loss, accuracy = self.model.evaluate(images, labels)
        print(f"Loss: {loss}, Accuracy: {accuracy}")
        return loss, accuracy

    def predict(self, image):
        image = np.expand_dims(image, axis=0)
        image = image / 255.0
        prediction = self.model.predict(image)
        return np.argmax(prediction, axis=1)

    def classify_symptoms(self, symptoms, symptom_to_disease_mapping):
        for disease, symptom_list in symptom_to_disease_mapping.items():
            if all(symptom in symptoms for symptom in symptom_list):
                return disease
        return "Unknown Disease"
