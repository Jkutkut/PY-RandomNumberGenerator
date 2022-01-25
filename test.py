from classes.random import RandomNumber

class Test:

	@staticmethod
	def randomNumberTest(r: RandomNumber):
		print(r.getRandom())


if __name__ == "__main__":
	r = RandomNumber(even = False, mult = 5, mini = 0, maxi = 200)

	Test.randomNumberTest(r)
