#################################
###### Popup Notifications ######
#################################
from Tkinter import *
import tkMessageBox

def error(title, text):
	window = Tk()
	window.wm_withdraw()
	#message at x:200,y:200
	window.geometry("1x1+200+200")#remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
	tkMessageBox.showerror(title=title,message=text,parent=window)

def info(title, text):
	window = Tk()
	window.wm_withdraw()
	#message at x:200,y:200
	window.geometry("1x1+200+200")#remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
	tkMessageBox.showinfo(title=title,message=text,parent=window)
