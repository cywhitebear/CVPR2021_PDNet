import os
import numpy as np
from PIL import Image

root = './data/mirror_scene_5_alt/test'
input_dir = os.path.join(root, 'depth')
output_dir = os.path.join(root, 'depth_normalized')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def normalize_and_resize_image(image_path, output_path, target_size):
    
    image = Image.open(image_path)
    image_np = np.array(image)
    
    image_np = ((image_np - image_np.min()) / float(image_np.max() - image_np.min()) + 1e-7) * 255
    
    image_normalized = Image.fromarray(image_np.astype(np.uint8))
    image_resized = image_normalized.resize(target_size, Image.Resampling.LANCZOS)
    image_resized.save(output_path)

target_size = (1920, 1440)

for filename in os.listdir(input_dir):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        normalize_and_resize_image(input_path, output_path, target_size)
        

print("Processing complete.")