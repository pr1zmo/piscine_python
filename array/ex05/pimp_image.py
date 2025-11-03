import numpy as np
from PIL import Image

def ft_invert(array) -> list:
	"""
	Inverts the colors of the image by subtracting each pixel value from 255.
	
	Args:
		array: RGB image as numpy array with shape (H, W, 3)
	
	Returns:
		Inverted image array
	"""
	array = array.copy()
	np.subtract(255, array, out=array, casting='unsafe')
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Invert.jpeg", png=b"best")
	return array

def ft_red(array) -> list:
	"""
	Applies a red filter by zeroing out the green and blue channels.
	
	Args:
		array: RGB image as numpy array with shape (H, W, 3)
	
	Returns:
		Red-filtered image array
	"""
	array = array.copy()
	array[..., 1] = 0   # G = 0
	array[..., 2] = 0   # B = 0
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Red.jpeg", png=b"best")
	return array

def ft_green(array) -> list:
	"""
	Applies a green filter by zeroing out the red and blue channels.
	
	Args:
		array: RGB image as numpy array with shape (H, W, 3)
	
	Returns:
		Green-filtered image array
	"""
	array = array.copy()
	array[..., 0] = 0   # R = 0
	array[..., 2] = 0   # B = 0
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Green.jpeg", png=b"best")
	return array

def ft_blue(array) -> list:
	"""
	Applies a blue filter by zeroing out the red and green channels.
	
	Args:
		array: RGB image as numpy array with shape (H, W, 3)
	
	Returns:
		Blue-filtered image array
	"""
	array = array.copy()
	array[..., 0] = 0   # R = 0
	array[..., 1] = 0   # G = 0
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Blue.jpeg", png=b"best")

def ft_grey(array) -> list:
	"""
	Converts the image to grayscale using weighted RGB values (luminosity method).
	Formula: Gray = 0.299*R + 0.587*G + 0.114*B
	
	Args:
		array: RGB image as numpy array with shape (H, W, 3)
	
	Returns:
		Grayscale image array with all channels equal
	"""
	array = array.copy()
	# Gray=0.299*R + 0.587*G + 0.114*B
	gray = (array[..., 0] * 0.299 + 
			array[..., 1] * 0.587 + 
			array[..., 2] * 0.114).astype('uint8')
	
	# Create RGB image where all channels = gray
	array[..., 0] = gray
	array[..., 1] = gray
	array[..., 2] = gray
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Grey.jpeg", png=b"best")
	return array