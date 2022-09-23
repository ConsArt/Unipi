"""
	This program takes a 2d list of 0's
	& 1's (4 at each row) & returns the
	number of tic-tac-toe's found in the list.
"""

"""
	{ PYTHON PSEUDOCODE }

	1) Initialize variables:
		tic_tac_0, tic_tac_1 = (0, 0)
		
	2) General data:

		"" GIVEN ""
			A tic-tac-toe occurs when 3 identical numbers
			meets each other horizontally, vertically or
			diagonally. Hence given lst = [ 
											[1, 0, 0, 0]
											[0, 1, 1, 0]
											[0, 0, 0, 0]
											[0, 1, 1, 1]
														 ]
			tic_tac_0 = 5 ( 3 horizontally, 2 vertically )
			tic_tac_1 = 1 ( horizontally )

	3) Show output:
		print tic-tac-toe's of 0 & 1
"""

#                                                  *** CODE STARTS HERE ***

# Necessary imports
import random as rd

"""
	Returns a tuple containing the 
	tic-tac-toe counters of 0 & 1.
"""
def tril( lst ):

	# Initialize counters
	count_tic_tac_0, count_tic_tac_1 = (0, 0)

	""" CHECK DIAGONALLY """
	for row in range( len(lst)-2 ):

		cur_table = list()
		for r in range( row, row+3 ):
			cur_table.append( lst[r] )

		# Declare current split tables
		tic_tac_toe_1, tic_tac_toe_2 = split_to_tables( cur_table )

		# Diagonal tic-tac-toe results
		res_first_table = check_diagonally( tic_tac_toe_1 )
		res_second_table = check_diagonally( tic_tac_toe_2 )

		# Update counters
		count_tic_tac_0 += res_first_table[0] + res_second_table[0]
		count_tic_tac_1 += res_first_table[1] + res_second_table[1]

	""" CHECK HORIZONTALLY """
	for row in range( len(lst) ):

		for t in range(2):

			item_to_check = lst[row][t]
			exists = True

			for k in range(t+1, t+3):

				if lst[row][k] != item_to_check:
					exists = False
					break

			# If a tic-tac-toe exists
			if exists:
				# Increment the right counter
				if item_to_check == 0:
					count_tic_tac_0 += 1
				else:
					count_tic_tac_1 += 1

	""" CHECK VERTICALLY """
	for col in range(4):

		for row in range( len(lst)-2 ):

			item_to_check = lst[row][col]
			exists = True

			for k in range(row+1, row+3):

				if lst[k][col] != item_to_check:
					exists = False
					break

			if exists:
				if item_to_check == 0:
					count_tic_tac_0 += 1
				else:
					count_tic_tac_1 += 1

	return count_tic_tac_0, count_tic_tac_1

"""
	This function splits the given table
	in two 3x3 consecutive tables.
"""
def split_to_tables( array ):
	return [ row[:3] for row in array ], [ row[1:] for row in array ]

# Returns diagonal tic-tac-toe's
def check_diagonally( array ):

	# Initialize counters
	tic_tac_0, tic_tac_1 = (0, 0)

	""" Main diagonal """
	item_to_check = array[0][0]
	exists = True

	for k in range( 1, len(array) ):

		if array[k][k] != item_to_check:
			exists = False
			break

	if exists:
		if item_to_check == 0:
			tic_tac_0 += 1
		else:
			tic_tac_1 += 1

	""" Secondary diagonal """
	item_to_check = array[0][2]
	exists = True

	for k in range( 1, len(array) ):

		if array[k][2-k] != item_to_check:
			exists = False
			break

	if exists:
		if item_to_check == 0:
			tic_tac_0 += 1
		else:
			tic_tac_1 += 1

	return tic_tac_0, tic_tac_1

# Function to show the table
def show_table():

	# Create rows
	rows = rd.randrange(3, 9)
	# Create table
	for r in range(rows):
		table.append( list( rd.randrange(0, 2) for _ in range(4) ) )

	# Show indented table
	for row in table:
		print( "{}".format( row ) )

# Function to show the results
def results():

	# Unpack counters
	tril_0, tril_1 = tril( table )

	# Print tic-tac-toe's
	print( f"\nO's tic-tac-toe's: {tril_0}"
	       f"\n1's tic-tac-toe's: {tril_1}" )

""" INITIALIZE CONTENT """
table = list()
show_table()

""" SHOW RESULTS """
results()