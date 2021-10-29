import tkinter

root = tkinter.Tk()

# def hello():
#     tkinter.Label(root, text="Hello World").pack()
#
# tkinter.Button(root, text="Submit", command=hello).pack()
# var = tkinter.Entry(root,)
# var.pack()

def Left_click(event):
    tkinter.Label(root, text ="left click").pack()

def Right_click(event):
    tkinter.Label(root, text ="right click").pack()

def clicker(event):
    tkinter.Label(root, text ="You press "+event.keysym).pack()

root.bind("<Button-1>", Left_click)
root.bind("<Key>", clicker)
root.bind("<Button-3>", Right_click)


root.mainloop()