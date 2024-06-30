import os
from PIL import Image

def convert_images_to_jpg(directory='.'):
    # Supported raw formats
    raw_formats = ('.raw', '.dng')
    
    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(raw_formats):
            raw_image_path = os.path.join(directory, filename)
            jpg_image_path = os.path.splitext(raw_image_path)[0] + '.jpg'
            
            try:
                with Image.open(raw_image_path) as img:
                    rgb_img = img.convert('RGB')
                    rgb_img.save(jpg_image_path, 'JPEG')
                    print(f"Converted {filename} to {jpg_image_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        print("No directory provided. Converting images in the current directory.")
        convert_images_to_jpg()
        print("Conversion complete")
