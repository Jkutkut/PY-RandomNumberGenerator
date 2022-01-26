from classes.random import RandomNumber

class Test:

	MAX_TESTS=1000
	
	@staticmethod
	def randomNumberTest(rng: RandomNumber):
		numbers = [i for i in range(rng.mini, rng.maxi) if any([i % j == 0 for j in rng.mult])];
		print("Numbers to generate:", len(numbers))
		print(numbers)
		
		i = 0
		while i < Test.MAX_TESTS and len(numbers) > 0:
			r = rng.getRandom()
			if r in numbers:
				numbers.remove(r)
			i += 1
		print("Test %s %d %d %r " % (rng.mult, rng.mini, rng.maxi, rng.odd), end = "")
		if len(numbers) != 0:
			Test.print_fail("KO")
			print("Remaining numbers:")
			print(numbers)
		else:
			Test.print_pass("OK")

	@staticmethod
	def print_fail(message, end = '\n'):
		print('\x1b[1;31m' + message.strip() + '\x1b[0m', end = end)

	@staticmethod
	def print_pass(message, end = '\n'):
		print('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

	@staticmethod
	def print_warn(message, end = '\n'):
		sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

	@staticmethod
	def print_info(message, end = '\n'):
		print('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

	@staticmethod
	def print_bold(message, end = '\n'):
		print('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)


if __name__ == "__main__":
	r = RandomNumber(mult = [5], mini = 0, maxi = 200, odd = False)

	Test.randomNumberTest(r)
