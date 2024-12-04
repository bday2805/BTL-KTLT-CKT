import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Đảm bảo tỷ lệ DPI chính xác

# Tạo cửa sổ chính với kích thước 1920x1080
root = tk.Tk()
root.title("Game Python")

# Kích thước cửa sổ
width, height = 1920, 1080
root.geometry(f"{width}x{height}")

root.resizable(False, False)

# Tải hình nền
background_image = Image.open("end_background.jpg")
background_image = background_image.resize((width, height), Image.Resampling.LANCZOS)  # Điều chỉnh kích thước hình ảnh
background_tk = ImageTk.PhotoImage(background_image)

# Tạo Canvas để vẽ
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
# Hiển thị hình nền
canvas.create_image(0, 0, image=background_tk, anchor="nw")
# Tải hình ảnh nút sound
play_image2 = Image.open("home_icon.png")
play_image2 = play_image2.resize((30*5, 30*5), Image.Resampling.LANCZOS)  # Kích thước nhỏ hơn
play_tk2 = ImageTk.PhotoImage(play_image2)

# Thêm nút sound vào góc màn hình
play_button2 = tk.Button(root, image=play_tk2, bg="#ffffff", bd=0, highlightthickness=0, relief="flat", activebackground="#ffffff")
play_button2.place(relx=0.95, rely=0.07, anchor="center")  # Đặt ở góc màn hình

root.mainloop()