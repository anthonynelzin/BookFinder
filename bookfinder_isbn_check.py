import re

def isbn_clean(isbn):
	# Remove hyphens from the provided ISBN
	isbn_cleaned = re.sub("\W", "", isbn)
	return isbn_cleaned
	
def isbn_check(isbn):
	# Check the length of the provided ISBN
	isbn = isbn_clean(isbn)
	
	if len(isbn) == 10:
		return isbn_10_check(isbn)
	elif len(isbn) == 13:
		return isbn_13_check(isbn)
	else:
		raise ValueError("You didn't enter a valid ISBN.")
		
def isbn_10_check(isbn):
	# Check the validity of the provided ISBN-10
	# Each of the first nine numbers is multiplied by its weight ranging from 10 to 2.
	# Those nine products are summed together.
	# We take the remainder of this sum divided by 11.
	# The check number is 11 minus the remainder.
	# Is the check number is 10, we convert it to X.
	# Is the check number is 11, we convert it to 0.
	numbers = list(isbn)
	sum = 0
	factor = 10
	
	for number in numbers:
		sum += factor*int(number)
		factor -= 1
	check = 11 - (sum%11)
	
	if check == 10:
		return "X"
	
	if check == 11:
		return "0"
	
	if numbers[-1] == check:
		print("The ISBN " + isbn + "is a valid ISBN-10.")
		return isbn
	else:
		raise ValueError("The ISBN " + isbn + "is not a valid ISBN-10.")
	
def isbn_13_check(isbn):
	# Check the validity of the provided ISBN-13
	# Odd-positioned numbers are multiplied by 1, even ones by 3.
	# Those twelve products are summed together.
	# We take the remainder of this sum divided by 10.
	# The check number is 10 minus the remainder.
	# Is the check number is 10, we convert it to 0.
	numbers = list(isbn)
	sum = 0
	position = 0
	
	for number in numbers:
		if (position%2 == 0):
			sum += int(number)
		else:
			sum += 3*int(number)
		position += 1
	
	check = 10 - (sum%10)
	
	if check == 10:
		return "0"
		
	if numbers[-1] == check:
		print("The ISBN " + isbn + "is a valid ISBN-13.")
		return isbn
	else:
		raise ValueError("The ISBN " + isbn + "is not a valid ISBN-13.")
	
def main():
	isbn_check(isbn)
	
if __name__ == '__main__':
	main()