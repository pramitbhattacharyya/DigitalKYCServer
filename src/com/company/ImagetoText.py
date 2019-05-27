#!/usr/bin/env python3
import cv2
import pytesseract
import sys
class ImagetoText:
	def convert(self,path):
		# print("---------------------------------------------------------")
		# print("File name: "+path)
		img=cv2.imread(path)
		grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# grey_inv=cv2.bitwise_not(grey)
		# cv2.imshow("grey_inv",grey_inv)
		# cv2.waitKey(0)
		# print("---------------------------------------------------------")
		# print("Only_cropped:")
		Only_cropped=pytesseract.image_to_string(img,lang="eng")
		# print(Only_cropped)
		# print("---------------------------------------------------------")
		# print("Grey Image:")
		Crop_n_Grey=pytesseract.image_to_string(grey,lang="eng")
		# print()
		# print("---------------------------------------------------------")
		# print("Grey Inverted:")
		# print(pytesseract.image_to_string(grey_inv,lang="eng"))
		# print("---------------------------------------------------------")
		# print("#########################################################")
		return Only_cropped,Crop_n_Grey
if __name__=='__main__':
	if len(sys.argv) == 2 and '*' in sys.argv[1]:
	        files = glob.glob(sys.argv[1])
	        random.shuffle(files)
	else:
	    files = sys.argv[1:]
	for path in files: 
		ImagetoText().convert(path)

