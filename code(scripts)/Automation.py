from PIL import Image
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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
