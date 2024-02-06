# Automation:
Before we start i would like to show you my work:

Here are some examples of what my code do:

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

 Let me explain the code step by step:

1. **Importing Necessary Modules:**
    ```python
    from PIL import Image
    import os
    import time
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    ```
   - `PIL`: This is the Python Imaging Library that provides the `Image` class for handling images.
   - `os`: This module provides a way to interact with the operating system, like working with file paths and directories.
   - `time`: This module is used for adding a short delay to the script.
   - `watchdog`: This library is used for monitoring file system events.

2. **Defining a FileSystemEventHandler:**
    ```python
    class ImageHandler(FileSystemEventHandler):
        def on_created(self, event):
            if event.is_directory:
                return
            input_path = event.src_path
            filename = os.path.basename(input_path)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                output_directory = 'Gray_Images'
                output_path = os.path.join(output_directory, f"bw_{filename}")
                convert_to_black_and_white(input_path, output_path)
    ```
   - This class inherits from `FileSystemEventHandler`, which provides methods for handling file system events.
   - The `on_created` method is called when a new file is created.
   - It checks if the event is related to a directory, and if not, it extracts the input file path and filename.
   - If the file has a supported image extension (JPEG or PNG), it defines the output path for the black and white version and calls `convert_to_black_and_white`.

3. **Defining the Conversion Function:**
    ```python
    def convert_to_black_and_white(input_path, output_path):
        try:
            img = Image.open(input_path)
            bw_img = img.convert("L")
            bw_img.save(output_path)
            print(f"Image converted to black and white: {output_path}")
        except Exception as e:
            print(f"Error processing {input_path}: {e}")
    ```
   - This function takes an input image file path and an output file path.
   - It opens the input image, converts it to black and white using the `"L"` mode, and saves the result.
   - Any exceptions during this process are caught, and an error message is printed.

4. **Main Execution Block:**
    ```python
    if __name__ == "__main__":
        input_directory = 'Colored_Images'
        output_directory = 'Gray_Images'

        os.makedirs(output_directory, exist_ok=True)

        event_handler = ImageHandler()
        observer = Observer()
        observer.schedule(event_handler, path=input_directory, recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    ```
   - The main block of the script sets up the input and output directories.
   - It creates the `ImageHandler` and `Observer` instances.
   - The observer is configured to watch the `input_directory` for file creation events (recursive=False means it won't look into subdirectories).
   - The observer is started, and the script enters a loop where it sleeps for 1 second, allowing it to continuously monitor for new files.
   - If the script is interrupted by a keyboard interrupt (Ctrl+C), it stops the observer and joins the thread.

In summary, this script continuously monitors the `Colored_Images` directory for new image files and converts them to black and white, saving the results in the `Gray_Images` directory. The monitoring is done using the `watchdog` library, and the script runs until manually interrupted.
