from PIL import Image
import os
import logging

def is_black_and_white(img):
    return img.mode == "L"

def convert_to_black_and_white(input_path, output_path):
    try:
        img = Image.open(input_path)

        if not is_black_and_white(img):
            bw_img = img.convert("L")
            bw_img.save(output_path)
            logging.info(f"Image converted to black and white: {output_path}")
        else:
            logging.info(f"Image is already black and white: {input_path}")

    except Exception as e:
        logging.error(f"Error processing {input_path}: {e}")

def process_images(input_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"bw_{filename}")

            convert_to_black_and_white(input_path, output_path)

if __name__ == "__main__":
    input_directory = 'Colored_Images'
    output_directory = 'Gray_Images'

    logging.basicConfig(level=logging.INFO, filename='conversion.log', filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s')

    process_images(input_directory, output_directory)

