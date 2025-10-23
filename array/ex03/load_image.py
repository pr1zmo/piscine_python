import numpy as np
from PIL import Image
import os

_ext = [".png", ".jpg", ".jpeg"]

def check_file(path: str) -> bool:
	return os.path.isfile(path) and path.lower().endswith(tuple(_ext))

def ft_load(path: str) -> np.ndarray:
	if not check_file(path):
		raise ValueError("Error opening image")

	with Image.open(path) as img:
		rgb = img.convert("RGB")
		arr = np.asarray(rgb)  # (H, W, 3)
		print(f"The shape of the image is: {arr.shape}")

		# 400x400 crop starting at (400, 400)
		x0, y0, size = 400, 200, 400
		w, h = rgb.size  # (W, H)
		x1, y1 = x0 + size, y0 + size
		print(w, h)
		print(x1, y1)
		if x1 > w or y1 > h:
			raise ValueError(
					f"Image too small for a {size}x{size} crop starting at ({x0},{y0}). "
					f"Image size is {w}x{h}."
			)

		zoomed = rgb.crop((x0, y0, x1, y1))
		zoomed.show()
		zarr = np.asarray(zoomed)  # (400, 400, 3)
		print(f"New shape after slicing: {zarr.shape}")
		print(zarr)

	# Return whichever you need; original array here:
	return arr