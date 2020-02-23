class MovingAverage:
	"""
	Use a array to store the numbers used for calculations over the last _size numbers,
	Every time when next() method gets called, append the value to the list and add it to sum.
	If times the next() method gets called have been over the given size,
	then minus first value in the list from sum and remove it from the list,
	and return sum / average / size.

	Attributes
	----------
	   _size : int
			The window size
		_array : array
			The array used to save the last _size given numbers in the stream.
		_sum : float
			Sum of the array numbers
	Methods
	-------
	__init__
	next(self, val)
	"""
	def __init__(self, size):
		"""
		Constructor for moving average/sum of numbers in  a stream with limited window with size _size

		Parameters
		----------
			size : int
			The window size for the calculated sum/average.

		Returns
		-------
			The sum or average of the current last _size numbers
		"""
		self._size = size
		self._array = []
		self._sum = 0

	def next(self, val):
		"""
		Parameters
		----------
			val : float
			next value to insert the array with size _size.
		"""
		self._sum += val
		self._array.append(val)
		if len(self._array) > self._size:
			self._sum -= self._array.pop(0)

	def sum(self):
		"""
		return _sum attribute
		Returns
		-------
			The sum of the current last _size numbers
		"""
		return self._sum

	def average(self):
		"""
		calculate the average(limit to only two decimal points) of the last _size numbers.
		Returns
		-------
			The average of the current last _size numbers
		"""
		return  round(self. _sum / len(self._array), 2)
