"""
	This program shows the number of primes
	in a given range n, from KINO web service.
"""

"""
	{ PYTHON PSEUDOCODE }

	1) Initialize variables:
		_count_primes = 0

	2) General data:

		"" GIVEN ""
			KINO statistics

		"" INSPECTION ""
			
			If there's a k such that number % k == 0
			-> number = l*k, k != {1,number}, then 
			number != a prime.

	3) Show output:
		print number of primes up to n
"""

#                                                   *** CODE STARTS HERE ***

# Necessary imports
import requests as rq
import math as mt

""" 
	This function returns the number of
	primes up to the given bound n.
"""
def primek( n ):

	# Initialize counter
	_count_primes = 1

	# Check for primes up to n
	for number in range(3, n+1):

		# Declare prime confirmation flag
		_isprime = True

		for k in range(2, mt.ceil( mt.sqrt(number) )+1 ):

			if number % k == 0:
				_isprime = False
				break

		# If number is prime,
		if _isprime:
			# Increment counter
			_count_primes += 1

	"""	
		If the n < 3 -> the only number
		is {2}( n >= 0 ), which is 
		the only prime up to 3
	"""
	return _count_primes

# Declare URL
base_url = "https://api.opap.gr/games/v1.0/1100/statistics?drawRange=1801"
# Get URLs information
response = rq.get(base_url)
# Get bound value from dictionary
limit = response.json()["data"][0]["value"]

# Show results
print( "Total primes up to {0}: {1}".format( limit, primek(limit) ) )
