# import the necessary packages
import numpy as np
import cv2
import imutils
import sys
 
# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image file")
# args = vars(ap.parse_args())
class SkewCorrection(object):
	def run(self,path,path_orig): 
		# load the image from disk
		# path=args["image"]	
		# image = cv2.imread(args["image"])
		orig_img=cv2.imread(path_orig)
		image = cv2.imread(path)
		# convert the image to grayscale and flip the foreground
		# and background to ensure foreground is now "white" and
		# the background is "black"
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)		
		gray = cv2.bitwise_not(gray)
		 
		# threshold the image, setting all foreground pixels to
		# 255 and all background pixels to 0
		thresh = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]		
		# cv2.imshow("thresh",thresh)
		# cv2.waitKey(0)
		# os.exit()
		# cv2.imshow("gray",gray)
		# cv2.waitKey(0)
		# grab the (x, y) coordinates of all pixel values that
		# are greater than zero, then use these coordinates to
		# compute a rotated bounding box that contains all
		# coordinates
		coords = np.column_stack(np.where(thresh > 0))
		init_angle = cv2.minAreaRect(coords)[-1]
		 
		# the `cv2.minAreaRect` function returns values in the
		# range [-90, 0); as the rectangle rotates clockwise the
		# returned angle trends to 0 -- in this special case we
		# need to add 90 degrees to the angle
		if init_angle < -45:
			angle = -(init_angle) 
			# image=imutils.rotate_bound(image,-90)
			# angle = -(90+init_angle)
		 
		# otherwise, just take the inverse of the angle to make
		# it positive
		else:
			# print("angle=",init_angle)
			angle = -init_angle
		# rotate the image to deskew it
		(h, w) = orig_img.shape[:2]
		center = (w // 2, h // 2)

		M = cv2.getRotationMatrix2D(center, angle, 1.0)
		rotated = cv2.warpAffine(orig_img, M, (w, h),
			flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
		# draw the correction angle on the image so we can validate it
		# cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
		# 	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

		# imutils.rotate() may crop the image on rotation 
		# whereas imutils.rotate_bound() doesn't as it takes 
		# care of the height and width of the iamge on rotation.

		if(init_angle< -45):
			rotated  = imutils.rotate_bound(rotated,90)
		 
		# show the output image
		# print("[INFO] angle: {:.3f}".format(angle))
		# cv2.imshow("Input", image)
		# cv2.imshow("Rotated", rotated)
		path=path[:-4]+"_rotated"+path[-4:]
		cv2.imwrite(path,rotated)
		if('.jpg' in path):
			out_path = path.replace('.jpg', '.crop.jpg')
		elif('.png' in path):
			out_path = path.replace('.png', '.crop.png')  # .png as input
		return path,out_path
		# python3orig().process_image(path, out_path)
		# os.system("python3 python3orig.py "+path[:-4]+"_rotated"+path[-4:])
		# cv2.waitKey(0)

if __name__ == '__main__':
	if len(sys.argv) == 2 and '*' in sys.argv[1]:
		files = glob.glob(sys.argv[1])
		random.shuffle(files)
	else:
		files = sys.argv[1:]
	for path in files:
		SkewCorrection().run(path,path)