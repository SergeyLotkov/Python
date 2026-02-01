import pygame
import random

class Snake:
    def __init__(self):
        self.head_x = 100
        self.head_y = 100
        self.size = 50
        self.body = [pygame.Rect(self.head_x, self.head_y, self.size, self.size)]
        self.direction = "RIGHT"
        self.head_color = (0, 255, 0)  # зеленый
        
        # Для анимации перелива
        self.color_offset = 0
        self.color_speed = 0.05
        
        # Палитра цветов для перелива
        self.color_palette = [
            (255, 0, 0),    # красный
            (0, 255, 0),    # зеленый
            (0, 0, 255)     # синий
        ]

    def get_interpolated_color(self, position):
        total_colors = len(self.color_palette)
        global_position = position + self.color_offset
        
        # Находим между какими цветами находимся
        color_index = int(global_position) % total_colors
        next_color_index = (color_index + 1) % total_colors
        blend_factor = global_position - int(global_position)
        
        # Интерполируем между двумя цветами
        color1 = self.color_palette[color_index]
        color2 = self.color_palette[next_color_index]
        
        # Ограничиваем значения в диапазоне 0-255
        r = max(0, min(255, int(color1[0] + (color2[0] - color1[0]) * blend_factor)))
        g = max(0, min(255, int(color1[1] + (color2[1] - color1[1]) * blend_factor)))
        b = max(0, min(255, int(color1[2] + (color2[2] - color1[2]) * blend_factor)))
        
        return (r, g, b)

    def draw(self, screen):
        self.color_offset += self.color_speed
        
        for i, segment in enumerate(self.body):
            if i == 0:
                pygame.draw.rect(screen, self.head_color, segment)
            else:
                # Для обратного направления можно также изменить множитель
                segment_color = self.get_interpolated_color((len(self.body) - i) * 0.3)
                pygame.draw.rect(screen, segment_color, segment)

    def move(self):
        old_head = self.body[0].copy()
        if self.direction == "RIGHT":
            old_head.x += self.size 
        elif self.direction == "LEFT":
            old_head.x -= self.size 
        elif self.direction =="UP":
            old_head.y -= self.size
        elif self.direction == "DOWN":
            old_head.y += self.size

        self.body.insert(0, old_head)
        self.body.pop()

    def change_direction(self, new_direction):
        if new_direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
            self.direction = new_direction

    def grow(self):
        tail = self.body[-1].copy()
        self.body.append(tail)

class Food:
    def __init__(self, screen_width, screen_hight, size = 50):
        self.size = size
        self.screen_width = screen_width
        self.screen_hight = screen_hight
        self.color = (215, 0, 200)
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, (self.screen_width - self.size) // self.size) * self.size
        y = random.randint(0, (self.screen_hight - self.size) // self.size) * self.size
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


def main():
    pygame.init()
    screen_wight = 1000
    screen_hight = 800
    screen = pygame.display.set_mode((screen_wight, screen_hight))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(screen_wight, screen_hight)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
                
        snake.move()

        if snake.body[0].colliderect(food.rect):
            snake.grow()
            food.randomize_position()


        screen.fill((0, 0, 0))
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()
        snake_length = len(snake.body)
        if snake_length > 10:
            clock.tick(12)
        elif snake_length > 5:
            clock.tick(10)
        else:
            clock.tick(6)
            food.color = ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))



if __name__ == "__main__":
    main()


