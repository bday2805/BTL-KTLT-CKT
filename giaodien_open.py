import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
from tkinter import messagebox
import ctypes

from nhac import play_music,stop_music
from giaodien_setting import open_settings

# Hàm để bắt đầu trò chơi khi nhấn nút "Play"
def start_game():
    # Ẩn nút Play và thay đổi trạng thái giao diện
    play_button.pack_forget()
    # Hiển thị một thông báo bắt đầu trò chơi
    messagebox.showinfo("Trò chơi bắt đầu", "Chúc bạn chơi vui vẻ!")


ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Đảm bảo tỷ lệ DPI chính xác

# Tạo cửa sổ chính với kích thước 1920x1080
root = tk.Tk()
root.title("Game Python")

# Kích thước cửa sổ
width, height = 1920, 1080
root.geometry(f"{width}x{height}")
play_music('music\sound.mp3', loop=True)
root.resizable(False, False)

# Tải hình nền
background_image = Image.open("source\start_background.png")
background_image = background_image.resize((width, height), Image.Resampling.LANCZOS)  # Điều chỉnh kích thước hình ảnh
background_tk = ImageTk.PhotoImage(background_image)

# Tạo Canvas để vẽ
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
# Hiển thị hình nền
canvas.create_image(0, 0, image=background_tk, anchor="nw")

# Tải hình ảnh logo
logo_image = Image.open("source\logo_icon.png")
logo_image = logo_image.resize((192*9, 108*9), Image.Resampling.LANCZOS)  # Điều chỉnh kích thước logo
logo_tk = ImageTk.PhotoImage(logo_image)

# Hiển thị logo ở vị trí trên cùng
logo_id = canvas.create_image(width // 2, -150, image=logo_tk, anchor="n")  # Logo nằm giữa màn hình, phía trên cùng
# Đảm bảo logo luôn ở trên cùng
canvas.tag_raise(logo_id)

# Tải hình ảnh nút Play
play_image = Image.open("source\play_icon.png")
play_image = play_image.resize((593 ,190 ), Image.Resampling.LANCZOS)  # Điều chỉnh kích thước nút
play_tk = ImageTk.PhotoImage(play_image)

# Thêm nút Play vào Canvas
play_button = tk.Button(root, image=play_tk, bg="#ffe6e6", bd=0, highlightthickness=0, relief="flat", activebackground="#ffe6e6", command=start_game)
canvas.create_window(width // 2, int(height * 0.7), window=play_button, anchor="center")

# Sound Setting
# Hàm chuyển đổi âm thanh
def toggle_sound():
    global is_muted
    if is_muted:
        # Chuyển sang trạng thái phát nhạc
        play_music('music\sound.mp3', loop=True)
        sound_button.config(image=play_tk2)
        is_muted = False
    else:
        # Chuyển sang trạng thái tắt nhạc
        stop_music()
        sound_button.config(image=play_tk4)
        is_muted = True

# Load hình ảnh âm thanh
unmute = Image.open("source\sound_icon.png").resize((120, 120), Image.Resampling.LANCZOS)
play_tk2 = ImageTk.PhotoImage(unmute)

mute = Image.open("source\mute_icon.png").resize((120, 120), Image.Resampling.LANCZOS)
play_tk4 = ImageTk.PhotoImage(mute)

# Biến trạng thái
is_muted = False

# Tạo nút và thêm vào cửa sổ
sound_button = Button(
    root,
    image=play_tk2,  # Hình ảnh ban đầu là unmute
    bg="#ffe6e6",
    bd=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#ffe6e6",
    command=toggle_sound
)
sound_button.place(relx=0.89, rely=0.065, anchor="center")


# Tải hình ảnh nút setting
play_image3 = Image.open("source\setting_icon.png")
play_image3 = play_image3.resize((30*4, 30*4), Image.Resampling.LANCZOS)  # Kích thước nhỏ hơn
play_tk3 = ImageTk.PhotoImage(play_image3)

# Thêm nút setting vào góc màn hình
play_button3 = tk.Button(root, image=play_tk3, bg="#ffe6e6", bd=0, highlightthickness=0, relief="flat", activebackground="#ffe6e6", command=lambda: open_settings(root))
play_button3.place(relx=0.96, rely=0.065, anchor="center")  # Đặt ở góc màn hình
# Chạy vòng lặp chính của game
root.mainloop()