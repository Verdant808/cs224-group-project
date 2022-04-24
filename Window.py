# Tkinter GUI experiment for CS 224
# Built alongside: https://www.youtube.com/watch?v=LeeCrwgHYnw&list=PLXlKT56RD3kBUYQiG_jrAMOtm_SfPLvwR
# @author Nolan Rapp

from doctest import Example
from struct import pack
from this import s
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, Label
from turtle import left, width
from PIL import ImageTk, Image
import os, spotify, shutil, subprocess, threading
from glitchart import main as glitcher

# first line
window = tk.Tk()
window.title('Top Album Glitch Art')
window.geometry('640x850')

# global variables
# **Note that transformations should modify imageOpen,
# which can then be used to generate a preview.**
path = os.getcwd() + os.path.sep + 'datafiles'
global new_img_path, new_img, angle, outputname, lowerthreshold, upperthreshold, current_transformation
spotify.getAlbumCovers(path)
imageList = [fname for fname in os.listdir(path) if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
imageNames = [x for x in os.listdir(path) if x.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
imagePath = path + os.path.sep + imageNames[0]
imagePreview = ImageTk.PhotoImage(Image.open(imagePath))
current_transformation = ""

picFrame = tk.Frame(window)
picFrame.pack(fill=tk.BOTH, expand=1, side=tk.RIGHT)

# Make frame fill the whole window
topFrame = tk.Frame(window)
topFrame.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

# Dropdown - image selection
tk_current_image = tk.StringVar()
image_select_input = tk.ttk.Combobox(topFrame, values=imageList, textvariable=tk_current_image, state='readonly')
image_select_input.set('Select an image')
# image_select_input.grid(row=0, column=0, columnspan=3, sticky='EW')
image_select_input.pack(side=tk.TOP, pady=5, anchor=NW)

# Dropdown - transformation function
tk_current_transformation = tk.StringVar()
transformation_select_input = tk.ttk.Combobox(topFrame, values=['Lightness', 'Hue', 'Saturation', 'Intensity', 'Minimum'], textvariable=tk_current_transformation, state='readonly')
transformation_select_input.set('Select a transformation')
# transformation_select_input.grid(row=1, column=0, columnspan=3, sticky='EW')
transformation_select_input.pack(side=tk.TOP, pady=5, anchor=NW)

# Dropdown - interval function
tk_interval = tk.StringVar()
transformation_select_input = tk.ttk.Combobox(topFrame, values=['Threshold', 'Random', 'None'], textvariable=tk_interval, state='readonly')
transformation_select_input.set('Select an interval function')
# transformation_select_input.grid(row=2, column=0, columnspan=3, sticky='EW')
transformation_select_input.pack(side=tk.TOP, pady=5, anchor=NW)

# get input values for parameters to glitcher function
def print_angle():
	global angle, outputname, lowerthreshold, upperthreshold, current_transformation, interval
	angle = int(tk_inputangle.get(1.0, 'end-1c'))
	outputname = str(tk_outputname.get(1.0, 'end-1c'))
	lowerthreshold = float(tk_lowerthreshold.get(1.0, 'end-1c'))
	upperthreshold = float(tk_upperthreshold.get(1.0, 'end-1c'))
	current_transformation = str(tk_current_transformation.get()).lower()
	interval = str(tk_interval.get()).lower()
	transfApply_command()

# angle entry text
angleText = StringVar()
angleText.set('Angle:')
angle_label = Label(topFrame, textvariable=angleText, height=1)
# angle_label.grid(row=3, column=0, columnspan=1, sticky='EW')
angle_label.pack(side=tk.TOP, pady=5, padx=5, after=transformation_select_input, anchor=NW)

tk_inputangle = tk.Text(topFrame, height=1, width=15)
# tk_inputangle.grid(row=3, column=1, columnspan=1, sticky='EW')
tk_inputangle.pack(side=tk.TOP, pady=5, padx=5, after=angle_label, anchor=NW)

# output name
outputText = StringVar()
outputText.set('Output Name:')
output_label = Label(topFrame, textvariable=outputText, height=1)
# output_label.grid(row=3, column=2, columnspan=1, sticky='EW')
output_label.pack(side=tk.TOP, pady=5, padx=5, after=tk_inputangle, anchor=NW, )

tk_outputname = tk.Text(topFrame, height=1, width=20)
# tk_outputname.grid(row=3, column=3, columnspan=1, sticky='EW')
tk_outputname.pack(side=tk.TOP, pady=5, padx=5, after=output_label, anchor=NW)

# lower threshold
lowerText = StringVar()
lowerText.set('Lower Threshold:')
lower_label = Label(topFrame, textvariable=lowerText, height=1)
# lower_label.grid(row=4, column=0, columnspan=1, sticky='EW')
lower_label.pack(side=tk.TOP, pady=5, padx=5, after=tk_outputname, anchor=NW)

tk_lowerthreshold = tk.Text(topFrame, height=1, width=15)
# tk_lowerthreshold.grid(row=4, column=1, columnspan=1, sticky='EW')
tk_lowerthreshold.pack(side=tk.TOP, pady=5, padx=5, after=lower_label, anchor=NW)

# upper threshold
upperText = StringVar()
upperText.set('Upper Threshold:')
upper_label = Label(topFrame, textvariable=upperText, height=1)
# upper_label.grid(row=4, column=2, columnspan=1, sticky='EW')
upper_label.pack(side=tk.TOP, pady=5, padx=5, anchor=NW)

tk_upperthreshold = tk.Text(topFrame, height=1, width=15)
# tk_upperthreshold.grid(row=4, column=3, columnspan=1, sticky='EW')
tk_upperthreshold.pack(side=tk.TOP, pady=5, padx=5, anchor=NW)

printButton = tk.Button(topFrame, text = 'Glitch', command=print_angle)
# printButton.grid(row=4, column=4, columnspan=1, sticky='EW')
printButton.pack(side=tk.TOP, pady=5, padx=5, anchor=NW)

# row 2
topFrame.rowconfigure(2, weight=2)
img_label = tk.Label(picFrame, bg='grey', image=imagePreview, width=640, height=640)
# img_label.grid(row=5, column=0, columnspan=3, sticky='EWNS')
img_label.pack(side=tk.TOP, pady=5, padx=5, anchor=NW)

# discard click event
def discard_command():
	imageOpen = Image.open(imagePath)
	imagePreview = ImageTk.PhotoImage(imageOpen)
	img_label.configure(image=imagePreview)
	img_label.image = imagePreview

# row 3 - column 0
topFrame.columnconfigure(0, weight=1)
discard_btn = tk.Button(topFrame, text="Undo", command= discard_command)
# discard_btn.grid(row=6, column=0, sticky='EW');
discard_btn.pack(side=tk.TOP, pady=5, padx=5, anchor=NW)

# row 3 - column 1
topFrame.columnconfigure(1, weight=5)
processing_bar = ttk.Progressbar( topFrame, orient='horizontal', mode='indeterminate')
# processing_bar.grid(row=6, column=1, sticky='EW')
processing_bar.pack(side=tk.TOP, pady=5, padx=5, anchor=NW)

# save function called when 'Save' button is clicked
def img_save():
	global new_img, new_img_path
	new_img.save(new_img_path)

# row 3 - column 2
topFrame.columnconfigure(2, weight=1)
save_btn = tk.Button(topFrame, text="Save", command=img_save)
# save_btn.grid(row=6, column=2, sticky='EW')
save_btn.pack(side=tk.TOP, pady=5, padx=5, anchor=NW)

## Events
# image selection
def image_select_command(event):
	global imagePath
	imagePath = path + os.path.sep + tk_current_image.get()
	imageOpen = Image.open(imagePath)
	imagePreview = ImageTk.PhotoImage(imageOpen)
	img_label.configure(image=imagePreview)
	img_label.image = imagePreview
image_select_input.bind('<<ComboboxSelected>>', image_select_command)

# Applies the glitcher to selected image
def transfApply_command():
	global new_img_path, new_img, angle, outputname, lowerthreshold, upperthreshold, current_transformation, interval

	glitched_rtn = glitcher.get_glitched(image_path=imagePath, lower_threshold=lowerthreshold, upper_threshold=upperthreshold,
										 angle=angle, sorting_func=current_transformation, interval_func=interval, output_name=outputname)
	new_img = glitched_rtn['img']
	new_img_path = glitched_rtn['img_path']
	# newImagePath = path + os.path.sep + glitched_pic
	# print(newImagePath)

	imageOpen = new_img
	imagePreview = ImageTk.PhotoImage(imageOpen)
	img_label.configure(image=imagePreview)
	img_label.image = imagePreview

# transformation selection event
def run_function():
	processing_bar.start(interval=10)
	transfApply_command()
	processing_bar.stop()

# transformation selection event
# def transformation_select_command(event):
# 	global current_transformation
# 	current_transformation = tk_current_transformation.get()
# 	threading.Thread(target=run_function).start()
# transformation_select_input.bind('<<ComboboxSelected>>', transformation_select_command)

# discard_btn.configure(command=discard_command)

# close event
def on_closing():
	# if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
		# imageOpen.close()
		# for file in os.listdir(path):
		# 	os.remove(os.path.join(path, file))
		window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
