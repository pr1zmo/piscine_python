import numpy as np
from PIL import Image

def ft_invert(array) -> list:
	array = array.copy()
	np.subtract(255, array, out=array, casting='unsafe')
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Invert.jpeg", png=b"best")
	return array

def ft_red(array) -> list:
	array = array.copy()
	array[..., 1] = 0   # G = 0
	array[..., 2] = 0   # B = 0
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Red.jpeg", png=b"best")
	return array

def ft_green(array) -> list:
	array = array.copy()
	array[..., 0] = 0   # R = 0
	array[..., 2] = 0   # B = 0
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Green.jpeg", png=b"best")
	return array

def ft_blue(array) -> list:
	array = array.copy()
	array[..., 0] = 0   # R = 0
	array[..., 1] = 0   # G = 0
	img = Image.fromarray(array.astype('uint8'))
	img.show()
	img.save("Blue.jpeg", png=b"best")

def ft_grey(array) -> list:
	array = array.copy()
	# Gray=0.299*R + 0.587*G + 0.114*B
	np.multiply(array[..., 0:], 0.299, out=array[..., 0:], casting='unsafe')
	np.multiply(array[..., 1:], 0.587, out=array[..., 1:], casting='unsafe')
	np.multiply(array[..., 2:], 0.114, out=array[..., 2:], casting='unsafe')
	img = Image.fromarray(array.astype('float64'))
	img.show()
	img.save("Grey.jpeg", png=b"best")