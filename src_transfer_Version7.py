from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras import models

def build_resnet_transfer(input_shape=(32,32,3), num_classes=10):
    resnet = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)
    resnet.trainable = False
    model = models.Sequential([
        resnet,
        GlobalAveragePooling2D(),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(num_classes, activation='softmax')
    ])
    return model