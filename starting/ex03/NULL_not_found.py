def format_type(res: any) -> str:
	res = str(type(res))
	res = res.replace("<class '", "")
	res = res.replace("'>", " ")
	return res

def NULL_not_found(object: any) -> int:
	if (object is None):
		print(f"Nothing: " + format_type(object) + str(type(object)))
	elif (object is float("NaN")):
		print(f"Cheese: " + format_type(object) + str(type(object)))
	elif (object is False):
		print(f"Fake: {object} {type(object)}")
	elif (object == 0):
		print(f"Zero: {object} {type(object)}")
	elif (object == ""):
		print(f"Empty: {type(object)}")
	else:
		print("Type not Found")
	return 1