import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""
	Calculate Body Mass Index (BMI) for given heights and weights.
	Args:
		height (list[int | float]): A list of heights in meters.
		weight (list[int | float]): A list of weights in kilograms.
	Returns:
		list[int | float]: A list of BMI values calculated as weight / height^2.
			Returns None if the input lists have different lengths.
	Example:
		>>> give_bmi([1.75, 1.80], [70, 80])
		[22.857142857142858, 24.691358024691358]
	"""
	# res = np.array(height, weight)
	if (len(height) != len(weight)):
		print("Wrong size")
		exit()
	res = np.array([height, weight])
	x = 0;
	fin = np.array([])
	while (x < len(height)):
		print(x)
		fin = np.append(fin, res[1][x] / (res[0][x] * res[0][x]))
		x += 1
	return fin


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""
	Apply a limit threshold to a list of BMI values.
	Args:
		bmi: A list of BMI values (integers or floats).
		limit: The threshold value to compare against.
	Returns:
		A list of boolean values where True indicates the BMI value
		is greater than or equal to the limit, False otherwise.
	"""
	res = []
	for i in bmi:
		if (i < limit):
			res.append(False)
		else:
			res.append(True)
	return res