import pygame

class Tower(pygame.sprite.Sprite):
    def __init__(self, num_of_tower, window_width, window_height, tower_filename, x, y, base_value, radius, damage, cooldown, cost):
        pygame.sprite.Sprite.__init__(self)
        self.num_of_tower = num_of_tower
        self.window_height = window_height
        self.window_width = window_width
        self.width = base_value
        self.height = base_value
        self.x = x
        self.y = y
        self.center_x = self.x + self.width // 2
        self.center_y = self.y + self.height // 2
        self.image = pygame.transform.scale(tower_filename, (self.width, self.height))
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))
        self.current_cooldown = 0
        self.cooldown = cooldown
        self.radius = radius
        self.damage = damage
        self.cost = cost

def tower_draw(tower_list, surface):
    for tower in tower_list:
        surface.blit(tower.image, (tower.x, tower.y))

def tower_update(tower_list):
    for tower in tower_list:
        tower.current_cooldown -= 1

class Shot(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height, shot_filename, x, y, target, base_value, damage):
        pygame.sprite.Sprite.__init__(self)
        self.window_height = window_height
        self.window_width = window_width
        self.width = base_value // 3
        self.height = base_value // 3
        self.x = x
        self.y = y
        self.center_x = self.x + self.width // 2
        self.center_y = self.y + self.height // 2
        self.image = pygame.transform.scale(shot_filename, (self.width, self.height))
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))
        self.target = target
        self.speed_x = 0
        self.speed_y = 0
        self.damage = damage

def shoting(towers, mobs, bullet_filenames, bullet_list, base_value):
    for tower in towers:
        for mob in mobs:
            if tower.center_x - mob.center_x <= tower.radius and tower.center_x - mob.center_x >= - tower.radius \
                    and tower.current_cooldown <= 0 and tower.center_y - mob.y < tower.radius \
                    and tower.y - mob.center_y > - tower.radius\
                    and mob.x > -base_value // 2:
                tower.current_cooldown = tower.cooldown
                bullet_list.append(Shot(0, 0, bullet_filenames[tower.num_of_tower], tower.center_x, tower.center_y, mob, base_value, tower.damage))
    return bullet_list

def shot_draw(bullet_list, surface):
    for bullet in bullet_list:
        surface.blit(bullet.image, (bullet.x, bullet.y))

def shot_update(bullet_list):

    for bullet in bullet_list:
        bullet.center_x = bullet.x + bullet.width // 2
        bullet.center_y = bullet.y + bullet.height // 2
        bullet.speed_x = - (bullet.center_x - bullet.target.center_x) // 15
        bullet.speed_y = - (bullet.center_y - bullet.target.center_y) // 15
        bullet.x += bullet.speed_x
        bullet.y += bullet.speed_y
        bullet.rect = pygame.Rect((bullet.x, bullet.y, bullet.width, bullet.height))
        if pygame.sprite.collide_rect(bullet, bullet.target):
            bullet_list.remove(bullet)
            bullet.target.current_health -= bullet.damage
