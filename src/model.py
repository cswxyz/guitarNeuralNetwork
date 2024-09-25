import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(input_shape=(512, 512, 3)):
    # Load the pre-trained MobileNetV2 model, excluding the top classification layer
    base_model = tf.keras.applications.MobileNetV2(input_shape=input_shape,
                                                   include_top=False,
                                                   weights='imagenet')

    base_model.trainable = False  # Keep base model frozen

    model = models.Sequential()

    model.add(base_model)

    model.add(layers.GlobalAveragePooling2D())

    model.add(layers.BatchNormalization())

    model.add(layers.Dense(128, activation='relu'))

    model.add(layers.BatchNormalization())

    model.add(layers.Dropout(0.3))

    # Final output layer for 3 classes
    model.add(layers.Dense(3, activation='softmax'))

    return model
