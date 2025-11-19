from tkinter import *
import os

root = Tk()
root.title('CUA HANG QUAN LY THUOC NONG DUOC')
root.geometry("500x500")
Listbox(root, width=80, height=20).grid(row= 0, columnspan=15)

#creat logo
direstory_path = os.path.dirname(__file__)
path_images = os.path.join(direstory_path, 'images')
root.iconbitmap(os.path.join(path_images, 'meds_bootle_plants_leaf_nature_eco_icon_186002.ico'))

Label(root, text = "Ten san pham").grid(row = 1, column =0)
Entry(root, width=30).grid(row = 1, column = 1)
Label(root, text = "Phan loai").grid(row = 2, column=0)
Entry(root, width=30).grid(row = 2, column=1)
Label(root, text = "Gia").grid(row = 3, column=0)
Entry(root, width=30).grid(row=3, column=1)
Label(root, text = "So luong").grid(row = 4, column=0)
Entry(root, width=30).grid(row=4, column=1)

Button(root, text = 'THEM', width=7).grid(row=1, column=2)
Button(root, text = 'XOA', width=7).grid(row=2, column=2)
Button(root, text = 'SUA', width=7).grid(row=3, column=2)
Button(root, text = 'SAP_XEP', width=7).grid(row=4, column=2)

my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = 'FILE', menu = file_menu)

file_menu.add_command(label = 'OPEN')
file_menu.add_command(label = 'SAVE')
file_menu.add_command(label = 'EXIT', command=root.quit)


root.resizable(FALSE, FALSE)
root.mainloop()