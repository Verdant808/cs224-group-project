# Tkinter GUI experiment for CS 224
# Built alongside: https://www.youtube.com/watch?v=LeeCrwgHYnw&list=PLXlKT56RD3kBUYQiG_jrAMOtm_SfPLvwR
# @author Nolan Rapp

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
window.geometry('900x700')

# global variables
# **Note that transformations should modify imageOpen,
# which can then be used to generate a preview.**
path = os.getcwd() + os.path.sep + 'datafiles'
global new_img_path, new_img, outputname, lowerthreshold, upperthreshold, current_transformation
spotify.getAlbumCovers(path)
imageList = [fname for fname in os.listdir(path) if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
imageNames = [x for x in os.listdir(path) if x.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
imagePath = path + os.path.sep + imageNames[0]
imagePreview = ImageTk.PhotoImage(Image.open(imagePath))
current_transformation = ""

# make frames to pack elements
picFrame = tk.Frame(window)
dropdowns = tk.Frame(window)
outputNameFrame = tk.Frame(window)
buttonFrame = tk.Frame(window)

# Make frame fill the whole window
dropdowns.grid(row=0, column=0)
outputNameFrame.grid(row=6, column=0)

# Dropdown - image selection
tk_current_image = tk.StringVar()
image_select_input = tk.ttk.Combobox(window, values=imageList, textvariable=tk_current_image, state='readonly')
image_select_input.set('Select an image')
image_select_input.grid(row=0, column=0, sticky='EW')

# Dropdown - transformation function
tk_current_transformation = tk.StringVar()
transformation_select_input = tk.ttk.Combobox(window, values=['Lightness', 'Hue', 'Saturation', 'Intensity', 'Minimum'], textvariable=tk_current_transformation, state='readonly')
transformation_select_input.set('Select a transformation')
transformation_select_input.grid(row=1, column=0, sticky='EW')

# Dropdown - interval function
tk_interval = tk.StringVar()
transformation_select_input = tk.ttk.Combobox(window, values=['Threshold', 'Random', 'None'], textvariable=tk_interval, state='readonly')
transformation_select_input.set('Select an interval function')
transformation_select_input.grid(row=2, column=0, sticky='EW')

var = StringVar()
scale_angle = Scale(window, label='Angle:', orient=HORIZONTAL, variable=var, from_=0, to=360)
scale_angle.grid(row=3, column=0, sticky="EW")

# output name
outputText = StringVar()
outputText.set('Output Name:')
output_label = Label(outputNameFrame, textvariable=outputText, height=1)
output_label.pack(side=tk.LEFT, pady=5, padx=5, anchor=NW)

tk_outputname = tk.Text(outputNameFrame, height=1, width=20)
tk_outputname.pack(side=tk.LEFT, pady=5, padx=5, anchor=NW)

# lower threshold
lower_scale = Scale(window, label='Lower Threshold:', orient=HORIZONTAL, from_=0.00, to=1.00, resolution=0.01)
lower_scale.set(0.35)
lower_scale.grid(row=4, column=0, sticky="EW")

# upper threshold
upper_scale = Scale(window, label='Upper Threshold:', orient=HORIZONTAL, from_=0.00, to=1.00, resolution=0.01)
upper_scale.set(0.85)
upper_scale.grid(row=5, column=0, sticky="EW")

# picture
img_label = tk.Label(window, bg='grey', image=imagePreview, width=640, height=640)
img_label.grid(row=0, column=1, rowspan=8, columnspan=3, sticky='EWNS')

# discard click event
def discard_command():
	imageOpen = Image.open(imagePath)
	imagePreview = ImageTk.PhotoImage(imageOpen)
	img_label.configure(image=imagePreview)
	img_label.image = imagePreview

# undo button
buttonFrame.columnconfigure(0, weight=1)
discard_btn = tk.Button(window, text="Undo", command= discard_command)
discard_btn.grid(row=8, column=0, sticky='EW')

# progress bar
buttonFrame.columnconfigure(1, weight=5)
processing_bar = ttk.Progressbar(window, orient='horizontal', mode='indeterminate')
processing_bar.grid(row=8, column=1, columnspan=2, sticky='EW')

# save function called when 'Save' button is clicked
def img_save():
	global new_img, new_img_path
	new_img.save(new_img_path)

# save button
buttonFrame.columnconfigure(2, weight=1)
save_btn = tk.Button(window, text="Save", command=img_save)
save_btn.grid(row=8, column=3, sticky='EW')

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
	global new_img_path, new_img, outputname, lowerthreshold, upperthreshold, current_transformation, interval
	angle = int(scale_angle.get())
	lowerthreshold = float(lower_scale.get())
	upperthreshold = float(upper_scale.get())
	outputname = str(tk_outputname.get(1.0, 'end-1c'))
	current_transformation = str(tk_current_transformation.get()).lower()
	interval = str(tk_interval.get()).lower()


	glitched_rtn = glitcher.get_glitched(image_path=imagePath, lower_threshold=lowerthreshold, upper_threshold=upperthreshold,
										 angle=angle, sorting_func=current_transformation, interval_func=interval, output_name=outputname)
	new_img = glitched_rtn['img']
	new_img_path = glitched_rtn['img_path']
	# run_function()

	imageOpen = new_img
	imagePreview = ImageTk.PhotoImage(imageOpen)
	img_label.configure(image=imagePreview)
	img_label.image = imagePreview

# transformation selection event
def run_function():
	processing_bar.start(interval=10)
	transfApply_command()
	processing_bar.stop()

# glitch button
printButton = tk.Button(window, text = 'Glitch', command=transfApply_command)
printButton.grid(row=7, column=0, columnspan=1, sticky='EW')

window.mainloop()
