"""
	This program takes a txt ASCII file,
	and processes the file's input, to
	create its unique hash value.
"""

#                                                   *** CODE STARTS HERE ***

# Necessary imports
from string import punctuation, whitespace

""" FUNCTION """
def FileHash( fl ):

	""" INITIALIZE VARIABLES """

	# Will contain the final 32char string
	_hashed_list = list()
	# Will contain the sum of each
	# 16range_th vector in _hashed_list
	sum = list( 0 for _ in range(16) )
	# Experimentation string
	_file = ""

	""" PROCESS FILE """
	with open( file = fl, mode = 'r', encoding = 'UTF-8') as fl:

		# Convert file's content to lowercase
		fl = fl.read().lower()

		# Remove whitespaces & punctuation
		for line in fl:
			_file += "".join( filter( lambda c: c not in whitespace + punctuation, line ) )

		# Declare hashed list, by splitting
		# _file string into parts of 16 chars
		_file = [ _file[ c:c+16 ] for c in range( 0, len(_file), 16 ) ]

		# Find the ASCII conjugate foreach _file[i][j]
		for element in _file:
			_hashed_list.append( [ ord(item) for item in element ] )

		# Add each _hashed_list[i][j] to
		# the jth position of sum[]
		for vector in range( len(_hashed_list) ):
			for el in range( len(_hashed_list[vector]) ):
				sum[el] += _hashed_list[vector][el]

		# Divide each item by 256 to get
		# the final hashed list
		_hashed_list = list( map( lambda item: item % 256, sum ) )

		# Convert each number to its hexadecimal conjugate
		_hashed_list = list( map( lambda item: hex(item), _hashed_list ) )

		# Remove 0x from each _hashed_list[i]
		_hashed_list = list( map( lambda item: item[2:], _hashed_list ) )

		# Split each _hashed_list[i] to create
		# the final value of _hashed_list
		_file = ""
		for char in range( len(_hashed_list) ):
			_file += _hashed_list[char]
		_hashed_list = _file

	return _hashed_list

""" RESULTS """
# Declare sample file
file = "sample2.txt"

# Print file's hash code
print( "Hash code of \"{}\": {}".format( file, FileHash(file) ) )