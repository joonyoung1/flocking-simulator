import pygame


class Slider:
    def __init__(self, pos, size, min_val, max_val, value, name):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.name = name

        self.min_val = min_val
        self.max_val = max_val
        self.gap = max_val - min_val

        self.scroll = value / self.gap * self.width
        self.activated = False
        
    def clicked(self, x, y):
        return self.x < x < self.x + self.width and self.y - 20 < y < self.y + self.height + 20
    
    def draw(self, screen):
        clicked = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (50, 50, 50), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (50, 50, 50), (self.x + self.scroll - 7, self.y - 15, 14, 30))

        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        title = font.render(self.name, True, (255, 0, 0))
        title_rect = title.get_rect(midbottom=(self.x + self.width / 2, self.y - 20))
        screen.blit(title, title_rect)
        
        if clicked[0] and self.clicked(*mouse):
            self.scroll = mouse[0] - self.x
    
    def get_value(self):
        return self.scroll / self.width * self.gap

