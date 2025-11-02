import numpy as np
from PIL import Image
import os

_ext = [".png", ".jpg", ".jpeg"]

def check_file(path) -> bool:
	return os.path.exists(path) and path.lower().endswith(tuple(_ext))

def ft_load(path: str) -> np.ndarray:
	if not check_file(path):
		raise ValueError("Error opening image")
	with Image.open(path) as img:
		print("The shape of the image is: ", end='')
		print(img.size)
		arr = np.asarray(img.convert('RGB'))  # shape: (height, width, 3), dtype=uint8
	return arr