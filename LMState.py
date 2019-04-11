class LMState:
	def __init__(self, width, height, color = Color(255, 255, 255)):
		self.width = width
		self.height = height
		self.colorMatrix = list(width * height)

		for i in range(0, len(self.colorMatrix)):
			self.colorMatrix[i] = color