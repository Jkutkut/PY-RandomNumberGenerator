from random import randint

class RandomNumber:

	def __init__(self, mult: list, mini: int, maxi: int, odd: bool = False):
		self.mult = mult
		self.fprimos = RandomNumber.getFactoresPrimos(mult)
		self.mini = mini
		self.maxi = maxi
		self.odd = odd

	def getRandom(self):
		if self.odd:
			return self.getOddNumber()
		else:
			return self.getNumber()

	def getNumber(self):
		fp = 1
		for i in self.fprimos:
			fp *= i
		return randint(self.mini // fp, self.maxi // fp) * fp
	
	def getOddNumber(self):
		return 0

	@staticmethod
	def getFactoresPrimos(mult):
		fprimos = set()
		for i in mult:
			fprimos.update(RandomNumber.factoresPrimos(i))
		return fprimos
		
	@staticmethod
	def factoresPrimos(n: int):
		f = []
		i = 2
		while n > 1:
			if n % i == 0:
				f.append(i)
				while n % i == 0:
					n /= i
			else:
				i += 1;
		return f



