def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	res = []
	if (len(height) != len(weight)):
		print("list sizes don't match")
		return NULL
	i = 0;
	while (i < len(height)):
		res.append(weight[i]/pow(height[i], 2))
		i += 1
	return res
	
	

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	res = []
	for i in bmi:
		if (i < limit):
			res.append(False)
		else:
			res.append(True)
	return res