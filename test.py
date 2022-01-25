from classes.random import RandomNumber

class Test:

	MAX_TESTS=1000
	
	@staticmethod
	def randomNumberTest(r: RandomNumber):
		numbers = [i for i in range(r.mini, r.maxi) if any([i % j == 0 for j in r.mult])];
		print("Numbers to generate:")
		print(numbers)
		
		i = 0
		while i < Test.MAX_TESTS and len(numbers) > 0:
			list(filter((r.getRandom()).__ne__, numbers))
			i += 1
		print("Test %r %d %d %d " % (r.even, r.mult, r.mini, r.maxi), end = "")
		if len(numbers) != 0:
			Test.print_fail("KO")
			print("Remaining numbers:")
			print(numbers)
		else:
			print("OK")

	@staticmethod
	def print_fail(message, end = '\n'):
		print('\x1b[1;31m' + message.strip() + '\x1b[0m', end = end)

	@staticmethod
	def print_pass(message, end = '\n'):
		sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

	@staticmethod
	def print_warn(message, end = '\n'):
		sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

	@staticmethod
	def print_info(message, end = '\n'):
		sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

	@staticmethod
	def print_bold(message, end = '\n'):
		sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)


if __name__ == "__main__":
	r = RandomNumber([5], mini = 0, maxi = 200)

	Test.randomNumberTest(r)
