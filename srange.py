# Python quick sum(range(*args))
def srange(*args) -> float:
	if len(args) > 3:
		raise TypeError(f'srange expected at most 3 arguments, got {len(args) + len(kwargs)}')
	if len(args) == 0:
		raise TypeError('srange expected at least 1 argument, got 0')
	
	start, stop, increment = 0, None, 1
	if len(args) == 1:
		stop = args[0]
	elif len(args) == 2:
		start, stop = args
	elif len(args) == 3:
		start, stop, increment = args
		if increment == 0:
			raise ValueError("srange argument 3 must not be zero")
	
	if start % 1 or stop % 1 or increment % 1: # should floating points be allowed?
		raise TypeError("'float' object cannot be interpreted as an integer")
	
	if start == stop:
		return 0
	if increment > 0 and start > stop:
		return 0
	if increment < 0 and start < stop:
		return 0
	
	if increment < 0:
		return srange(stop+1, start+1, -increment)
	if increment > 1: # TODO handle increments > 1
		# caclulate starting and stoppping points
		
		return None #increment * srange(start//increment, stop//increment) ???
	
	if stop < 0:
		return -srange(-stop+1, -start+1)
	
	# adaptation of https://en.wikipedia.org/wiki/Triangular_number
	return (stop * (stop - 1) - start * (start - 1)) >> 1
	
if __name__ == "__main__":
	for start in range(-100, 100):
		assert srange(start) == sum(range(start))
		for stop in range(-100, 100):
			assert srange(start, stop) == sum(range(start, stop))
	from datetime import datetime
	now = datetime.now()
	for start in range(-1000, 1000):
		srange(start)
		for stop in range(-1000, 1000):
			srange(start, stop)
	print(datetime.now() - now)
