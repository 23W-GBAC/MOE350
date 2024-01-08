import os
from PIL import Image, ImageEnhance

# Here i set the input and output directories
input_dir = 'Images/'
output_dir = 'enhanced_images/'

# Here i ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# I write a Function to enhance images
def enhance_image(input_path, output_path):
    try:
        img = Image.open(input_path)

        # I apply enhancements (increase contrast)
        enhancer = ImageEnhance.Color(img)
        enhanced_img = enhancer.enhance(1.5)  # Adjust enhancement factor as needed

        # Here were i Save my enhanced image
        enhanced_img.save(output_path)
        print(f"Image enhanced and saved: {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Monitor the input directory for new image files
while True:
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file formats as needed
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"enhanced_{filename}")
            
            # Check if the output file already exists
            if not os.path.exists(output_path):
                enhance_image(input_path, output_path)
                
    # You can adjust the frequency of checking for new images (e.g., using time.sleep(seconds))
