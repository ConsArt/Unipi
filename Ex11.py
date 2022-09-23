"""
	This program takes a 2d string list of
	"s" & "o" and finds all of "sos"
	occurrences in the list.
"""

"""
	{ PYTHON PSEUDOCODE }

	1) Initialize variables:
		count_sos = 0
		
	2) General data:

		"" GIVEN ""
			When the lst[element] is 'o' then skip 
			to -> lst[element+1], because of 
			the 'sos' syntax.
			
	3) Show output:
		print sos counter
"""

#                                                  *** CODE STARTS HERE ***

# Necessary imports
import random as rd

# Declare global SOS
SOS = "sos"

"""
	Returns a counter containing the 
	"sos" encounters in the list lst.
"""
def sos( lst ):

	# Initialize counters
	count_sos = 0
	_split_results = 0

	""" CHECK DIAGONALLY """
	for row in range( len(lst)-2 ):

		cur_table = list()
		for r in range( row, row+3 ):
			cur_table.append( lst[r] )

		# Declare current split tables
		_sos_table1, _sos_table2, _sos_table3, _sos_table4 = split_to_tables( cur_table )

		# Diagonal sos results
		_split_results = check_diagonally( _sos_table1 ) + check_diagonally( _sos_table2 ) +\
		                 check_diagonally( _sos_table3 ) + check_diagonally( _sos_table4 )

		# Update "sos" counter
		count_sos += _split_results

	""" CHECK HORIZONTALLY """
	for row in range( len(lst) ):

		for col in range( len(lst[row])-2 ):

			# If the current item starts,
			# with an "s", check for "sos"
			if lst[row][col] == "s":

				_sos = "s"
				for k in range(col+1, col+3):
					_sos += lst[row][k]

				if _sos == SOS:
					count_sos += 1

			else:
				# Continue with the next element
				continue

	""" CHECK VERTICALLY """
	for col in range(6):

		for row in range( len(lst)-2 ):

			# If the current item starts,
			# with an "s", check for "sos"
			if lst[row][col] == "s":

				_sos = "s"
				for k in range( row+1, row+3 ):
					_sos += lst[k][col]

				if _sos == SOS:
					count_sos += 1

			else:
				# Continue with the next element
				continue

	return count_sos

"""
	This function splits the given table
	in four 3x3 consecutive tables.
"""
def split_to_tables( array ):
	return [ row[ :3 ] for row in array ], [ row[ 1:4 ] for row in array ],\
	       [ row[ 2:5 ] for row in array ], [ row[ 3: ] for row in array ]

# Returns diagonal 'sos'
def check_diagonally( array ):

	# Initialize counter
	count_sos = 0

	# If the 1st element starts with "s"
	if array[0][0] == "s":

		""" Main diagonal """
		_sos = "s"

		for k in range( 1, len(array) ):
			_sos += array[k][k]

		if _sos == SOS:
			count_sos += 1

	# If the last element starts with "s"
	if array[0][2] == "s":

		""" Secondary diagonal """
		_sos = "s"

		for k in range( 1, len(array) ):
			_sos += array[k][2-k]

		if _sos == SOS:
			count_sos += 1

	return count_sos

# Function to show the table
def show_table():

	# Declare sample array
	sample = [ "s", "o" ]

	# Create rows
	rows = rd.randrange( 3, 8 )
	# Create table
	for r in range( rows ):
		table.append( list( sample[ rd.randrange( 2 ) ] for _ in range(6) ) )

	# Show indented table
	for row in table:
		print( "{}".format( row ) )

# Function to show the results
def results():

	# Unpack counter
	_sos = sos( table )

	# Print occurrences of sos
	print( f"\nOccurrences of \"sos\": {_sos}" )

""" INITIALIZE CONTENT """
table = list()
show_table()

""" SHOW RESULTS """
results()