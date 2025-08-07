from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_augmentor():
    return ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True
    )