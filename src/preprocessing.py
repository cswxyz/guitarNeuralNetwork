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
    # Skip processing if output_folder already exists and is not empty
    if os.path.exists(output_folder) and len(os.listdir(output_folder)) > 0:
        print(f"Skipping {output_folder}: already processed.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".jpg"):
            image_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            preprocess(image_path, output_path, size)

# List of all guitar models to check
guitar_models = [
    "fender_jaguar", "fender_telecaster", "fender_stratocaster", "fender_jazzmaster",
    "fender_mustang", "fender_duosonic", "fender_leadii", "fender_toronado",
    "fender_performer", "fender_starcaster"
]

for model in guitar_models:
    input_dir = f"data/raw_data/{model}"
    output_dir = f"processed_data/{model}"
    if not os.path.exists(input_dir):
        print(f"Skipping {model}: {input_dir} does not exist.")
        continue
    preprocess_folder(input_dir, output_dir)