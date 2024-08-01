from PIL import Image
import os

root = './data/mirror_scene_5_alt/test'
img_dir = os.path.join(root, 'image')
depth_dir = os.path.join(root, 'depth_normalized')

def png2jpg_in_dir(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            png_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, filename.replace('.png', '.jpg'))
            img = Image.open(png_path)
            rgb_img = img.convert('RGB')
            rgb_img.save(jpg_path, 'JPEG')

png2jpg_in_dir(img_dir)
png2jpg_in_dir(depth_dir)