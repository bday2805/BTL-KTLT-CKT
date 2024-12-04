import pygame
import game_config as gc
from pygame import display, event
from time import sleep
from animal import Animal
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
# Đường dẫn tới hình ảnh nền
BACKGROUND_IMAGE_PATH = 'source\choi.png'

def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index

pygame.init()
display.set_caption('Game')

# Tạo cửa sổ với kích thước 1920x1080
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_HEIGHT)) 

# Tải hình ảnh nền và thay đổi kích thước cho phù hợp với màn hình mới
background = pygame.image.load(BACKGROUND_IMAGE_PATH)
background = pygame.transform.scale(background, (gc.SCREEN_SIZE, gc.SCREEN_HEIGHT))  # Thay đổi kích thước

running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images_displayed = []

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, col, index = find_index_from_xy(mouse_x, mouse_y)
            if index not in current_images_displayed:
                if len(current_images_displayed) > 1:
                    current_images_displayed = current_images_displayed[1:] + [index]
                else:
                    current_images_displayed.append(index)

    # Vẽ nền trước
    screen.blit(background, (0, 0))  # Vẽ hình nền vào vị trí (0, 0)

    total_skipped = 0

    # Vẽ các ô vật phẩm lên nền
    for i, tile in enumerate(tiles):
        current_image = tile.image if i in current_images_displayed else tile.box
        if not tile.skip:
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped += 1

    display.flip()

    # Kiểm tra các cặp vật phẩm
    if len(current_images_displayed) == 2:
        idx1, idx2 = current_images_displayed
        sleep(0.5)  # Tạm dừng để hiển thị ảnh trong 0.5 giây

        if tiles[idx1].name == tiles[idx2].name:
            # Nếu giống nhau, đánh dấu là đã ghép
            tiles[idx1].skip = True
            tiles[idx2].skip = True
        else:
            # Nếu không giống nhau, ẩn cả hai ô
            current_images_displayed = []

        # Xóa danh sách hình ảnh hiện tại để chuẩn bị cho lượt tiếp theo
        current_images_displayed = []

    # Kết thúc game khi tất cả các ô đã được ghép
    if total_skipped == len(tiles):
        running = False

print('Goodbye!')
