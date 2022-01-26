class RandomNumber:

	def __init__(self, mult: list, mini: int, maxi: int, odd: bool = False):
		self.mult = mult
		self.fprimos = self.getFactoresPrimos()
		self.mini = mini
		self.maxi = maxi

	def getRandom(self):
		if self.odd:
			return self.getOddNumber()
		else:
			return self.getNumber()

	def getNumber(self):
		return 0
	
	def getOddNumber(self):
		return 0

	def getFactoresPrimos(self):
		self.fprimos = set()
		for i in self.mult:
			self.fprimos.update(RandomNumber.factoresPrimos(i))
		print(self.fprimos)
		
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



