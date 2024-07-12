import os
from PIL import Image
import argparse

def convert_images_to_jpg(directory='.'):
    """
    This function converts all raw format images in a directory to JPG format.
    If no directory is passed it defaults to current directory.
    
    Args:
        directory (str, optional): The directory containing the raw format images. Defaults to '.'.
    """
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
    
    parser = argparse.ArgumentParser(description="Convert raw images to JPG format.")
    parser.add_argument("-d", "--directory", help="Specify the directory containing raw images.")
    args = parser.parse_args()
    
    if args.directory:
        convert_images_to_jpg(args.directory)
        print("Conversion complete in the specified directory.")
    else:
        print("No directory provided. Converting images in the current directory.")
        convert_images_to_jpg()
        print("Conversion complete in the current directory.")