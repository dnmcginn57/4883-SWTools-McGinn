"""
David McGinn
3-15-19
4883-Software-Tools
This program uses Mean Squared Error(MSE) to find the most similar
Image in a given folder
"""
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os,sys

def mse(imageA, imageB):
	"""
	Accepts: Target Image, Candidate Image
	Returns: MSE between the two, the lower the better
	"""
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	return err

def compare_images(imageA, imageB, cand_name):
	"""
	Accepts: Target image, Candidate Image, Name of Candidate Image
	Returns: MSE, SSIM of the two images
	This function calls this.mse and skimage.measure.compare_ssim
	"""

	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)

	return (cand_name,m,s)



folder = str(sys.argv[1])
imName = str(sys.argv[2])
#set target image and gray version
tgt_im = cv2.imread(folder + imName)
tgt_im_g = cv2.cvtColor(tgt_im, cv2.COLOR_BGR2GRAY)

filenames = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
closest = ("",sys.maxsize,-1)
for f in filenames:
	#squirrel nor shipit are different sizes than any other emoji so they cannot be compared
	if(str(f) != imName and str(f) != "squirrel.png" and str(f) != "shipit.png"):
		#set current candidate and gray version
		cand_im = cv2.imread(folder + str(f))
		cand_im_g = cv2.cvtColor(cand_im, cv2.COLOR_BGR2GRAY)
		#compare images' gray versions and set to closest if the current candidate is more similar
		cur = compare_images(tgt_im_g,cand_im_g,str(f))
		if(cur[1] < closest[1] and cur[2] > closest[2]):
			closest = cur

#display closest image and target image side by side with their metrics
im_match = cv2.imread(folder + closest[0])
fig = plt.figure("Images")
images = (imName,tgt_im),(closest[0],im_match)
for(i,(name,image)) in enumerate(images):
	ax = fig.add_subplot(1,2,i+1)
	ax.set_title(name)
	plt.imshow(image)
plt.suptitle("MSE: %.2f, SSIM: %.2f" % (closest[1], closest[2]))
plt.show()

