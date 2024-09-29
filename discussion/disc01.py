def race(x, y):
	"""The tortoise always walks x feet per minute, while the hare repeatedly
	runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
	many minutes pass until the tortoise first catches up to the hare.
	
	>>> race(5, 7) # After 7 minutes, both have gone 35 steps
	7
	>>> race(2, 4) # After 10 minutes, both have gone 20 steps
	10
	"""
	assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
	tortoise = 0
	minute = 0
	hare = 0
	while True:
		minute += 1
		if minute <= 11 and minute >= 6:
			tortoise += x
		else:
			tortoise += x
			hare += y
		if tortoise == hare:
			return minute

def fizzbuzz(n):
	"""
	>>> result = fizzbuzz(16)
	1
	2
	fizz
	4
	buzz
	fizz
	7
	8
	fizz
	buzz
	11
	fizz
	13
	14
	fizzbuzz
	16
	>>> print(result)
	None
	"""
	i = 1
	while i <= n:
		if i % 3 == 0 and i % 5 == 0:
			print("fizzbuzz")
		elif i % 3 == 0:
			print("fizz")
		elif i % 5 == 0:
			print("buzz")
		else:
			print(i)
		i += 1

def is_prime(n):
	"""
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
	>>> is_prime(1) # one is not a prime number!!
	False
	"""
	if n == 1:
		return False
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i += 1
	return True

def unique_digits(n):
	"""Return the number of unique digits in positive integer n.
	>>> unique_digits(8675309) # All are unique
	7
	>>> unique_digits(13173131) # 1, 3, and 7
	3
	>>> unique_digits(101) # 0 and 1
	2
	"""
	total = 0
	temp = 0
	while n >= 10:
		last_digit = n % 10
		n = n // 10
		if not has_digit(temp, last_digit):
			total += 1
			temp = temp * 10 + last_digit
	if not has_digit(temp, n):
		total += 1
	return total


def has_digit(n, k):
	if n < 10 and n != k:
		return False
	elif n < 10 and n == k:
		return True
	else:
		if n % 10 == k:
			return True
		else:
			return has_digit(n // 10, k)