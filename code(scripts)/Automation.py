from PIL import Image
import os

def convert_to_black_and_white(input_path, output_path):
    try:
        img = Image.open(input_path)

        bw_img = img.convert("L")

       
        bw_img.save(output_path)
        print(f"Image converted to black and white: {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    input_directory = 'Colored_Images'
    output_directory = 'Gray_Images'

    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"bw_{filename}")

            convert_to_black_and_white(input_path, output_path)
