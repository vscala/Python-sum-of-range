# Python quick sum(range(*args))
def srange(*args) -> int:
    """Sum over a range
	srange(stop) == sum(range(stop))
	srange(start, stop) == sum(range(start, stop))
	srange(start, stop, increment) == sum(range(start, stop, increment))
	
    Arguments:
    start -- starting value of sum (inclusive)
    stop -- stoppping value of sum (exclusive)
	increment -- increment between start and stop 
    """
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
	
	if increment != 1:
		range_offset = start % increment
		start -= range_offset
		stop -= range_offset
		solution_offset = -((stop - start) // -increment) * range_offset
		return solution_offset + increment * srange(start // increment, -(stop // -increment))
	
	if stop < 0:
		return -srange(-stop+1, -start+1)
	
	# Adaptation of https://en.wikipedia.org/wiki/Triangular_number
	return (stop * (stop - 1) - start * (start - 1)) >> 1

if __name__ == "__main__":
	for start in range(-100, 100):
		assert srange(start) == sum(range(start))
		for stop in range(-100, 100):
			assert srange(start, stop) == sum(range(start, stop))
	for i in range(-10, 10):
		for j in range(-10, 10):
			for k in range(-10, 10):
				if k:
					assert srange(i, j, k) == sum(range(i, j, k))
