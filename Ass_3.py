import tkinter as tk

def file_new():
    print("New File")
    filewin = tk.Toplevel(root)
    filewin.geometry('200x200')
    button = tk.Button(filewin, text="This is New Tab", bg='yellow')
    button.pack()


def file_open():
    print("Open File")
    filewin = tk.Toplevel(root)
    filewin.geometry('200x200')
    button = tk.Button(filewin, text="This is New Tab", bg='yellow')
    button.pack()

def file_save():
    print("Save File")
    print("Open File")
    filewin = tk.Toplevel(root)
    filewin.geometry('200x200')
    button = tk.Button(filewin, text="This is New Tab", bg='yellow')
    button.pack()

root = tk.Tk()


label1 = tk.Label(root, text="Label 1", bg="red")
label1.pack()

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.pack()

# Create menu bar
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Save", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
