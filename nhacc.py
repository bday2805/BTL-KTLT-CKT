import pygame

# Khởi tạo pygame
pygame.init()

# Khởi tạo mixer để xử lý âm thanh
pygame.mixer.init()

# Tải tệp âm thanh (đảm bảo đường dẫn đúng)
pygame.mixer.music.load(r"C:\Users\Administrator\PycharmProjects\PythonProject\BTL KTLT\sound.mp3")

# Phát âm thanh
pygame.mixer.music.play()

# Giữ chương trình chạy để nghe âm thanh
while pygame.mixer.music.get_busy():  # Kiểm tra xem âm thanh còn đang phát không
    pygame.time.Clock().tick(10)
