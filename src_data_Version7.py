import tensorflow as tf

def load_cifar10(normalize=True):
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    if normalize:
        x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)