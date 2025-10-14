import sys

def handle_input(inp : any) -> any:
	word_count = 0
	upper = 0
	lower = 0
	punc = 0
	space = 0
	digits = 0
	for i in inp:
		if (i.isdigit()):
			digits += 1
		elif (i.islower()):
			lower += 1
		elif (i.isupper()):
			upper += 1
		elif (i == ' '):
			space += 1
		else:
			punc += 1
		word_count+=1
	print(f"The text contains {word_count} characters: ")
	print(f"{upper} upper letters")
	print(f"{lower} lower letters")
	print(f"{punc} punctuation marks")
	print(f"{space} spaces")
	print(f"{digits} digits")

def building() -> any:
	"""
	Read until EOF error
	Then count the give characters to match the output
	exit after reading all
	"""
	if (len(sys.argv) > 1):
		inp = sys.argv[1]
	else:
		inp = ""
	print("Enter text (press Ctrl+D when done):")
	try:
		inp = sys.stdin.read()  # Reads until EOF
	except KeyboardInterrupt:
		print("\nInput interrupted.")
		return
	if (len(sys.argv) > 2):
		raise AssertionError("Only takes one argument")
	return handle_input(inp)
	