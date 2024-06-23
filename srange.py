# Python quick sum(range(*args))
def srange(*args) -> int:
    """
    Sum over a range.

    srange(stop) == sum(range(stop))
    srange(start, stop) == sum(range(start, stop))
    srange(start, stop, increment) == sum(range(start, stop, increment))

    Arguments:
    start -- starting value of sum (inclusive), defaults to 0
    stop -- stopping value of sum (exclusive)
    increment -- increment between start and stop, defaults to 1

    Returns:
    Sum of the range.
    """
    if len(args) > 3:
        raise TypeError(f"srange expected at most 3 arguments, got {len(args)}")
    if len(args) == 0:
        raise TypeError("srange expected at least 1 argument, got 0")

    if len(args) == 1:
        start, stop, increment = 0, args[0], 1
    elif len(args) == 2:
        start, stop, increment = args + (1,)
    else:
        start, stop, increment = args

    if increment == 0:
        raise ValueError("srange argument 3 must not be zero")
    if any(isinstance(arg, float) for arg in args):
        raise TypeError("'float' object cannot be interpreted as an integer")

    if (increment > 0 and start >= stop) or (increment < 0 and start <= stop):
        return 0

    def arithmetic_sum(number_of_terms, first_term, common_difference):
        last_term = first_term + (number_of_terms - 1) * common_difference
        return number_of_terms * (first_term + last_term) // 2

    adjusted_stop = stop - (1 if increment > 0 else -1)
    number_of_terms = (adjusted_stop - start) // increment + 1

    return arithmetic_sum(number_of_terms, start, increment)
