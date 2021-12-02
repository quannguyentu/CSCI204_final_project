class MinHeap:

	def __init__(self, max_size):
		self._elements = []
		self._count = 0

	def insert(self, priority, value):
		assert self._count < self.capacity()
		"Cannot add to a full heap."
		# Add the new value to the end of the list.
		self._elements[self._count] = value
		self._count += 1
		#	Sift the new value up the tree.
		self._sift_up(self._count - 1)

	def _sift_up(self, index):
		# Find parent of index
		# Sift up based on order property of tree
		while index // 2 > 0:

			if self._elements[index] < self._elements[index // 2]:
				c = self._elements[index]
				self._elements[index] = self._elements[index // 2]
				self._elements[index // 2] = c

				index = index // 2

	def extract(self):
		assert self._count > 0
		"Cannot extract from an empty heap."
		value = self._elements[0]
		self._count -= 1
		self._elements[0] = self._elements[self._count]
		self._sift_down(0)

	def _sift_down(self, index):
		# We can do this to find left & right because it’s a complete tree
		# Sift down based on order property of tree
		pass

	def heap_sort(self, heap):
		pass