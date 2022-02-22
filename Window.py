# Tkinter GUI experiment for CS 224
# @author Nolan Rapp

from PIL import ImageTk, Image
import tkinter as tk
import os

# first line
root = tk.Tk()
# root setup
root.title('Sunbird')
root.geometry('800x600')
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# default image
imagePath = os.getcwd() + '\\datafiles\\' + 'img00.jpg'
imageOpen = Image.open(imagePath)
imagePreview = ImageTk.PhotoImage(imageOpen)

# define button events, helper methods
def fileChoose_command():
	print("File Choose!")

def fileOpen_command():
	print("File Open!")

def transfApply_command():
	for i in transf_inp.curselection():
		print(transf_inp.get(i))

def save_command():
	print("Save!")

# widgets
# row 1
fileSelect_label = tk.Label(root, text='File Selection:')
fileSelect_label.grid(padx=1, pady=2.5, sticky='we')

fileSelect_inp = tk.Entry(root)
fileSelect_inp.insert(0, imagePath) # default text
fileSelect_inp.grid(row=0, column=1, sticky='we')

fileChoose_btn = tk.Button(root, text='Choose File', command=fileChoose_command)
fileChoose_btn.grid(row=0, column=2, padx=1, pady=3, sticky='we')

fileOpen_btn = tk.Button(root, text='Open File', command=fileOpen_command)
fileOpen_btn.grid(row=0, column=3, padx=1, pady=3, sticky='we')

# row 1
transfs = ['Vertical Streak', 'Horizontal Streak', 'Boost Hue', 'Gaussian Blur']

transf_label = tk.Label(root, text="Transformation:")
transf_label.grid(row=1, column=0, padx=1, pady=3, sticky='we')

transf_inp = tk.Listbox(root, height=1)
transf_inp.grid(row=1, column=1, sticky='we')

transfApply_btn = tk.Button(root, text="Apply", command=transfApply_command)
transfApply_btn.grid(row=1, column=2, padx=1, pady=3, columnspan=2, sticky='we')

for transformation in transfs:
		transf_inp.insert(tk.END, transformation)

# row 2
img_label = tk.Label(root, bg='grey', image=imagePreview)
img_label.grid(row=2, column=0, padx=5, columnspan=4, sticky='nesw')

# row 3
save_btn = tk.Button(root, text='Save', command=save_command)
save_btn.grid(row=99, column=1, pady=5, sticky = "sew")

# last line
root.mainloop()