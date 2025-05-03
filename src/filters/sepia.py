from PIL import Image
import numpy as np

def apply_sepia(image):
    """
    Application of sepia filter on an image using NumPy for better performance.
    
    Args:
        image: PIL Image object in RGB mode
        
    Returns:
        PIL Image object with sepia effect applied
    """
    if image.mode != "RGB":
        raise ValueError(f"Sepia filter only supports RGB mode images, got {image.mode}")
    
    # Convert to numpy array for faster processing
    img_array = np.array(image)
    
    # Apply sepia transformation using matrix operations
    sepia_matrix = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    
    # Reshape to apply transformation to all pixels at once
    flat_img = img_array.reshape(-1, 3)
    sepia_flat = np.matmul(flat_img, sepia_matrix.T)
    
    # Reshape back to original dimensions and clip values to 0-255
    sepia_array = np.clip(sepia_flat.reshape(img_array.shape), 0, 255).astype(np.uint8)
    
    # Convert back to PIL image
    return Image.fromarray(sepia_array)