import serial
from Tkinter import *
from threading import Thread
from SimpleCV import Camera, DrawingLayer, Color

#s = serial.Serial(port='/dev/ttyACM2', baudrate=9600)
cam = Camera(0,{"width": 320, "height": 240})

def initPos():
	w1.set(120)
	w2.set(180)
	w3.set(150)
	w4.set(0)
	w5.set(0)

def renderGUI():
	global bNums
	initPos()
	while True:
		img = cam.getImage().flipHorizontal()
		img = img.binarize()
		blobs = img.findBlobs()
		rect = DrawingLayer((img.width, img.height))
		rect_dim = (200,200)
		l1.configure(text = "Total Blobs: " + str(len(blobs)))
		for b in blobs:
			#print b.centroid()
			# print b.isCircle()
			if b.area() > 300:
				center_point = b.centroid()
				rect.centeredRectangle(center_point, rect_dim, color=Color.RED)
				img.addDrawingLayer(rect)
				#img.applyLayers()
		img.show()
		servos = [str(w1.get()), str(w2.get()), str(w3.get()), str(w4.get()), str(w5.get())]
		for i in servos:
			pass
			#print (str(servos.index(i)+1) + ":" + str(i) + ";")
			#s.write(str(servos.index(i)+1) + ":" + str(i) + ";")

master = Tk()
master.title("Robot Arm Controller")
w1 = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=300)
w1.pack()
w2 = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=300)
w2.pack()
w3 = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=300)
w3.pack()
w4 = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=300)
w4.pack()
w5 = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=300)
w5.pack()

l1 = Label(master)
l1.pack()

t = Thread(target=renderGUI)
t.daemon = True
t.start()

mainloop()
