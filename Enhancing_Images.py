import os
from PIL import Image, ImageEnhance


input_dir = 'Images/'
output_dir = 'enhanced_images/'


os.makedirs(output_dir, exist_ok=True)


def enhance_image(input_path, output_path):
    try:
        img = Image.open(input_path)

       
        enhancer = ImageEnhance.Color(img)
        enhanced_img = enhancer.enhance(1.5)  

        
        enhanced_img.save(output_path)
        print(f"Image enhanced and saved: {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")


while True:
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"enhanced_{filename}")
            
            
            if not os.path.exists(output_path):
                enhance_image(input_path, output_path)
                
    
