import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(input_shape=(512, 512, 3)):
    base_model = tf.keras.applications.Xception(input_shape=input_shape,
                                                   include_top=False,
                                                   weights='imagenet')

    base_model.trainable = False

    model = models.Sequential()

    model.add(base_model)

    model.add(layers.GlobalAveragePooling2D())

    model.add(layers.BatchNormalization())

    model.add(layers.Dense(32, activation='relu'))

    model.add(layers.BatchNormalization())

    model.add(layers.Dense(3, activation='softmax'))

    return model
