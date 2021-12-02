from Tree import *
import csv
from MinHeap import *
import Beats_priority

class ChicagoCrimeFun:
	CRIME_DICTIONARY = {"HOMICIDE": 0, "ARSON": 1, "HUMAN TRAFFICKING": 2, "KIDNAPPING": 3, "WEAPONS VIOLATION": 4,
	                    "SEX OFFENSE": 5, "CRIM SEXUAL ASSAULT": 6, "ASSAULT": 7, "BATTERY": 8,
	                    "MOTOR VEHICLE THEFT": 9, "THEFT": 10, "BURGLARY": 11, "ROBBERY": 12,
	                    "INTERFERENCE WITH PUBLIC OFFICER": 13, "DECEPTIVE PRACTICE": 14, "NARCOTICS": 15,
	                    "OTHER NARCOTIC VIOLATION": 16, "CRIMINAL DAMAGE": 17, "CRIMINAL TRESPASS": 18,
	                    "OFFENSE INVOLVING CHILDREN": 19, "STALKING": 20, "CONCEALED CARRY LICENSE VIOLATION": 21,
	                    "PUBLIC INDECENCY": 22, "OBSCENITY": 23, "PUBLIC PEACE VIOLATION": 24,
	                    "LIQUOR LAW VIOLATION": 25, "INTIMIDATION": 26, "PROSTITUTION": 27,
	                    "NON-CRIMINAL (SUBJECT SPECIFIED)": 28, "NON-CRIMINAL": 29, "GAMBLING": 30, "OTHER OFFENSE": 31}

	def __init__(self):
		"""
		Constructor that could do several things, including read in your training data
		"""
		csvfile = open('full.csv', "r", newline="")
		self.data = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
		self.header = next(self.data)
		self.crime_priority_tree = AVLTree()
		self.loc_priority_tree = AVLTree()

		# dispatch_queue = MinHeap()

	def build_loc_priority(self):
		"""
		Should be used to build your location-priority AVL tree
		"""
		# latitude_index=self.header.index("Latitude")
		# longitude_index=self.header.index("Longitude")
		# location_index=self.header.index("Location")
		# street_index=self.header.index("Block")
		loc_dict = Beats_priority.create_dict()
		beat_index = self.header.index("Beat")
		crime_index = self.header.index("Primary Type")

		# curr_lat=41.830640
		# curr_long=-87.623780
		for i in self.data:
			beat = i[beat_index]
			# dist=abs(current_lat-latitude)+abs(current_long-longitude)
			self.loc_priority_tree.insert(loc_dict[beat],beat)
		return self.loc_priority_tree

	def build_crime_priority(self):
		"""
		Should be used to build your location-priority AVL tree
		"""
		primary_type_index = self.header.index("Primary Type")
		for i in self.data:
			primary_type = i[primary_type_index]
			self.crime_priority_tree.insert(self.CRIME_DICTIONARY[primary_type], primary_type)
		return self.crime_priority_tree

	def add_dispatch(self, dispatch_string):

		MinHeap.dispatch_queue.insert(dispatch_string)

	def decide_next_patrol(self, new_request=None):
		"""
		You will need this later, but I'm just giving this here for you to keep it as a placeholder
		"""
		add_dispatch(new_request)

		if self._count != 0:

			next_patrol = MinHeap.dispatch_queue.extract()

			lat = next_patrol.value.split()[21]
			long = next_patrol.value.split()[22]

			bottomleft = (lat - 0.001, long - 0.001)
			topleft = (lat - 0.001, long + 0.001)
			topright = (lat + 0.001, long + 0.001)
			bottomright = (lat + 0.001, long - 0.001)

			return topleft, topright, bottomleft, bottomright

		else:
			pass


d = ChicagoCrimeFun()
tree = d.build_loc_priority()
tree.visualize()
