import sys

NESTED_MORSE = {
	" ": "/ ",
	"A": ".- ",
	"B": "-... ",
	"C": "-.-. ",
	"D": "-.. ",
	"E": ". ",
	"F": "..-. ",
	"G": "--. ",
	"H": ".... ",
	"I": ".. ",
	"J": ".--- ",
	"K": "-.- ",
	"L": ".-.. ",
	"M": "-- ",
	"N": "-. ",
	"O": "--- ",
	"P": ".--. ",
	"Q": "--.- ",
	"R": ".-. ",
	"S": "... ",
	"T": "- ",
	"U": "..- ",
	"V": "...- ",
	"W": ".-- ",
	"X": "-..- ",
	"Y": "-.-- ",
	"Z": "--.. ",
	"0": "----- ",
	"1": ".---- ",
	"2": "..--- ",
	"3": "...-- ",
	"4": "....- ",
	"5": "..... ",
	"6": "-.... ",
	"7": "--... ",
	"8": "---.. ",
	"9": "----. "
}


def main(object: any) -> bool:
	if (len(object) != 2):
		raise AssertionError
	result = ""
	for i in object[1]:
		if ((not i.isalnum()) and (i != " ")):
			raise AssertionError
		a = NESTED_MORSE.get(i.upper())
		if (a is not None):
			result += a
	print(result)

if __name__ == "__main__":
	try:
		main(sys.argv)
	except AssertionError:
		print("the arguments are bad")

