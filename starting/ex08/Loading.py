loading = ""

def ft_tqdm(lst: range) -> None:
	loading = "█"
	for i in lst:
		yield i
		next(i)
		# print(i * 100 / 300, end='')
		# print(f"IS it integer?? : {(i * 100 / 333).is_integer()}")
		# if ((i * 100 / 333).is_integer()):
		# 	print(f"i is now {i}% out of 333")
		# 	loading += "█"
		# else:
		# 	print("Not a percentage")

# isinstance(result1, int)