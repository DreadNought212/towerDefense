import pygame
from towers import Tower
from other import Inscription

class TowerPanel():
    def __init__(self, wondow_width, window_height, base_value, tower_filenames_list, current_gold):
        self.window_width = wondow_width
        self.window_height = window_height
        self.base_value = base_value
        self.tower_filenames_list = tower_filenames_list
        self.width = base_value * len(self.tower_filenames_list)
        self.height = base_value
        self.x = self.window_width - self.width
        self.y = self.window_height - self.height
        self.surface = pygame.Surface((self.width, self.height))
        self.num_of_towers = len(tower_filenames_list)
        self.tower_is_intall = False
        self.select_num_tower = 0
        self.tower_cost = 0
        self.tower_radius = 0
        self.current_gold = current_gold
        self.damage = 0
        self.current_cooldown = 0
        self.surface.fill((13, 13, 13))
        self.surface.set_colorkey((13, 13, 13))

    def draw_tower_panel(self, surface):
        for tower_icon in self.tower_filenames_list:

            self.surface.blit(tower_icon, (self.base_value * self.tower_filenames_list.index(tower_icon), 0))
        surface.blit(self.surface, (self.x, self.y))

    def install_tower(self, mouse_position, base_value):
        for num_tower in range(self.num_of_towers):
            if mouse_position[1] > self.y and mouse_position[1] < self.y + base_value:
                if mouse_position[0] > self.x + base_value * num_tower and mouse_position[0] < self.x + base_value + base_value * num_tower:
                    self.tower_is_intall = True
                    if num_tower == 0:
                        #cannon tower
                        self.select_num_tower = 0
                        self.tower_radius = self.base_value * 4
                        self.tower_cost = 100
                        self.damage = 10
                        self.current_cooldown = 100
                    elif num_tower == 1:
                        #muskeeter tower
                        self.select_num_tower = 1
                        self.tower_radius = self.base_value * 3
                        self.tower_cost = 120
                        self.damage = 2
                        self.current_cooldown = 25


    def select_tower_place(self, mouse_position, tower_list, inscription_list, all_objects_position):
        x_tower_soul = mouse_position[0]
        y_tower_soul = mouse_position[1]
        while x_tower_soul % self.base_value != 0:
            x_tower_soul -= 1
        while y_tower_soul % self.base_value != 0:
            y_tower_soul -= 1
        if y_tower_soul >= self.window_height - self.base_value:
                y_tower_soul = self.window_height - self.base_value * 2

        if self.current_gold >= self.tower_cost and (str(x_tower_soul) + str(y_tower_soul)) not in all_objects_position:
            tower_list.append(
                Tower(self.select_num_tower, self.window_width, self.window_height, self.tower_filenames_list[self.select_num_tower],
                      x_tower_soul, y_tower_soul, self.base_value, self.tower_radius, self.damage, self.current_cooldown
                      , self.tower_cost))
            self.current_gold -= self.tower_cost
            all_objects_position.append((str(x_tower_soul) + str(y_tower_soul)))
        elif (str(x_tower_soul) + str(y_tower_soul)) in all_objects_position:
            inscription_list.append(
                Inscription(self.base_value * 8, self.base_value, self.window_width, self.window_height, None, 36, 'Select another place', (255, 0, 0), 100,
                            1, 0, 0))
        elif self.current_gold < self.tower_cost:
            inscription_list.append(
                Inscription(self.base_value, self.base_value, self.window_width, self.window_height, None, 36, 'You have no gold', (255, 0, 0), 100,
                            1, 0, 0))

        return tower_list, inscription_list, all_objects_position



