import pygame
from mobs import *
from towers import *
from level import *
from control import *
from other import *

pygame.init()

#основная величина для масштабирования всех объектов
base_value = 50
#ширина окна
WIDTH = 20 * base_value
#высота окна
HEIGHT = 13 * base_value
#создание окна
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

font_1 = pygame.font.Font(None, 36)

footer_filename = pygame.image.load('hud.jpg').convert_alpha()

mob_filename_01 = pygame.image.load('mob01.png').convert_alpha()
mob_filename_02 = pygame.image.load('pony01.png').convert_alpha()
mob_filename_03 = pygame.image.load('ghost01.png').convert_alpha()
mob_filename_04 = pygame.image.load('minecrafter01.png').convert_alpha()
mob_filename_05 = pygame.image.load('trump01.png').convert_alpha()
mob_filename_06 = pygame.image.load('skeleton01.png').convert_alpha()
mob_filename_07 = pygame.image.load('boss01.png').convert_alpha()
mob_filenames_list = [
    mob_filename_01,
    mob_filename_02,
    mob_filename_03,
    mob_filename_04,
    mob_filename_05,
    mob_filename_06,
    mob_filename_07
]

tower_filename_01 = pygame.transform.scale(pygame.image.load('cannon_tower01.png'), (base_value, base_value)).convert_alpha()
tower_filename_02 = pygame.transform.scale(pygame.image.load('musketeer_tower01.png'), (base_value, base_value)).convert_alpha()
tower_filenames_list = [
    tower_filename_01,
    tower_filename_02
]

bullet_filename_01 = pygame.transform.scale(pygame.image.load('ball01.png'), (base_value, base_value)).convert_alpha()
bullet_filename_02 = pygame.transform.scale(pygame.image.load('ball02.png'), (base_value, base_value)).convert_alpha()
bullet_filenames_list = [
    bullet_filename_01,
    bullet_filename_02
]

bg_filename = pygame.transform.scale(pygame.image.load('bg01.jpg'), (WIDTH, HEIGHT)).convert()
road_filename = pygame.image.load('road01.jpg').convert()
clock = pygame.time.Clock()

# preview
def preview(level):
    #title
    title = Title(WIDTH, HEIGHT, base_value)
    # world creating
    world = level[0]
    current_gold = 550
    y_road = 0
    x_road = 0
    route_for_mobs = []
    road_list = []
    tower_panel = TowerPanel(WIDTH, HEIGHT, base_value, tower_filenames_list, current_gold)

    tower_list = [
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 5, base_value * 3, base_value, 250, 5, 100
              , 0),
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 10, base_value * 2, base_value, 250, 5, 100
              , 0),
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 7, base_value * 10, base_value, 250, 5, 100
              , 0),
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 7, base_value * 4, base_value, 250, 5, 100
              , 0),
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 3, base_value * 4, base_value, 250, 5, 100
              , 0),
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 11, base_value * 6, base_value, 250, 5, 100
              , 0),
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 7, base_value * 6, base_value, 250, 5, 100
              , 0),
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 10, base_value * 10, base_value, 250, 5, 100
              , 0),
        Tower(0, WIDTH, HEIGHT,
              tower_filenames_list[0],
              base_value * 3, base_value * 10, base_value, 250, 5, 100
              , 0),
    ]

    for row in world:
        for col in row:
            if col != ' ':
                road_rect = Road(x_road, y_road, WIDTH, HEIGHT, road_filename, base_value)
                road_list.append(road_rect)
            if col == 'r':
                route_for_mobs.append([x_road, y_road, 'right'])
            if col == 'l':
                route_for_mobs.append([x_road, y_road, 'left'])
            if col == 'u':
                route_for_mobs.append([x_road, y_road, 'up'])
            if col == 'd':
                route_for_mobs.append([x_road, y_road, 'down'])
            x_road += base_value
        x_road = 0
        y_road += base_value

    inscription_list = []
    bullet_list = []
    wave_num = 0

    run = True

    is_mob_creating = True

    while run:
        current_gold = tower_panel.current_gold

        if is_mob_creating:
            level_mobs_list = mobs_creating(level[1][wave_num], WIDTH, HEIGHT, mob_filenames_list, base_value)
            is_mob_creating = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainloop(level_01)

        # update objects
        tower_panel.current_gold, inscription_list = mob_update(level_mobs_list, route_for_mobs, tower_panel.current_gold, inscription_list)
        tower_update(tower_list)
        shot_update(bullet_list)

        # adding shots to the list
        bullet_list = shoting(tower_list, level_mobs_list, bullet_filenames_list, bullet_list, base_value)

        # draw objects
        # bg
        WINDOW.blit(bg_filename, (0, 0))
        # roads
        road_draw(road_list, WINDOW)
        # towers
        tower_draw(tower_list, WINDOW)
        # bullets
        shot_draw(bullet_list, WINDOW)
        # mobs
        mob_draw(level_mobs_list, WINDOW)
        #title
        title.draw_title(WINDOW)

        pygame.display.update()

        pygame.time.delay(10)

#mainloop
def mainloop(level):
    #карта
    world = level[0]
    #началное количество золота
    current_gold = 550
    #начальные координаты дороги
    y_road = 0
    x_road = 0
    #маршрут для врагов
    route_for_mobs = []
    #список с элементами дороги
    road_list = []
    #список с надписями
    inscription_list = []
    #создание панели для выбора башен
    tower_panel = TowerPanel(WIDTH, HEIGHT, base_value, tower_filenames_list, current_gold)
    #список со всеми объектами
    all_objects_position = []
    #список врагов в данный момент
    level_mobs_list = []
    #создание карты
    for row in world:
        for col in row:
            if col != ' ':
                road_rect = Road(x_road, y_road, WIDTH, HEIGHT, road_filename, base_value)
                road_list.append(road_rect)
                all_objects_position.append(str(x_road) + str(y_road))
            if col == 'r':
                route_for_mobs.append([x_road, y_road, 'right'])
            if col == 'l':
                route_for_mobs.append([x_road, y_road, 'left'])
            if col == 'u':
                route_for_mobs.append([x_road, y_road, 'up'])
            if col == 'd':
                route_for_mobs.append([x_road, y_road, 'down'])
            x_road += base_value
        x_road = 0
        y_road += base_value

    tower_list = []
    bullet_list = []
    wave_num = -1

    run = True
    #разрешает создание врагов
    is_mob_creating = False

    while run:
        #текущее золото и его отображение для игрока
        current_gold = tower_panel.current_gold
        current_gold_text = font_1.render(str(current_gold), 1, (180, 0, 0))
        #between waves control
        if len(level_mobs_list) == 0:
            is_mob_creating = False
            inscription_list.append(Inscription(base_value * 8, base_value, WIDTH, HEIGHT, None, 36, 'Press SPACE to start', (255, 255, 255), 1, 1, 0, 0))
        #циклс обработки событий
        for event in pygame.event.get():
            #выход из программы
            if event.type == pygame.QUIT:
                exit()
            #старт волны при нажатии SPACE
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and is_mob_creating == False:
                    wave_num += 1
                    level_mobs_list = mobs_creating(level[1][wave_num], WIDTH, HEIGHT, mob_filenames_list, base_value)
                    is_mob_creating = True
            #установка башни
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tower_panel.tower_is_intall:
                        tower_list, inscription_list, all_objects_position = tower_panel.select_tower_place(pygame.mouse.get_pos(), tower_list, inscription_list, all_objects_position)
                        tower_panel.tower_is_intall = False
                    tower_panel.install_tower(pygame.mouse.get_pos(), base_value)

        #обновление
        tower_panel.current_gold, inscription_list = mob_update(level_mobs_list, route_for_mobs, tower_panel.current_gold, inscription_list)
        #обновление башен
        tower_update(tower_list)
        #обновление снарядов
        shot_update(bullet_list)
        #обновление надписей
        inscription_update(inscription_list)

        #создание снаряда и добавление его в список
        bullet_list = shoting(tower_list, level_mobs_list, bullet_filenames_list, bullet_list, base_value)

        #отрисовка
        #отрисовка фона
        WINDOW.blit(bg_filename, (0, 0))
        #отрисовка дороги
        road_draw(road_list, WINDOW)
        #отрисовка башен
        tower_draw(tower_list, WINDOW)
        #отрсовка снарядов
        shot_draw(bullet_list, WINDOW)
        #отрисовка врагов
        mob_draw(level_mobs_list, WINDOW)

        #отрисовка выбранной башни
        if tower_panel.tower_is_intall:
            x_tower_soul = pygame.mouse.get_pos()[0]
            y_tower_soul = pygame.mouse.get_pos()[1]
            while x_tower_soul % base_value != 0:
                x_tower_soul -= 1
            while y_tower_soul % base_value != 0:
                y_tower_soul -= 1
            if y_tower_soul >= HEIGHT - base_value:
                y_tower_soul = HEIGHT - base_value * 2

            WINDOW.blit(tower_filenames_list[tower_panel.select_num_tower],
                        (x_tower_soul, y_tower_soul))
            #радиус стрельбы башни
            pygame.draw.circle(WINDOW, (255, 0, 0), (x_tower_soul + base_value // 2, y_tower_soul + base_value // 2), tower_panel.tower_radius, 2)

        #HUD
        Footer(WIDTH, HEIGHT, base_value, footer_filename).draw_footer(WINDOW)
        #панель выбора башен
        tower_panel.draw_tower_panel(WINDOW)
        #создание надписей
        inscription_list = draw_inscription(inscription_list, WINDOW)
        #отображение золота
        WINDOW.blit(current_gold_text, (WIDTH - base_value, 0))
        #обновление всех объектов при каждой итерации цикла
        pygame.display.update()
        #частота итераций основного цикла
        pygame.time.delay(10)

#вызов функции со вступлением
preview(preview_level)
