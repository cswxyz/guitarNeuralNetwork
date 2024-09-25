import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
from model import build_model

def load_data(data_dir, img_size=(512, 512), batch_size=32):
    datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        validation_split=0.2,
        rotation_range=30,
        width_shift_range=0.3,
        height_shift_range=0.3,
        shear_range=0.3,
        zoom_range=0.3,
        horizontal_flip=True,
        brightness_range=[0.7, 1.3]
    )

    train_generator = datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='sparse',
        subset='training'
    )

    validation_generator = datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='sparse',
        subset='validation'
    )

    return train_generator, validation_generator

def train_model(data_dir, model_save_path='models/saved_model.keras', epochs=10, batch_size=32):
    train_data, val_data = load_data(data_dir, img_size=(512, 512), batch_size=batch_size)

    # Build the model
    model = build_model(input_shape=(512, 512, 3))

    # Compile the model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Define a ModelCheckpoint to save the model
    model_checkpoint = ModelCheckpoint(model_save_path, save_best_only=True)

    # Train the model and store the training history
    history = model.fit(train_data, validation_data=val_data, epochs=epochs, callbacks=[model_checkpoint])

    # Save the trained model
    model.save(model_save_path)
    print(f"Model saved at {model_save_path}")

    # Print final training and validation accuracy
    final_train_accuracy = history.history['accuracy'][-1]
    final_val_accuracy = history.history['val_accuracy'][-1]

    print(f"Final Training Accuracy: {final_train_accuracy}")
    print(f"Final Validation Accuracy: {final_val_accuracy}")

if __name__ == "__main__":
    train_model('data/processed_data', epochs=10, batch_size=32)
