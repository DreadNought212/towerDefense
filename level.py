import pygame

preview_level = [
    ['                    ',
     'r+++++++++++++++d   ',
     '                +   ',
     '                +   ',
     '                +   ',
     '   d++++++++++++l   ',
     '   +                ',
     '   +                ',
     '   +                ',
     '   r++++++++++++d   ',
     '                +   ',
     '                +   ',
     '                +   ',],

    [
     ['ghost','pony', 'ghost', 'ghost','ghost', 'ghost', 'ghost','ghost', 'ghost', 'ghost','ghost', 'ghost', 'ghost'],
                    ]
]

level_01 = [
    ['                    ',
     'r++++d              ',
     '     +              ',
     '     +              ',
     '     +              ',
     '     +    r+++++++++',
     '   d+l    +         ',
     '   +      u+++++l   ',
     '   +            +   ',
     '   +      r+++++u   ',
     '   r++++++u         ',
     '                    ',
     ],

    [
     ['skeleton','skeleton','skeleton','skeleton','skeleton','skeleton','skeleton','skeleton','skeleton','skeleton','skeleton','skeleton','skeleton',],
     ['skeleton', 'pony', 'minecrafter', 'boss', 'ghost', 'trump'],
     ['skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton', 'skeleton'],
     ['boss'],
     ['trump', 'minecrafter', 'ghost', 'ghost', 'ghost', 'ghost', 'ghost', 'ghost', 'ghost', 'ghost', 'ghost', 'ghost', 'ghost', 'ghost', 'pony'],

                    ]
]

class Road(pygame.sprite.Sprite):
    def __init__(self, x, y, window_width, window_height, road_filename, base_value):
        pygame.sprite.Sprite.__init__(self)
        self.window_height = window_height
        self.window_width = window_width
        self.width = base_value
        self.height = base_value
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(road_filename, (self.width, self.height))
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))

def road_draw(road_list, surface):
    for road_rect in road_list:
        surface.blit(road_rect.image, (road_rect.x, road_rect.y))
