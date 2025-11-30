from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from tkcalendar import DateEntry
import os
import mysql.connector

from Do_An_09.Nhap import date_entry


#Kê nối MySQL
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

#Canh giữa cửa sổ
def center_window(win, w=800, h=500):
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

root = tk.Tk()
root.title('CUA HANG QUAN LY THUOC NONG DUOC')
center_window(root)

tk.Label(root, text="QUẢN LÝ THUỐC NÔNG DƯỢC", font=("Arial", 14, "bold")).grid()

#Tạo logo
direstory_path = os.path.dirname(__file__)
path_images = os.path.join(direstory_path, 'images')
root.iconbitmap(os.path.join(path_images, 'meds_bootle_plants_leaf_nature_eco_icon_186002.ico'))

#Tạo thộc tính
frame_info = tk.Frame(root)
frame_info.grid(pady=10, padx=10, sticky="w")

tk.Label(frame_info, text = "Tên sản phẩm").grid(row = 3, column =0, pady=3, padx=40, sticky="w")
entry_tensp = tk.Entry(frame_info, width=20)
entry_tensp.grid(row = 3, column = 1, sticky="w")

tk.Label(frame_info, text = "Phân loại").grid(row = 4, column=0, pady=3, padx=40, sticky="w")
cbb_Phanloai = ttk.Combobox(frame_info, values=["Trừ sâu", "Trừ bệnh", "Trừ cỏ", "Thuốc sinh trưởng"], state="readonly")
cbb_Phanloai.grid(row = 4, column=1, sticky="w")

tk.Label(frame_info, text = "Giá").grid(row = 5, column=0, pady=3, padx=40, sticky="w")
entry_gia = tk.Entry(frame_info, width=20)
entry_gia.grid(row=5, column=1, sticky="w")

tk.Label(frame_info, text = "Số lượng").grid(row = 6, column=0, padx=40, sticky="w")
entry_soluong = tk.Entry(frame_info, width=20)
entry_soluong.grid(row=6, column=1, sticky="w")

tk.Label(frame_info, text = "Thương hiệu").grid(row = 3, column=2, padx=50, sticky="w")
entry_thuonghieu = tk.Entry(frame_info, width=20)
entry_thuonghieu.grid(row=3, column=3, sticky="w")

tk.Label(frame_info, text = "Mã sản phẩm").grid(row = 4, column=2, padx=50, sticky="w")
entry_masanpham = tk.Entry(frame_info, width=20)
entry_masanpham.grid(row=4, column=3, sticky="w")

tk.Label(frame_info, text = "Ngày sản xuất").grid(row = 5, column=2, padx=50, sticky="w")
entry_ngaysanxuat = DateEntry(frame_info, width=20, background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
entry_ngaysanxuat.grid(row=5, column=3, sticky="w")

tk.Label(frame_info, text = "Hạn sử dụng").grid(row = 6, column=2, padx=50, sticky="w")
entry_hansudung = DateEntry(frame_info, width=20, background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
entry_hansudung.grid(row=6, column=3, sticky="w")

'''
frame_search = tk.Frame(root)
frame_search.grid(row=8, column=0, pady=5)
tk.Label(frame_search, text="Tìm theo tên:").pack(side="left")
'''
#

frame_table = tk.Frame(root)
frame_table.grid(row=2, column=0, padx=10, pady=10)
tk.Label(frame_table, text="Danh sách thuốc", font=("Arial", 10, "bold")).pack(pady=5)


#Treeview
columns = ("Tên sản phẩm", "Phân loại", "Giá", "Số lượng", "Thương hiệu", "Mã sản phẩm", "Ngày sản xuất", "Hạn sử dụng")
tree = ttk.Treeview(root, columns = columns, show = "headings")
for col in columns:
    tree.heading(col, text=col.capitalize())

tree.column("Tên sản phẩm", width=100, anchor="center")
tree.column("Phân loại", width=100)
tree.column("Giá", width=100, anchor="center")
tree.column("Số lượng", width=100, anchor="center")
tree.column("Thương hiệu", width=100)
tree.column("Mã sản phẩm", width=100)
tree.column("Ngày sản xuất", width=100)
tree.column("Hạn sử dụng", width=100)

tree.grid(row=6, column=0, sticky="nesw")

#hàm chức năng
def clear_input():
    entry_masanpham.config(state="normal")
    entry_masanpham.delete(0, tk.END)
    entry_tensp.delete(0, tk.END)
    entry_gia.delete(0, tk.END)
    entry_soluong.delete(0, tk.END)
    entry_thuonghieu.delete(0, tk.END)
    entry_ngaysanxuat.set_date("2000-01-01")
    entry_hansudung.set_date("2000-01-01")

    cbb_Phanloai.set("")

def load_data():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()

    tree.delete(*tree.get_children())
    cur.execute("select * from thuocnongduoc")

    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)

    cur.close()
    conn.close()

def them_sp():
    tensp = entry_tensp.get().strip()
    phanloai = cbb_Phanloai.get()
    gia = entry_gia.get().strip()
    soluong = entry_soluong.get().strip()
    thuonghieu = entry_thuonghieu.get().strip()
    masanpham = entry_masanpham.get().strip()
    ngaysanxuat = entry_ngaysanxuat.get()
    hansudung = entry_hansudung.get()


    if tensp == "" or gia == "" or soluong == "" or thuonghieu == "" or masanpham == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập đủ thông tin!")
        return

    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()

    try:
        cur.execute("""
            insert into thuocnongduoc(tensp, phanloai, gia, soluong, thuonghieu, masanpham, ngaysanxuat, hansudung)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (tensp , phanloai, gia, soluong, thuonghieu, masanpham, ngaysanxuat, hansudung))

        conn.commit()
        load_data()
        clear_input()

    except mysql.connector.IntegrityError:
        messagebox.showerror("Lỗi", "Mã số đã tồn tại!")

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

    finally:
        cur.close()
        conn.close()

def on_tree_select(event):
    selected = tree.selection()
    if not selected:
        return
    values = tree.item(selected)["values"]

    entry_tensp.delete(0, tk.END)
    entry_tensp.insert(0, values[0])

    cbb_Phanloai.set(values[1])

    entry_gia.delete(0, tk.END)
    entry_gia.insert(0, values[2])

    entry_soluong.delete(0, tk.END)
    entry_soluong.insert(0, values[3])

    entry_thuonghieu.delete(0, tk.END)
    entry_thuonghieu.insert(0, values[4])

    entry_masanpham.config(state="normal")
    entry_masanpham.delete(0, tk.END)
    entry_masanpham.insert(0, values[5])
    entry_masanpham.config(state="readonly")

    entry_ngaysanxuat.set_date(values[6])

    entry_hansudung.set_date(values[7])

tree.bind("<<TreeviewSelect>>", on_tree_select)

def xoa_sp():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn đối tượng để xóa!")
        return

    masanpham = tree.item(selected)["values"][5]

    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa đối tượng này?"):
        conn = connect_db()
        cur = conn.cursor()

        cur.execute("delete from thuocnongduoc where masanpham=%s", (masanpham,))
        conn.commit()

        cur.close()
        conn.close()
        load_data()
        clear_input()

def luu_sp():
    tensp = entry_tensp.get().strip()
    phanloai = cbb_Phanloai.get()
    gia = entry_gia.get().strip()
    soluong = entry_soluong.get().strip()
    thuonghieu = entry_thuonghieu.get().strip()
    masanpham = entry_masanpham.get().strip()
    ngaysanxuat = entry_ngaysanxuat.get()
    hansudung = entry_hansudung.get()

    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()

    cur.execute("""
        UPDATE thuocnongduoc 
        SET tensp=%s, phanloai=%s, gia=%s, soluong=%s, thuonghieu=%s, ngaysanxuat=%s, hansudung=%s
        WHERE masanpham=%s
    """, (tensp, phanloai, gia, soluong, thuonghieu, ngaysanxuat, hansudung,masanpham))

    conn.commit()
    cur.close()
    conn.close()
    load_data()
    clear_input()
    entry_masanpham.config(state="normal")


def sap_xep():
    global sort

    sort_order = {
        "Trừ sâu": 1,
        "Trừ bệnh": 2,
        "Trừ cỏ": 3,
        "Thuốc sinh trưởng": 4
    }
    data = []
    for item in tree.get_children():
        data.append(tree.item(item)["values"])

    tree.delete(*tree.get_children())
    data.sort(
        key=lambda x: sort_order.get(x[1], 99),
        reverse=False
    )
    for row in data:
        tree.insert("", tk.END, values=row)

def tim_kiem():
    k = entry_search.get().strip()
    if k == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên sản phẩm cần tìm!")
        return

    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()

    q = "select * from thuocnongduoc where tensp like %s"
    cur.execute(q, ("%" + k + "%",))

    rows = cur.fetchall()

    # Xóa dữ liệu hiện tại trên tree
    tree.delete(*tree.get_children())

    # Nếu không có kết quả
    if not rows:
        messagebox.showinfo("Kết quả", "Không tìm thấy sản phẩm phù hợp!")
    else:
        for row in rows:
            tree.insert("", tk.END, values=row)

    cur.close()
    conn.close()

#Tạo nút
frame_btn = tk.Frame(root)
frame_btn.grid(row=8,column = 0, pady=10)

Button(frame_btn, text='THÊM', width=10, command=them_sp).grid(row=0, column=0, padx=5)
Button(frame_btn, text='XÓA', width=10, command=xoa_sp).grid(row=0, column=1, padx=5)
Button(frame_btn, text='HỦY', width=10, command = clear_input).grid(row=0, column=2, padx=5)
Button(frame_btn, text='SẮP XẾP', width=10, command=sap_xep).grid(row=1, column=0, padx=5)
Button(frame_btn, text='LƯU', width=10, command=luu_sp).grid(row=1, column=1, padx=5)
Button(frame_btn, text= 'THOAT', width=10, command=root.quit).grid(row=1, column=2, padx=5)

tk.Label(frame_btn, text = "Nhập tên tìm kiếm").grid(row=0, column=3, padx=5)
entry_search = tk.Entry(frame_btn, width=20)
entry_search.grid(row = 0, column=4, padx=5)

Button(frame_btn, text="TÌM", width=10, command=lambda: tim_kiem()).grid(row = 1, column=3, padx=5)
Button(frame_btn, text="HIỂN THỊ TẤT CẢ", width=14, command=load_data).grid(row = 1, column=4, padx=5)


#Khóa kích thước bảng
#root.resizable(FALSE, FALSE)

#load dữ liệu
load_data()
root.mainloop()