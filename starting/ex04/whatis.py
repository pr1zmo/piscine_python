import sys

if (len(sys.argv) > 2):
	raise AssertionError("more than one argument is provided")
elif (sys.argv[1].isdigit() == False):
	raise AssertionError("argument is not an integer")
else :
	if (int(sys.argv[1])%2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")

