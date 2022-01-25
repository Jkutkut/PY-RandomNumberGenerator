class RandomNumber:

	def __init__(self, mult: list, mini: int, maxi: int):
		self.mult = mult
		self.mini = mini
		self.maxi = maxi

	def getRandom(self):
		if self.even:
			return self.getEvenNumber()
		else:
			return self.getOddNumber()

	def getEvenNumber(self):
		return 0
	
	def getOddNumber(self):
		return 0




