# Extract Name, DOB, DL No. and Address from text

import re

class DL_Regex:
	def find_dob(self,text):
		dates = re.findall(r"(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-](\d{4})", text)
		min_year = '3000'
		dob = None
		for date in dates:
			if(date[2] < min_year):
				min_year = date[2]
				dob = date
		if(dob):
			return dob[0]+"/"+dob[1]+"/"+dob[2]
		return "Not Found!"


	def find_DLNo(self,text):
		DLNo = re.search(r"([A-Z]+[\s\-]*)(\d{2}[\s\-]*)(\d{4}[\s\-]*)(\d{7})", text)
		if(DLNo):
			return DLNo.group(0)
		return "Not Found!"

	def find_Name(self,text):
		name = re.search(r"(?i)Name\s*[\.\:\-\s]\s*(\b[a-zA-Z]*[^\s@.]\b\s?\b[a-zA-Z]*[^\s@.]\b)", text)
		if(name):
			nme = name.group().split()
			sname = nme[len(nme) - 1]
			fname = nme[len(nme) - 2]
			return fname + ' ' + sname
		return "Not Found!"

	def find_address(self,text):
		addr = re.search(r"(Add)(.*)(\d{6})", text)
		if(addr):
			return addr.group()
		return "Not Found!"
