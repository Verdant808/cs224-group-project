# import tkinter as tk

# # Top level window
# frame = tk.Tk()
# frame.title("TextBox Input")
# frame.geometry('400x200')
# # Function for getting Input
# # from textbox and printing it
# # at label widget

# def printInput():
# 	inp = inputtxt.get(1.0, "end-1c")
# 	lbl.config(text = "Provided Input: "+inp)

# # TextBox Creation
# inputtxt = tk.Text(frame,
# 				height = 5,
# 				width = 20)

# inputtxt.pack()

# # Button Creation
# printButton = tk.Button(frame,
# 						text = "Print",
# 						command = printInput)
# printButton.pack()

# # Label Creation
# lbl = tk.Label(frame, text = "")
# lbl.pack()
# frame.mainloop()


from tkinter import Tk, Label, Entry, StringVar

app = Tk()

labelText=StringVar()
labelText.set("Enter directory of log files")
labelDir=Label(app, textvariable=labelText, height=4)
labelDir.grid(row=1,column=1)

directory=StringVar(None)
dirname=Entry(app,textvariable=directory,width=50)
dirname.grid(row=1,column=2)

app.mainloop()