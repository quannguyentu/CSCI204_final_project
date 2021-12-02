# This File has been updated
# It has the fully working tree

from bridges.bridges import *
from bridges.avl_tree_element import *

YOUR_USER_ID = "qnt001"
YOUR_API_KEY = "1228515534002"


class AVLTree:

	def __init__(self):
		self.root = None

		# visualization
		self.bridges = Bridges(0, YOUR_USER_ID, YOUR_API_KEY)

	# The clean calling of Insert
	def insert(self, key, value):
		if self.root is not None:
			self.root = self._insert(key, value, self.root)
		else:
			self.root = Node(key, value)

	# Recursive calling of Insert
	def _insert(self, key, value, root):
		if root is None:
			root = Node(key, value)

		elif key < root.key:
			root.left = self._insert(key, value, root.left)

		elif key > root.key:
			root.right = self._insert(key, value, root.right)

		elif key == root.key:
			root.value += value

		# Sets the weight of the root node of the subtree
		root.weight = self.get_weight(root)

		# visualization
		root.balance_factor = root.weight

		if root.weight <= -2:
			if root.left is not None and root.left.weight <= -1:
				return self.rotation1(root)
			elif root.left.weight >= 1:
				return self.rotation2(root)

		elif root.weight >= 2:
			if root.right is not None and root.right.weight >= 1:
				return self.rotation3(root)
			elif root.right.weight <= -1:
				return self.rotation4(root)

		return root


	def rotation1(self, pivot):
		c = pivot.left
		pivot.left = c.right
		c.right = pivot
		return c


	def rotation2(self, pivot):
		pivot.left = self.rotation3(pivot.left)
		return self.rotation1(pivot)


	def rotation3(self, pivot):
		c = pivot.right
		pivot.right = c.left
		c.left = pivot
		return c


	def rotation4(self, pivot):
		pivot.right = self.rotation1(pivot.right)
		return self.rotation3(pivot)


	# Returns the weight for a specified node based on the differences is the hights of its children
	def get_weight(self, root):
		if root.left is None and root.right is None:
			return 0
		elif root.left is None:
			return self.get_height(root.right)
		elif root.right is None:
			return -1 * self.get_height(root.left)
		else:
			return self.get_height(root.right) - self.get_height(root.left)


	def get_height(self, root):
		if root.left is None and root.right is None:
			return 1
		elif root.left is None:
			return 1 + self.get_height(root.right)
		elif root.right is None:
			return 1 + self.get_height(root.left)
		else:
			return 1 + max(self.get_height(root.left), self.get_height(root.right))

	def visualize(self):
		self.bridges.set_data_structure(self.root)
		self.bridges.visualize()



###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Node(AVLTreeElement):

	def __init__(self, key, value):
		super().__init__(key, value)
		self.value = value
		# self.right = None
		# self.left = None
		self.height = 0
		self.label = value

	def print(self):
		""" Print out the tree rooted at this node."""
		lines = []
		strings = []
		self.print_nodes(lines, strings)
		st = ""
		for string in strings:
			st = st + string
		print(st)

	def print_nodes(self, lines, strings):
		""" Helper function for print(). """
		level = len(lines)
		if self.right != None:
			lines.append(False)
			self.print_lines(lines, strings, "\n")
			self.right.print_nodes(lines, strings)
			lines.pop(level)
		else:
			self.print_lines(lines, strings, "\n")

		if level > 0:
			old = lines.pop(level - 1)
			self.print_lines(lines, strings, " +--")
			lines.append(not old)
		strings.append(str(self.key) + "\n")

		if self.left != None:
			lines.append(True)
			self.left.print_nodes(lines, strings)
			self.print_lines(lines, strings, "\n")
			lines.pop(level)
		else:
			self.print_lines(lines, strings, "\n")

	def print_lines(self, lines, strings, suffix):
		""" Helper function for print(). """
		for line in lines:
			if line:
				strings.append(" | ")
			else:
				strings.append("   ")
		strings.append(suffix)
