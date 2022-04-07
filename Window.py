# Tkinter GUI experiment for CS 224
# Built alongside: https://www.youtube.com/watch?v=LeeCrwgHYnw&list=PLXlKT56RD3kBUYQiG_jrAMOtm_SfPLvwR
# @author Nolan Rapp

import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, Label
from PIL import ImageTk, Image
import os, spotify, shutil, subprocess, threading
from glitchart import main as glitcher

# first line
window = tk.Tk()
window.title('Top Album Glitch Art')
window.geometry('640x700')

# global variables
# **Note that transformations should modify imageOpen,
# which can then be used to generate a preview.**
path = os.getcwd() + os.path.sep + 'datafiles'
global new_img_path, new_img
spotify.getAlbumCovers(path)
imageList = [fname for fname in os.listdir(path) if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
imageNames = [x for x in os.listdir(path) if x.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
imagePath = path + os.path.sep + imageNames[0]
imagePreview = ImageTk.PhotoImage(Image.open(imagePath))
current_transformation = ""

# Make frame fill the whole window
topFrame = tk.Frame(window)
topFrame.pack(fill=tk.BOTH, expand=1)

# Dropdown 0
tk_current_image = tk.StringVar()
image_select_input = tk.ttk.Combobox(topFrame, values=imageList, textvariable=tk_current_image, state='readonly')
image_select_input.set('Select an image')
image_select_input.grid(row=0, column=0, columnspan=3, sticky='EW')

# Dropdown 1
tk_current_transformation = tk.StringVar()
transformation_select_input = tk.ttk.Combobox(topFrame, values=['Lightness', 'Hue', 'Saturation', 'Intensity', 'Minimum'], textvariable=tk_current_transformation, state='readonly')
transformation_select_input.set('Select a transformation')
transformation_select_input.grid(row=1, column=0, columnspan=3, sticky='EW')

# row 2
topFrame.rowconfigure(2, weight=2)
img_label = tk.Label(topFrame, bg='grey', image=imagePreview, width=640, height=640)
img_label.grid(row=2, column=0, columnspan=3, sticky='EWNS')

# discard click event
def discard_command():
	imageOpen = Image.open(imagePath)
	imagePreview = ImageTk.PhotoImage(imageOpen)
	img_label.configure(image=imagePreview)
	img_label.image = imagePreview

# row 3 - column 0
topFrame.columnconfigure(0, weight=1)
discard_btn = tk.Button(topFrame, text="Undo", command= discard_command)
discard_btn.grid(row=3, column=0, sticky='EW');

# row 3 - column 1
topFrame.columnconfigure(1, weight=5)
processing_bar = ttk.Progressbar( topFrame, orient='horizontal', mode='indeterminate')
processing_bar.grid(row=3, column=1, sticky='EW')

# save function called when 'Save' button is clicked
def img_save():
	global new_img, new_img_path
	new_img.save(new_img_path)

# row 3 - column 2
topFrame.columnconfigure(2, weight=1)
save_btn = tk.Button(topFrame, text="Save", command=img_save)
save_btn.grid(row=3, column=2, sticky='EW')

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
	global new_img_path, new_img

	glitched_rtn = glitcher.get_glitched(image_path=imagePath, lower_threshold=0.25, upper_threshold=0.85, angle=0, sorting_func=current_transformation, interval_func='threshold')
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
def transformation_select_command(event):
	global current_transformation
	current_transformation = tk_current_transformation.get()
	threading.Thread(target=run_function).start()
transformation_select_input.bind('<<ComboboxSelected>>', transformation_select_command)

# discard_btn.configure(command=discard_command)

# close event
def on_closing():
	if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
		# imageOpen.close()
		# for file in os.listdir(path):
		# 	os.remove(os.path.join(path, file))
		window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
