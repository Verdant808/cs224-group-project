# Tkinter GUI experiment for CS 224
# Built alongside: https://www.youtube.com/watch?v=LeeCrwgHYnw&list=PLXlKT56RD3kBUYQiG_jrAMOtm_SfPLvwR
# @author Nolan Rapp

import tkinter as tk
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
spotify.getAlbumCovers(path)
imageList = [fname for fname in os.listdir(path)]
imageNames = os.listdir(path)
imagePath = path + os.path.sep + imageNames[0]
try: 
	imageOpen = Image.open(imagePath)
except IOError:
	print('oops')
imagePreview = ImageTk.PhotoImage(Image.open(imagePath))
current_transformation = ""

# Make frame fill the whole window
topFrame = tk.Frame(window)
topFrame.pack(fill=tk.BOTH, expand=1)

# row 0
tk_current_image = tk.StringVar()
image_select_input = tk.ttk.Combobox(topFrame, values=imageList, textvariable=tk_current_image, state='readonly')
image_select_input.set('Select an image')
image_select_input.grid(row=0, column=0, columnspan=3, sticky='EW')

# row 1
tk_current_transformation = tk.StringVar()
transformation_select_input = tk.ttk.Combobox(topFrame, values=['Lightness', 'Hue', 'Saturation', 'Intensity', 'Minimum'], textvariable=tk_current_transformation, state='readonly')
transformation_select_input.set('Select a transformation')
transformation_select_input.grid(row=1, column=0, columnspan=3, sticky='EW')

# row 2
topFrame.rowconfigure(2, weight=2)
img_label = tk.Label(topFrame, bg='grey', image=imagePreview, width=640, height=640)
img_label.grid(row=2, column=0, columnspan=3, sticky='EWNS')

# row 3 - column 0
topFrame.columnconfigure(0, weight=1)
discard_btn = tk.Button(topFrame, text="Undo")
discard_btn.grid(row=3, column=0, sticky='EW')

# row 3 - column 1
topFrame.columnconfigure(1, weight=5)
processing_bar = ttk.Progressbar( topFrame, orient='horizontal', mode='indeterminate')
processing_bar.grid(row=3, column=1, sticky='EW')

# row 3 - column 2
topFrame.columnconfigure(2, weight=1)
save_btn = tk.Button(topFrame, text="Save")
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

# transformation selection event
def transfApply_command():
	glitched_pic = glitcher.get_glitched(image_path=imagePath, lower_threshold=0.25, upper_threshold=0.85, angle=0, sorting_func=current_transformation, interval_func='threshold')
	newImagePath = path + os.path.sep + glitched_pic

	# match current_transformation:
	# 	case 'Lightness':
	# 		newImagePath = path + os.path.sep + 'temp.png'
	# 		subprocess.run(['python', '-m', 'glitchart', imagePath,'-o', newImagePath, '-s', 'lightness'])
	# 	case 'Hue':
	# 		tk.messagebox.showwarning("Warning", "Transformation not yet implemented")
	# 		return
	# 	    # newImagePath = path + os.path.sep + 'temp.png'
	# 	    # subprocess.run(['python', '-m', 'glitchart', imagePath, '-o', newImagePath, '-s', 'hue'])
	# 	case 'Saturation':
	# 		tk.messagebox.showwarning("Warning", "Transformation not yet implemented")
	# 		return			
	# 	    # newImagePath = path + os.path.sep + 'temp.png'
	# 	    # subprocess.run(['python', '-m', 'glitchart', imagePath, '-o', newImagePath, '-s', 'saturation'])
	# 	case 'Intensity':
	# 		tk.messagebox.showwarning("Warning", "Transformation not yet implemented")
	# 		return
	# 	    # newImagePath = path + os.path.sep + 'temp.png'
	# 	    # subprocess.run(['python', '-m', 'glitchart', imagePath, '-o', newImagePath, '-s', 'intensity'])
	# 	case 'Minimum':
	# 		tk.messagebox.showwarning("Warning", "Transformation not yet implemented")
	# 		return
	# 	    # newImagePath = path + os.path.sep + 'temp.png'
	# 	    # subprocess.run(['python', '-m', 'glitchart', imagePath, '-o', newImagePath, '-s', 'minimum'])

	imageOpen = Image.open(newImagePath)
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

# discard click event
def discard_command():
	imageOpen = Image.open(imagePath)
	imagePreview = ImageTk.PhotoImage(imageOpen)
	img_label.configure(image=imagePreview)
	img_label.image = imagePreview
discard_btn.configure(command=discard_command)

# close event
def on_closing():
	if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
		imageOpen.close()
		for file in os.listdir(path):
			os.remove(os.path.join(path, file))
		window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
