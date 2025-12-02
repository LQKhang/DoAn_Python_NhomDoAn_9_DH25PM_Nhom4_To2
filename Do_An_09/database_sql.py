import mysql.connector

#Đăng nhập MySQL
dp = mysql.connector.connect(user = 'root', password = '123456', host = 'localhost')

#Tạo database
code = ("""
        create schema `qlthuocnongduoc`
        CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci;
        """
)

#Tạo table
create_table = """
CREATE TABLE `qlthuocnongduoc`.`thuocnongduoc` (
    tensp VARCHAR(50),
    phanloai VARCHAR(30),
    gia FLOAT,
    soluong INT,
    thuonghieu VARCHAR(50),
    masanpham CHAR(20),
    ngaysanxuat DATE,
    hansudung DATE,
    PRIMARY KEY (masanpham)
);
"""

#chạy code
mycursor = dp.cursor()
mycursor.execute(code)
mycursor.execute(create_table)
dp.commit()

# Đóng kết nối
mycursor.close()
mycursor.close()



