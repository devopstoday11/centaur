import sys

# def check_axis_swap(axis):
# 	if axis == 'positive':
# 		axis = 'negative'
# 	else: 
# 		axis = 'positive'
# 	return axis

#start MAX/MIN tracking when passes 16k
axis = 'negative'
swap = 0
min = -50000
min_sec = 0
max = 50000
max_sec = 0

for line in sys.stdin:
	split = line.rstrip().split(' ')

	z = float(split[3])


	# walk check
	# positive
	if (z <= 16384.0) and (z > 8192):
		# check_axis_swap(axis)
		if axis == 'negative':
			axis = 'positive'
			swap = True
		else: 
			swap = False

		if z > min:
			min = z
			min_sec = float(split[0])

		# print 'positive'

		if swap == True:
			# print min
			print('%f %d %d' % (min_sec, min, 2))
			min = -50000
			min_sec = 0

	elif (z > 16384.0) and (z < 24576):
		# check_axis_swap(axis)
		if axis == 'positive':
			axis = 'negative'
			swap = True
		else: 
			swap = False
		if z < max:
			max = z
			max_sec = float(split[0])

		# print 'negative'

		if swap == True:
			# print max
			print('%f %d %d' % (max_sec, max, 2))
			max = 50000
			max_sec = 0

	else:
		print('%s %s %d' % (split[0], split[3], 0))









# print walking


# # walk= 0 trot= 1 canter=2
# current = 0
# current_sec = 0
# first_line = True
# base_time = 0.0

# walking = 0
# troting = 0
# cantering = 0

# for line in sys.stdin:
# 	split = line.rstrip().split(' ')
# 	# print float(split[0])

# 	if first_line == True:
# 		last_z = float(split[3])
# 		# prev_sec = float(split[0])
# 		last_time = float(split[0])
# 		first_line = False

# 	# current_z = float(split[3])
# 	# current_sec = float(split[0])

	# if negative g force skip
	# if current_z < 16384.0:
	# if current_z > 16384.0:
	# 	print "first if"
	# 	prev_z = current
	# 	prev_sec = current_sec
	# 	base_time = current_sec
	# 	continue

	# # check that number is still going up
	# if prev_z < current_z:
	# 	print "second if"
	# 	prev_z = current_z
	# 	prev_sec = current_sec
	# 	continue


	# # get top value by checking if the value has started to fall
	# # if at this point our current is SMALLER than prev, prev is top of the motion curve
	# if prev_z > 8192:
	# 	print "third if"
	# 	motion = 0
	# 	# how much time has passed 
	# 	walking += (base_time - current_sec)
