import re

class AadharRegex:
	def find_name(self,text):
		words = text.split()
		stop = ['DOB', 'Year', 'Date', 'DOB:', 'Year:', 'Date:', 'Address', 'Address:']
		#print(words)
		if(words):
			name = ""
			for word in words:
				if(word in stop):
					return name
				name = name + word + ' '
			return name
		return "Not Found!"

	def find_dob(self,text):
		dob = re.search(r"(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-](\d{4})", text)
		if(dob):
			return dob.group()
		return "Not Found!"

	def find_AadharNo(self,text):
		aadhar = re.search(r"(\d{4}[\-\s]*)(\d{4}[\-\s]*)(\d{4}[\-\s]*)", text)
		if(aadhar):
			return aadhar.group()
		return "Not Found!"

	def find_address(self,text):
		addr = re.search(r"(?<=Address: )(.*)(\d{6})", text)
		if(addr):
			fname, address = addr.group().split(',', 1)
			return address
		return "Not Found!"
