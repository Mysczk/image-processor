import os

def save_image(image, output_path):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        image.save(output_path)
        print(f"File saved: {output_path}")
    except Exception as e:
        raise IOError(f"Error while saving file: {e}")
