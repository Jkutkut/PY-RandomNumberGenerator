from classes.random import RandomNumber

class Test:

	MAX_TESTS=1000
	
	@staticmethod
	def randomNumberTest(r: RandomNumber):
		numbers = [i for i in range(r.mini, r.maxi) if i % r.mult == 0 and (r.even and i % 2 == 0 or i % 2 == 1)];
		print("Numbers to generate:")
		print(numbers)
		
		i = 0
		while i < Test.MAX_TESTS and len(numbers) > 0:
			list(filter((r.getRandom()).__ne__, numbers))
			i += 1
		if len(numbers) != 0:
			print("Test %r %d %d %d KO" % (r.even, r.mult, r.mini, r.maxi))
			print("Remaining numbers:")
			print(numbers)
		else:
			print("Test %r %d %d %d OK" % (r.even, r.mult, r.mini, r.maxi))


if __name__ == "__main__":
	r = RandomNumber(even = False, mult = 5, mini = 0, maxi = 200)

	Test.randomNumberTest(r)
