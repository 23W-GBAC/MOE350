# Automation:
Before we start i would like to show you my work:

here are some examples of what my code do:

### original BMW M4 Competition photo from colored to B&W:
<img src="./../Colored_Images/BMW_M4_Comp.jpg" alt="BMW M4 Competition photo" width="300" />
<img src="./../Gray_Images/bw_BMW_M4_Comp.jpg" alt="black and white BMW M4 Competition photo" width="300" />

### edited black and white BMW M4 Competition photo


### original Mercedes AMG E63 S photo from colored to B&W:
<img src="./../Colored_Images/Mercedes_AMG_E63_S_Sedan.jpg" alt="Mercedes AMG E63 S photo" width="300" />
<img src="./../Gray_Images/bw_Mercedes_AMG_E63_S_Sedan.jpg" alt="black and white Mercedes AMG E63 S photo" width="300" />




### Check the rest of the Colored images at my directory: [Colored_Images](./../Colored_Images)

### Check the rest of the Gray images at my directory: [Gray_Images](./../Gray_Images/)



### Introduction:

I encountered a challenge with my collection of colored images — they simply weren't meeting my preference. In pursuit of a solution, I decided to automate the process of converting these colored images to black and white. This not only addressed my aesthetic preferences but also offered a more cohesive visual style for my image repository. Below is the script I devised to seamlessly transition from colored to black and white images.

### Code Explanation:

```python
from PIL import Image
import os
```

- **PIL (Python Imaging Library):**
  - The `from PIL import Image` statement imports the Image module from the PIL library for image processing.

- **OS Module:**
  - `import os` allows interaction with the operating system, enabling tasks like file and directory manipulation.

```python
def convert_to_black_and_white(input_path, output_path):
    try:
        img = Image.open(input_path)

        # Convert the image to grayscale (black and white)
        bw_img = img.convert("L")

        # Save the black and white image
        bw_img.save(output_path)
        print(f"Image converted to black and white: {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
```

- **Convert to Black and White Function:**
  - `convert_to_black_and_white` is a function that takes two parameters: `input_path` (the path to the original colored image) and `output_path` (where the black and white image will be saved).

  - Inside the function, the code:
    - Opens the image using `Image.open`.
    - Converts the image to grayscale (black and white) using `img.convert("L")`.
    - Saves the black and white image with `bw_img.save`.
    - Prints a message indicating the successful conversion.

  - Exception handling is implemented to catch any errors during image processing.

```python
if __name__ == "__main__":
    input_directory = 'path/to/your/colored/images/'
    output_directory = 'path/to/save/black_and_white/images/'

    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"bw_{filename}")

            convert_to_black_and_white(input_path, output_path)
```

- **Main Execution:**
  - The `__main__` block checks if the script is being run directly.
  - It defines the input directory (containing colored images) and the output directory (where black and white images will be saved).
  - A loop iterates through files in the input directory with specified extensions.
  - For each eligible file, it constructs input and output paths and calls the `convert_to_black_and_white` function.
  
  ![Example Image](./../code(scripts)/Screenshot.png)
  
### Requirements:

1. **Pillow Library:**
   - You need to install the Pillow library. You can do this using the following command:
     ```bash
     pip install Pillow
     ```

2. **Images Directory:**
   - Ensure that you have a directory containing the colored images you want to convert to black and white.

3. **Output Directory:**
   - Define the directory where you want to save the black and white images.

4. **Python Environment:**
   - Make sure you have a Python environment set up on your machine.

### Usage:

- Run the script, and it will process colored images in the specified input directory, convert them to black and white, and save the results in the output directory.

Remember to adapt the paths according to your specific requirements.

Feel free to ask if you have any further questions or need additional clarification on any part!    

