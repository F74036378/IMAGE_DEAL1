import tkinter as tk
import pygubu
import cv2
import copy
import numpy as np

class Application:

	def __init__(self, master):
		self.master = master

		#create builder
		self.builder = builder = pygubu.Builder()
		#load ui file
		builder.add_from_file('hw1.ui')
		#create a widget
		self.mainwindow = builder.get_object('window', master)

		#connect callback
		builder.connect_callbacks(self)

	def btn_quit_on_click(self):
		self.master.quit()

	#button for problem 1.1
	def btn_11_on_click(self):
		#add your code here
		img = cv2.imread('dog.bmp')
		height, width, channels = img.shape
		cv2.imshow('img1.1',img)
		print('Height = '+str(height))
		print('Width = '+str(width))
		cv2.waitKey(0)

	#button for problem 1.2
	def btn_12_on_click(self):
		#add your code here
		img = cv2.imread('color.png')
		'''img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		cv2.imshow('img1.2',img)'''
		for x in range(0,len(img)):
			for y in range(0,len(img[x])):
				a = img[x][y][0]
				b = img[x][y][1]
				c = img[x][y][2]
				img[x][y][0] = b
				img[x][y][1] = c
				img[x][y][2] = a
		cv2.imshow('img1.2',img)
		cv2.waitKey(0)

	#button for problem 1.3
	def btn_13_on_click(self):
		#add your code here
		img = cv2.imread('dog.bmp')
		height, width, channels = img.shape
		new_img = copy.deepcopy(img)
		for x in range(height):
			for y in range(width):
				new_img[x][width-1-y] = img[x][y]
		cv2.imshow('img1.3',new_img)
		cv2.waitKey(0)
	
	#button for problem 1.4
	def btn_14_on_click(self):
		def callback(x):
			pass
		#add your code here
		cv2.namedWindow('img1.4')

		cv2.createTrackbar('BLEND','img1.4',0,100,callback)
		cv2.createTrackbar('OFF','img1.4',0,1,callback)

		img = cv2.imread('dog.bmp')
		height, width, channels = img.shape
		new_img = copy.deepcopy(img)
		for x in range(height):
			for y in range(width):
				new_img[x][width-1-y] = img[x][y]
		while(True):
			off = cv2.getTrackbarPos('OFF','img1.4')
			if(off == 1):
				break
			blend = cv2.getTrackbarPos('BLEND','img1.4')
			blend = blend/100
			img_mix = cv2.addWeighted(img, (1-blend), new_img, blend, 0)
			cv2.imshow('img1.4',img_mix)
			cv2.waitKey(1)

	#button for problem 2.1
	def btn_21_on_click(self):
		#add your code here
		img = cv2.imread('eye.jpg')
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		cv2.imshow('gray_img2.1', img)
		detect_img = cv2.Canny(img, 150, 300)
		cv2.imshow('detect_img2.1', detect_img)

		cv2.waitKey(0)
	
	#button for problem 2.2
	def btn_22_on_click(self):
		#add your code here
		img = cv2.imread('eye.jpg')
		cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		draw_img = np.ones(img.shape, dtype=np.uint8)
		#	HoughCircles has Canny detector itself
		circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 20,param1=300,param2=40,minRadius=10,maxRadius=50)

		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
			# draw the outer circle
			cv2.circle(draw_img,(i[0],i[1]),i[2],(0,0,255),2)
			# draw the center of the circle
			#cv2.circle(fimg,(i[0],i[1]),2,(0,0,255),3)

		#	get Canny result to draw (has the same Canny parameter with HoughCircles)
		fimg = cv2.Canny(img,150,300)
		fimg = cv2.cvtColor(fimg, cv2.COLOR_GRAY2RGB)

		#	combine draw and Canny result
		mix_draw = cv2.addWeighted(draw_img, 1, fimg, 1, 0)
		cv2.imshow('detected circles',mix_draw)
		cv2.waitKey(0)

	#button for problem 2.3
	def btn_23_on_click(self):
		#add your code here
		cv2.waitKey(0)
	
	#button for problem 3
	def btn_3_on_click(self):
		#add your code here
		cv2.waitKey(0)
	
	#button for problem 4.1
	def btn_41_on_click(self):
		#add your code here
		img = cv2.imread('shoes.jpg')
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
		#cv2.imshow('img4.1_1',img)
		blur = cv2.GaussianBlur(img,(5,5),0)
		#cv2.imshow('img4.1_2',blur)
		median = cv2.medianBlur(blur,5)
		cv2.imshow('img4.1',median)
		cv2.waitKey(0)
	
	#button for problem 4.2
	def btn_42_on_click(self):
		#add your code here
		img = cv2.imread('shoes.jpg')
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
		cv2.imshow('img4.2_local',img)
		blur = cv2.GaussianBlur(img,(5,5),0)
		cv2.imshow('img4.2_Gussian_smooth',blur)
		median = cv2.medianBlur(blur,5)
		cv2.imshow('img4.2_median_filter',median)

if __name__ == '__main__':
	root = tk.Tk()
	app = Application(root)

	root.mainloop()
