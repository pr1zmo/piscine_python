def all_thing_is_obj(object : any) -> int:
	if (type(object) == str):
		print(object + " is in the kitchen", end=" ")
	else:
		res = str(type(object))
		res = res.replace("<class '", "")
		res = res.replace("'>", "")
		print(res + ": ", end="")
	print(type(object))