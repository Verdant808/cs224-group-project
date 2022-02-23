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

# default image
path = os.getcwd() + os.path.sep + 'datafiles'
imageNames = os.listdir(path)
imagePath = path + os.path.sep + imageNames[2]
imageOpen = Image.open(imagePath)
imagePreview = ImageTk.PhotoImage(imageOpen)

# define button events, helper methods
def dirChoose_command():
	print("File Choose!")

def dirOpen_command():
	print(fileSelect_inp.get())

def transfApply_command():
	for i in transf_inp.curselection():
		print(transf_inp.get(i))

def save_command():
	print("Save!")

# widgets
# row 1
dirSelect_label = tk.Label(root, text='Directory:', anchor='e')
dirSelect_label.grid(padx=1, pady=2.5, sticky='we')

dirSelect_inp = tk.Entry(root)
dirSelect_inp.insert(0, imagePath) # default text
dirSelect_inp.grid(row=0, column=1, sticky='we')

dirChoose_btn = tk.Button(root, text='Select', command=dirChoose_command)
dirChoose_btn.grid(row=0, column=2, padx=2, pady=3, sticky='we')

dirOpen_btn = tk.Button(root, text='Open', command=dirOpen_command)
dirOpen_btn.grid(row=0, column=3, padx=2, pady=3, sticky='we')

# row 1
transfs = ['Vertical Streak', 'Horizontal Streak', 'Boost Hue', 'Gaussian Blur']

transf_label = tk.Label(root, text='Transformation:', anchor='e')
transf_label.grid(row=1, column=0, padx=2, pady=3, sticky='we')

transf_inp = tk.Listbox(root, height=1)
transf_inp.grid(row=1, column=1, sticky='we')

transfApply_btn = tk.Button(root, text="Apply", command=transfApply_command)
transfApply_btn.grid(row=1, column=2, padx=2, pady=3, columnspan=2, sticky='we')

for transformation in transfs:
		transf_inp.insert(tk.END, transformation)

# row 2
img_label = tk.Label(root, bg='grey', image=imagePreview)
img_label.grid(row=2, column=0, padx=2, columnspan=4, sticky='nesw')

# row 3
status_label = tk.Label(root, text='', anchor='e')
status_label.grid(row = 99, column = 1, padx=2, pady = 3, sticky = "ew")

save_btn = tk.Button(root, text='Save', command=save_command)
save_btn.grid(row=99, column=2, columnspan=2, padx=2, pady=3, sticky = "sew")

# last line
root.mainloop()