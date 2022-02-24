# Tkinter GUI experiment for CS 224
# @author Nolan Rapp

from PIL import ImageTk, Image
import tkinter as tk
import os

# first line
root = tk.Tk()
# root setup
root.title('Title')
root.geometry('800x600')
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# global variables
# **Note that transformations should modify imageOpen,
# which can then be used to generate a preview.**
path = os.getcwd() + os.path.sep + 'datafiles'
imageNames = os.listdir(path)
imagePath = path + os.path.sep + imageNames[0]
imageOpen = Image.open(imagePath)
imagePreview = ImageTk.PhotoImage(Image.open(imagePath))


# widgets
# row 1
dirSelect_label = tk.Label(root, text='Directory:', anchor='e')
dirSelect_label.grid(padx=1, pady=2.5, sticky='we')

dirSelect_inp = tk.Entry(root)
dirSelect_inp.insert(0, imagePath) # default text
dirSelect_inp.grid(row=0, column=1, sticky='we')

dirChoose_btn = tk.Button(root, text='Select')
dirChoose_btn.grid(row=0, column=2, padx=2, pady=3, sticky='we')

def dirChoose_command():
	# Opens a dialog to help select a directory
	status_label.configure(text='Directory selected.')

dirChoose_btn.configure(command=dirChoose_command)

dirOpen_btn = tk.Button(root, text='Open')
dirOpen_btn.grid(row=0, column=3, padx=2, pady=3, sticky='we')

def dirOpen_command():
	# Opens the selected directory and loads its contents
	# path = dirSelect_inp.get() # .replace("\\\\", os.path.sep)
	# imageNames = os.listdir(path)
	imagePath = path + os.path.sep + imageNames[1]
	imageOpen = Image.open(imagePath)
	imagePreview = ImageTk.PhotoImage(imageOpen)
	img_label.configure(image=imagePreview)
	img_label.image = imagePreview

	status_label.configure(text='Opened a new file.')

dirOpen_btn.configure(command=dirOpen_command)


# row 1
transf_label = tk.Label(root, text='Transformation:', anchor='e')
transf_label.grid(row=1, column=0, padx=2, pady=3, sticky='we')

transfs = ['Vertical Streak', 'Horizontal Streak', 'Hue Boost', 'Gaussian Blur']
transf_inp = tk.Listbox(root, height=1)
transf_inp.grid(row=1, column=1, sticky='we')

for transformation in transfs:
		transf_inp.insert(tk.END, transformation)

transfApply_btn = tk.Button(root, text="Apply")
transfApply_btn.grid(row=1, column=2, padx=2, pady=3, columnspan=2, sticky='we')

def transfApply_command():
	# Applies a transformation selected via the transformation input listbox
	selected = transf_inp.curselection()
	if not selected:
		status_label.configure(text='No transformation selected.')
	else:
		transformation = transfs[selected[0]]
		status_label.configure(text='Applied a '+transformation+'.')

transfApply_btn.configure(command=transfApply_command)

# row 2
img_label = tk.Label(root, bg='grey', image=imagePreview)
img_label.grid(row=2, column=0, padx=2, columnspan=4, sticky='nesw')

# row 3
status_label = tk.Label(root, text='', anchor='e')
status_label.grid(row = 99, column = 1, padx=2, pady = 3, sticky = "ew")

save_btn = tk.Button(root, text='Save')
save_btn.grid(row=99, column=2, columnspan=2, padx=2, pady=3, sticky = "sew")

def save_command():
	# Save the modified image
	status_label.configure(text='Image saved.')

save_btn.configure(command=save_command)

# last line
root.mainloop()