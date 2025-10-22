from PIL import Image
import os
import numpy as np

_ext = [".png", ".jpg", ".jpeg"]

def check_file(path) -> bool:
   return os.path.exists(path) and path.lower().endswith(tuple(_ext))

def ft_load(path: str) -> np.ndarray:
   if not check_file(path):
      raise ValueError("Error opening image")
   with Image.open(path) as img:
      arr = np.asarray(img.convert('RGB'))  # shape: (height, width, 3), dtype=uint8
   return arr

print(ft_load("at.jpg"))