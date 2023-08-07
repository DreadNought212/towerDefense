import pygame
from other import Inscription

class Mob(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height, mob_filename, sprite_delay, num_of_cadr, num_of_right, num_of_left,
                 num_of_up, num_of_down, health, base_value, delay_before_appearance, cost):
        pygame.sprite.Sprite.__init__(self)
        self.window_height = window_height
        self.window_width = window_width
        self.width = base_value
        self.height = base_value
        self.base_value = base_value
        self.x = -self.base_value
        self.y = self.base_value
        self.center_x = self.x + self.width // 2
        self.center_y = self.y + self.height // 2
        self.num_of_cadr = num_of_cadr
        self.surface_image = pygame.Surface((self.width, self.height))
        self.image = pygame.transform.scale(mob_filename, (self.width * self.num_of_cadr, self.height * 4))
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))
        self.health = health
        self.x_speed = 1
        self.y_speed = 0
        self.route_step = 0
        self.num_of_right = num_of_right
        self.num_of_left = num_of_left
        self.num_of_up = num_of_up
        self.num_of_down = num_of_down
        self.delay_before_appearance = delay_before_appearance
        self.x_sprite = 0
        self.y_sprite = -self.base_value * self.num_of_right
        self.sprite_delay = sprite_delay
        self.current_sprite_delay = 0
        self.current_health = self.health
        self.cost = cost


def mobs_creating(level_mobs_list, window_width, window_height, mob_filenames_list, base_value):
    mob_list = []
    delay_before_appearance = 0
    for mob in level_mobs_list:
        if mob == 'pony':
            num_of_sprite = 1
            health = 50
            num_of_cadr = 3
            num_of_right = 2
            num_of_left = 1
            num_of_up = 3
            num_of_down = 0
            cost = 50
            sprite_delay = 10
        if mob == 'ghost':
            num_of_sprite = 2
            health = 25
            num_of_cadr = 3
            num_of_right = 2
            num_of_left = 1
            num_of_up = 3
            num_of_down = 0
            cost = 50
            sprite_delay = 10
        if mob == 'minecrafter':
            num_of_sprite = 3
            health = 100
            num_of_cadr = 4
            num_of_right = 2
            num_of_left = 1
            num_of_up = 3
            num_of_down = 0
            cost = 50
            sprite_delay = 10
        if mob == 'trump':
            num_of_sprite = 4
            health = 5
            num_of_cadr = 6
            num_of_right = 1
            num_of_left = 3
            num_of_up = 2
            num_of_down = 0
            cost = 50
            sprite_delay = 10
        if mob == 'skeleton':
            num_of_sprite = 5
            health = 40
            num_of_cadr = 9
            num_of_right = 3
            num_of_left = 1
            num_of_up = 0
            num_of_down = 2
            cost = 50
            sprite_delay = 10
        if mob == 'boss':
            num_of_sprite = 6
            health = 140
            num_of_cadr = 9
            num_of_right = 3
            num_of_left = 1
            num_of_up = 0
            num_of_down = 2
            cost = 150
            sprite_delay = 10
        mob_list.append(Mob(window_width, window_height, mob_filenames_list[num_of_sprite], sprite_delay, num_of_cadr, num_of_right, num_of_left, num_of_up, num_of_down, health, base_value, delay_before_appearance, cost))
        delay_before_appearance += 100
    return mob_list

def mob_update(mob_list, road_list, current_gold, inscription_list):
    for mob in mob_list:
        mob.delay_before_appearance -= 1
        mob.center_x = mob.x + mob.width // 2
        mob.center_y = mob.y + mob.height // 2
        if mob.current_sprite_delay == mob.sprite_delay:
            mob.x_sprite -= mob.base_value
            mob.current_sprite_delay = 0
        if mob.x_sprite == -mob.base_value * mob.num_of_cadr:
            mob.x_sprite = 0
        mob.current_sprite_delay += 1
        for road in road_list:
            if road[0] == mob.x and road[1] == mob.y:
                if road[2] == 'right':
                    mob.y_sprite = -mob.base_value * mob.num_of_right
                    mob.x_speed = 1
                    mob.y_speed = 0
                if road[2] == 'left':
                    mob.y_sprite = -mob.base_value * mob.num_of_left
                    mob.x_speed = -1
                    mob.y_speed = 0
                if road[2] == 'up':
                    mob.y_sprite = -mob.base_value * mob.num_of_up
                    mob.x_speed = 0
                    mob.y_speed = -1
                if road[2] == 'down':
                    mob.y_sprite = -mob.base_value * mob.num_of_down
                    mob.x_speed = 0
                    mob.y_speed = 1

        if mob.current_health <= 0:
            inscription_list.append(
                Inscription(mob.x + mob.width // 2, mob.y, mob.window_width, mob.window_height, None, 24,
                            str(mob.cost), (255, 0, 0), 20,
                            1, 0, -1))
            mob_list.remove(mob)
            current_gold += mob.cost
        if mob.delay_before_appearance <= 0:
            mob.x += mob.x_speed
            mob.y += mob.y_speed
        mob.rect = pygame.Rect((mob.x, mob.y, mob.width, mob.height))

    return current_gold, inscription_list


def mob_draw(mob_list, surface):
    for mob in mob_list:
        if mob.delay_before_appearance <= 0:
            mob.surface_image.fill((1, 2, 3))
            mob.surface_image.blit(mob.image, (mob.x_sprite, mob.y_sprite))
            mob.surface_image.set_colorkey((1, 2, 3))
            pygame.draw.rect(surface, (255, 0, 0),
                             (mob.x, mob.y - mob.base_value // 5, mob.width, mob.base_value // 10))
            pygame.draw.rect(surface, (0, 255, 0),
                             (mob.x, mob.y - mob.base_value // 5, mob.current_health * mob.width // mob.health, mob.base_value // 10))
            surface.blit(mob.surface_image, (mob.x, mob.y))
