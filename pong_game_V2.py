"""CÁC BƯỚC ĐỂ TẠO THÀNH 1 CON GAME PONG 
-B1: Tạo cửa sổ trò chơi 
-B2: Tạo 2 thanh chắn 2 bên và gán cho nó khả năng di chuyển và reset để về cuối sử dụng 
-B3: Tạo 1 thanh mà ở giữa màn hình để mà nối đuôi với hình chữ nhật
-B4: Tạo 1 quả bóng và nó có khả năng phản lại với khi đụng nóc trên với dưới của màn hình. 
    Thêm nữa là khả năng khi nó va chạm với thanh chắn thì càng gần tới góc thì góc phản lại sẽ có góc độ càng lớn và sẽ không vượt quá tốc độ tối đa của quả bóng
-B5: Hiện điểm với khi quả bóng chả ra khỏi màn hình trái phải thì cộng thêm điểm 
-B6: Là khi người chơi bên nào đã trước 10 điểm thì sẽ chiến thắng rồi hiện dòng chữ thông báo chiến thắng của người đó trong 5 giây rồi sẽ bắt đầu lại 1 ván hoàn toàn mới""" 

import pygame 
import time
import os 
pygame.init() 
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500 
WINDOW_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption("Pong Game Remake") 
clock = pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255,255,255)
AQUA = 	(0,255,255) # For a ball 
GOLD = (255,215,0) # For paddles 


def main():
    clock.tick(60) 
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                break
    
    pygame.quit()



if __name__ == "__main__": 
    main()

