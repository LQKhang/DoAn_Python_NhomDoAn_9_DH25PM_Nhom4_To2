from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import mysql.connector




#Ket noi MySQL
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="QLThuocNongDuoc"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi MySQL", f"Không thể kết nối MySQL:\n{err}")
        return None

#canh giua cua so
def center_window(win, w=500, h=500):
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")


root = Tk()
root.title('CUA HANG QUAN LY THUOC NONG DUOC')
center_window(root)

Label(root, text="QUẢN LÝ THUỐC NÔNG DƯỢC", font=("Arial", 14, "bold")).grid()

#Listbox(root, width=80, height=20).grid(row= 2)

#creat logo
direstory_path = os.path.dirname(__file__)
path_images = os.path.join(direstory_path, 'images')
root.iconbitmap(os.path.join(path_images, 'meds_bootle_plants_leaf_nature_eco_icon_186002.ico'))

#creat object
frame_info = Frame(root)
frame_info.grid(pady=5, padx=10)

Label(frame_info, text = "Ten san pham").grid(row = 3, column =0, sticky="w")
Entry(frame_info, width=20).grid(row = 3, column = 1, sticky="w")
Label(frame_info, text = "Phan loai").grid(row = 4, column=0, sticky="w")
Entry(frame_info, width=20).grid(row = 4, column=1, sticky="w")
Label(frame_info, text = "Gia").grid(row = 5, column=0, sticky="w")
Entry(frame_info, width=20).grid(row=5, column=1, sticky="w")
Label(frame_info, text = "So luong").grid(row = 6, column=0, sticky="w")
Entry(frame_info, width=20).grid(row=6, column=1, sticky="w")

#
frame_table = Frame(root)
frame_table.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
Label(frame_table, text="Danh sách thuốc", font=("Arial", 10, "bold")).pack(pady=5)

columns = ("Ten san pham", "Phan loai", "Gia", "So luong")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col.capitalize())

tree.column("Ten san pham", width=150, anchor="center")
tree.column("Phan loai", width=150)
tree.column("Gia", width=110, anchor="center")
tree.column("So luong", width=90, anchor="center")

tree.grid(row=6, column=0, sticky="nesw")


#creat nude
frame_btn = Frame(root)
frame_btn.grid(row=8, column=0, pady=10)

# ===== CÁC NÚT =====
Button(frame_btn, text='THÊM', width=10).grid(row=0, column=0, padx=10)
Button(frame_btn, text='XÓA', width=10).grid(row=0, column=1, padx=10)
Button(frame_btn, text='SỬA', width=10).grid(row=0, column=2, padx=10)
Button(frame_btn, text='SẮP XẾP', width=10).grid(row=0, column=3, padx=10)


#creat menu
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = 'FILE', menu = file_menu)

file_menu.add_command(label = 'OPEN')
file_menu.add_command(label = 'SAVE')
file_menu.add_command(label = 'EXIT', command=root.quit)

#unblock kick thuoc
#root.resizable(FALSE, FALSE)
root.mainloop()