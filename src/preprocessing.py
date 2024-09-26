from PIL import Image
import os

# Preprocesses the image: resizing to a 512x512 pixel image
def preprocess(image_path, output_path, size=(512, 512)):
    try:
        with Image.open(image_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = img.resize(size)
            img.save(output_path)
            print(f"Processed and saved: {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Iterates through unprocessed images
# Creates a directory for each data type if it doesn't already exist
# Appends the new directories with their corresponding images
# Once they are sorted, preprocess_image() is called to resize them
def preprocess_folder(input_folder, output_folder, size=(512, 512)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Here we loop through the input_folder to process each image
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".jpg"):
            image_path = os.path.join(input_folder, file_name) # nnnn
            output_path = os.path.join(output_folder, file_name)
            preprocess(image_path, output_path, size)

# Call preprocess_folder with separate paths for each guitar type
preprocess_folder('data/raw_data/fender_jaguar', 'processed_data/fender_jaguar')
preprocess_folder('data/raw_data/fender_telecaster', 'processed_data/fender_telecaster')
preprocess_folder('data/raw_data/fender_stratocaster', 'processed_data/fender_stratocaster')