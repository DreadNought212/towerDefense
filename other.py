import pygame

class Inscription():
    def __init__(self, x, y, window_width, window_height, font, font_size, text, color, draw_delay, isDisappear, move_x, move_y):
        self.x = x
        self.y = y
        self.window_width = window_width
        self.window_height = window_height
        self.font = font
        self.font_size = font_size
        self.text = text
        self.draw_delay = draw_delay
        self.current_delay = 0
        self.color = color
        self.isDisappear = isDisappear
        self.move_x = move_x
        self.move_y = move_y

def inscription_update(list):
    for insc in list:
        insc.x += insc.move_x
        insc.y += insc.move_y

def draw_inscription(list, surface):
    for insc in list:
        if insc.current_delay <= insc.draw_delay:
                surface.blit(pygame.font.Font(insc.font, insc.font_size).render(insc.text, 0, insc.color), (insc.x, insc.y))
        else:
            list.remove(insc)
        insc.current_delay += insc.isDisappear
    return list

title_filename = pygame.image.load('title.png')

class Title():
    def __init__(self, window_width, window_height, base_value):
        self.window_width = window_width
        self.window_height = window_height
        self.base_value = base_value
        self.width = window_width // 2
        self.height = window_height // 2
        self.image = pygame.transform.scale(title_filename, (self.width, self.height))
        self.x = self.window_width // 2 - self.width // 2
        self.y = self.window_height // 2 - self.height
        self.top_y = self.y
        self.bot_y = self.top_y + self.base_value
        self.move_y = 1


    def draw_title(self, surface):
        if self.y == self.top_y:
            self.move_y = 1
        elif self.y == self.bot_y:
            self.move_y = -1
        self.y += self.move_y

        surface.blit(self.image, (self.x, self.y))

class Button():
    def __init__(self, window_width, window_height, base_value, x, y, func, mouse_pos):
        self.window_width = window_width
        self.window_height = window_height
        self.x = x
        self.y = y
        self.base_value = base_value
        self.width = window_width // 4
        self.height = window_height // 4
        self.image = pygame.transform.scale(title_filename, (self.width, self.height))
        self.mouse_pos = mouse_pos
        self.func = func

    def draw_button(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Footer():
    def __init__(self, window_width, window_height, base_value, footer_filename):
        self.footer_filename = footer_filename
        self.window_width = window_width
        self.window_height = window_height
        self.base_value = base_value
        self.width = self.window_width
        self.height = self.base_value
        self.image = pygame.transform.scale(footer_filename, (self.width, self.height))
        self.x = 0
        self.y = self.window_height - self.base_value

    def draw_footer(self, surface):
        surface.blit(self.image, (self.x, self.y))



