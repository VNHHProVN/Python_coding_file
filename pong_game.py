# import pygame 
# import os 
# import random 
# import time 

# # Khởi tạo game
# pygame.init() 
# WINDOW_WIDTH, WINDOW_HEIGHT = 980, 630 
# PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100 
# BALL_RADIUS = 7
# window_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
# pygame.display.set_caption("Pong Game Remake") 
# clock = pygame.time.Clock()
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0) 
# RED = (255, 0, 0) 
# SCORE_FONT = pygame.font.SysFont("comicsans", 50) # Giá trị đầu trong ngoặc là kiểu chữ mà ta muốn nó hiểu với giá trị thứ hai là kích thước của chữ
# WINNING_SCORE = 10
# # Tạo 2 thanh 2 bên của game Pong 
# class Paddle: 
#     # Add color to the paddle 
#     COLOR = GREEN
#     # Thêm tốc độ di chuyển của thanh 
#     VEL = 0.7
#     def __init__(self, x, y, width, height):
#         self.x = self.original_x = x 
#         self.y = self.original_y = y 
#         self.width = width 
#         self.height = height 
#     def draw(self, win): # Vẽ thanh ra màn hình với màu với vị trí
#         pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height)) 
#     def movement(self, up = True): # Tạo logic để thanh được đi LÊN
#         if up: 
#             self.y -=  self.VEL 
#         else: 
#             self.y += self.VEL 
#     def reset(self): 
#         self.x = self.original_x 
#         self.y = self.original_y 


# # Hàm để vẽ ra màn hình
# def draw(win, paddles, ball, left_score, right_score):
#     win.fill(BLACK) 
#     # Hiện ra điểm số trên màn hình 
#     left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
#     right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
#     win.blit(left_score_text, (WINDOW_WIDTH // 4 - left_score_text.get_width() // 2, 20))
#     win.blit(right_score_text, (WINDOW_WIDTH * (3/4) - right_score_text.get_width() // 2, 20))
#     for paddles in paddles: # Nơi nhập điều kiện để vẽ các thanh trong game Pong
#         paddles.draw(win) 
#     # Vẽ cái thanh ở giữa màn hình là các hình chữ nhật kích thước nhỏ và có khoảng cách ra 
#     for i in range(10, WINDOW_HEIGHT, WINDOW_HEIGHT // 20): 
#         # in range(x, y, z): => x: giá trị bắt đầu; y: giá trị cuối cùng để giá trị bắt đầu đến đích; z: số bước nhảy tức là mỗi giá trị cách nhau một khoảng giá trị nhiêu đó
#         if i % 2 == 1: 
#             continue
#         pygame.draw.rect(win, WHITE, (WINDOW_WIDTH // 2 - 5, i, 10, WINDOW_HEIGHT // 20))
#         # WINDOW_WIDTH // 2 - 5 tọa độ x mà nó nằm ở giữa màn hình đi xuống dưới cùng luôn và tại sao trừ đi 5 thì nếu không thì tọa độ x mà có chiều dài là 10 thì nó sẽ đặt cái góc trái trên cùng ngay tại điểm trung tâm luôn và chính giữa của chiều ngang hình chữ nhật nó sẽ bị lệch sang một bên phải và ta phải trừ đi 5 để nó nhích sang trái 5 pixel để nó nằm giữa
#         # i là giá trị mà ta sẽ vẽ nó xuống theo tọa độ y 
#         # 10 là chiều ngang của hình chữ nhật 
#         # WINDOW_HEIGHT // 20 là chiều dọc của hình chữ nhật 
#     ball.draw(win)
#     pygame.display.update()

# # Va chạm cho quả bóng với 2 thanh phản lại 2 bên với chiều ngang trên dưới của màn hình
# def handle_collision(ball, left_paddle, right_paddle):
#     # Va chạm với màn hình
#     if ball.y + ball.radius >= WINDOW_HEIGHT: 
#         ball.y_vel *= -1 
#     elif ball.y - ball.radius <= 0: 
#         ball.y_vel *= -1 
#     # Va chạm với 2 thanh phản lại quả bóng 
#     # Thanh chắn bên trái:
#     if ball.x_vel < 0: # Là nó đang đi về hướng thanh chắn bên trái
#         if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height: 
#                     # left_paddle.y là cạnh trên cùng của thanh chắn bên trái
#                     # left_paddle.y + left_paddle.height là cạnh dưới cùng của thanh chắn bên trái
#             if ball.x - ball.radius <= left_paddle.x + left_paddle.width: 
#                 # ball.x - ball.radius là cạnh bên trái của quả bóng
#                 # left_paddle.x + left_paddle.width là cạnh bên phải của quả bóng
#                 ball.x_vel *= -1 
#                 # Phần này sẽ làm va chạm vào thanh chắn BÊN TRÁI khi mà chạm vào càng xa trung tâm thì hướng nó bật lại sẽ đa dạng hơn ví dụ nếu chạm vào gần góc trên cùng của thanh chắn thì nó sẽ bật lên trên và ngược lại
#                 middle_y = left_paddle.y + left_paddle.height / 2 # Khoảng cách của thanh bên trái tính từ cạnh trên cùng đến trung tâm của đỉnh
#                 different_in_y = middle_y - ball.y # Khoảng cách từ tâm của trái bóng để trung tâm của thanh bên trái 
#                 reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL 
                
#                 # Mục đích: Tạo ra một hệ số điều chỉnh. Nó hoạt động như một "cầu nối" chuyển đổi từ khoảng cách (pixel) sang một vận tốc (pixel/khung hình) nằm trong giới hạn mong muốn
#                 #         - Hệ số này dùng để chuẩn hóa (scale) giá trị difference_in_y thành một vận tốc hợp lý, đảm bảo vận tốc theo trục Y của bóng không bao giờ vượt quá giá trị MAX_VEL (vận tốc tối đa đã định nghĩa).

#                 # Cách hoạt động: Nó tạo ra một tỉ lệ giữa khoảng cách va chạm tối đa (nửa chiều cao vợt) và vận tốc tối đa.
#                 # Nếu không có tỉ lệ xích này (reduction_factor), tốc độ sẽ căn cứ thẳng vào chiều dài thanh chắn. Một va chạm cách tâm 40 pixels sẽ tạo ra vận tốc 40 pixels/khung hình. Điều này khiến tốc độ tăng lên một cách không được chuẩn hóa và khó cân bằng, nó hoàn toàn phụ thuộc vào kích thước pixel của vật thể trong game.

#                 y_vel = different_in_y / reduction_factor 

                
#                 ball.y_vel = y_vel * -1
#     else: # Thanh chắn bên phải: 
#         if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height: 
#             # right_paddle.y là cạnh trên cùng của thanh chắn bên phải 
#             # right_paddle.y + right_paddle.height là cạnh dưới cùng của thanh chắn bên phải
#             if ball.x + ball.radius >= right_paddle.x: 
#                 # ball.x + ball.radius là cạnh bên phải của quả bóng 
#                 # right_paddle.x là cạnh bên trái của thanh chắn bên phải
#                 ball.x_vel *= -1 
#                 # Phần này sẽ làm va chạm vào thanh chắn BÊN PHẢI khi mà chạm vào càng xa trung tâm thì hướng nó bật lại sẽ đa dạng hơn ví dụ nếu chạm vào gần góc trên cùng của thanh chắn thì nó sẽ bật lên trên và ngược lại
#                 middle_y = right_paddle.y - right_paddle.height / 2 
#                 different_in_y = middle_y - ball.y 
#                 reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL 
#                 y_vel = different_in_y / reduction_factor
#                 ball.y_vel = y_vel * -1


# def handle_paddle_movement(keys, left_paddle, right_paddle): 
#     # Di chuyển cho thanh bên trái
#     if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
#        left_paddle.movement(up = True)
#     if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= WINDOW_HEIGHT:
#        left_paddle.movement(up = False)

#     # Di chuyển cho thanh bên phải 
#     if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0: 
#         right_paddle.movement(up = True)
#     if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= WINDOW_HEIGHT: 
#         right_paddle.movement(up = False)
    
# class Ball: 
#     MAX_VEL = 0.6
#     COLOR = RED
    
#     def __init__(self, x, y, radius): # radius là bán kính của hình tròn
#         self.x = self.original_x = x 
#         self.y = self.original_y = y 
#         self.radius = radius 
#         self.x_vel = self.MAX_VEL
#         self.y_vel = 0 
#     def draw(self, win): 
#         pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius) 
#     def move(self):
#         self.x += self.x_vel 
#         self.y += self.y_vel 
#     def reset(self):
#         self.x = self.original_x
#         self.y = self.original_y 
#         self.y_vel = 0 
#         self.x_vel *= -1
    

        

# def main():
#     clock.tick(60) # Số FPS
#     left_paddle = Paddle(10, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT) 
#     right_paddle = Paddle(WINDOW_WIDTH - 10 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
#     ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BALL_RADIUS) 
#     left_score = 0 
#     right_score = 0 
    
#     running = True 
#     while running: 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False 
#         # Bắt đầu gán các phím ấn để di chuyển
#         keys = pygame.key.get_pressed() 
#         handle_paddle_movement(keys, left_paddle, right_paddle)
#         draw(window_display, [left_paddle, right_paddle], ball, left_score, right_score) # Vẽ những thứ mà tôi đã cập nhật trên từng khung hình
#         ball.move()
#         handle_collision(ball, left_paddle, right_paddle)
#         # Nơi thiết lập logic để tăng số điểm khi mà quả bóng đi ra khỏi màn hình
       
#         if ball.x < 0: 
#             right_score += 1 
#             ball.reset()
#         elif ball.x > WINDOW_WIDTH: 
#             left_score += 1 
#             ball.reset() 

#         # Thiết lập khi người chơi đạt đủ 10 điểm thì sẽ tạm dừng và reset lại trò chơi
#         won = False 
#         if left_score >= WINNING_SCORE:
#             won = True 
#             win_text = "Left Player is the winner!"
#         elif right_score >= WINNING_SCORE: 
#             won = True 
#             win_text = "Right Player is the winner!"

#         if won: 
#             text_for_the_winner = SCORE_FONT.render(win_text, 1, RED)
#             window_display.blit(text_for_the_winner, (WINDOW_WIDTH // 2 - text_for_the_winner.get_width() // 2, WINDOW_HEIGHT // 2 - text_for_the_winner.get_height() // 2))
#             pygame.display.update()
#             pygame.time.delay(5000)
#             ball.reset()
#             left_paddle.reset()
#             right_paddle.reset()
#             left_score = 0 
#             right_score = 0 

            
#     pygame.quit() 

# if __name__ == '__main__':
#     main()
    

    
""" Các bước để làm con game Pong:
    -B1: Tạo cửa sổ với tô màu cho cửa sổ theo ý muốn của mình 
    -B2: Tạo thanh di chuyển với vị trí mà ta muốn nó xuất hiện trên mà hình 
    -B3: Rồi tạo khả năng di chuyển cho thanh 
    -B4: Tạo cái trái bóng để 2 thanh có thể truyền qua lại 
    -B5: Thêm va chạm vào giữa trái banh với thanh phản quả bóng
    -B6: Thêm điểm số vào game
    -B7: Là giới hạn điểm ở mức 10 và hiện tên người chiến thắng nếu bên nào có 10 điểm trước"""