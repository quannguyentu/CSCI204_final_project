import csv

CRIME_DICTIONARY = {"HOMICIDE": 0, "ARSON": 1, "HUMAN TRAFFICKING": 2, "KIDNAPPING": 3, "WEAPONS VIOLATION": 4,
	                    "SEX OFFENSE": 5, "CRIM SEXUAL ASSAULT": 6, "ASSAULT": 7, "BATTERY": 8,
	                    "MOTOR VEHICLE THEFT": 9, "THEFT": 10, "BURGLARY": 11, "ROBBERY": 12,
	                    "INTERFERENCE WITH PUBLIC OFFICER": 13, "DECEPTIVE PRACTICE": 14, "NARCOTICS": 15,
	                    "OTHER NARCOTIC VIOLATION": 16, "CRIMINAL DAMAGE": 17, "CRIMINAL TRESPASS": 18,
	                    "OFFENSE INVOLVING CHILDREN": 19, "STALKING": 20, "CONCEALED CARRY LICENSE VIOLATION": 21,
	                    "PUBLIC INDECENCY": 22, "OBSCENITY": 23, "PUBLIC PEACE VIOLATION": 24,
	                    "LIQUOR LAW VIOLATION": 25, "INTIMIDATION": 26, "PROSTITUTION": 27,
	                    "NON-CRIMINAL (SUBJECT SPECIFIED)": 28, "NON-CRIMINAL": 29, "GAMBLING": 30, "OTHER OFFENSE": 31}

def read_data(file_name):
	with open(file_name, "r", newline="") as data:
		result = csv.reader(data, delimiter=',', skipinitialspace=True)
		result = list(result)
	return result


def create_dict():
	data = read_data("full.csv")
	loc_dict = {}
	beat_index = 10
	crime_index = 5
	for row in data[1:]:
		beat = row[beat_index]
		crime = row[crime_index]
		crime_priority = CRIME_DICTIONARY[crime]
		try:
			loc_dict[beat] += crime_priority
		except:
			loc_dict[beat] = crime_priority
	return loc_dict
