import arcade

WALL_RESOURCE = "resources/muro.png"


def create_collidable(screen_width_room, screen_height_room, screen_width, screen_height, floor):
    if floor == 1:
        return create_collidable_ground(screen_width_room, screen_height_room, screen_width, screen_height)
    elif floor == 2:
        return create_collidable_up(screen_width_room, screen_height_room, screen_width, screen_height)
    else:
        return create_collidable_down(screen_width_room, screen_height_room, screen_width, screen_height)


def create_collidable_ground(screen_width_room, screen_height_room, screen_width, screen_height):
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    walls.extend(create_outer_walls(screen_width_room,
                                    screen_height_room, screen_width, screen_height))
    walls.extend(create_lab(screen_height_room))
    walls.extend(create_bath())
    walls.extend(create_kitchen(screen_height_room))
    walls.extend(create_double_room_ground(screen_height))
    walls.extend(create_library(screen_height_room))
    walls.extend(create_desk_texture())
    walls.extend(create_lib_texture())
    walls.extend(create_desk_texture())
    return walls


def create_collidable_up(screen_width_room, screen_height_room, screen_width, screen_height):
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    walls.extend(create_outer_walls(screen_width_room,
                                    screen_height_room, screen_width, screen_height_room))
    walls.extend(create_serra(screen_height_room))
    walls.extend(create_bedroom())
    walls.extend(create_double_room_up(screen_height_room))
    walls.extend(create_plants())

    return walls


def create_collidable_down(screen_width_room, screen_height_room, screen_width, screen_height):
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    walls.extend(create_outer_walls(screen_width_room,
                                    screen_height_room, screen_width, screen_height_room))
    walls.extend(create_boiler())
    walls.extend(create_generator())
    return walls


def create_not_collidable():
    texture = arcade.SpriteList(is_static=True)

    texture.extend(create_stair())
    texture.extend(create_lift())

    return texture

# Posizionamento dei muri


def create_outer_walls(screen_width_room, screen_height_room, screen_width, screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    # muro superiore
    for i in range(int(screen_width/SPRITE_SIZE)):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = screen_height-8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro inferiore
    for i in range(int(screen_width/SPRITE_SIZE)):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = 8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro sinistro
    for i in range(1, int(screen_height_room/SPRITE_SIZE)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = 8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro destro
    for i in range(1, int(screen_height_room/SPRITE_SIZE)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = screen_width-8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro centrale
    for i in range(1, int(screen_height_room/SPRITE_SIZE)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = screen_width_room-8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro division interfaccia
    # muro superiore
    for i in range(int(screen_width_room/SPRITE_SIZE), int(screen_width/SPRITE_SIZE)):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = screen_height/2-8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list

# Ground Scene


def create_lab(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(20):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 16*SPRITE_SIZE+8
        y = screen_height-SPRITE_SIZE*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(24, 28):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 16*SPRITE_SIZE+8
        y = screen_height-SPRITE_SIZE*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = SPRITE_SIZE*i+24
        y = (20*SPRITE_SIZE)+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list


def create_bath():
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(14):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 16*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(3):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = SPRITE_SIZE*i+24
        y = 14*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(7, 16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = SPRITE_SIZE*i+24
        y = 14*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list


def create_kitchen(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(6):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # Muro Orizontale
    for i in range(26):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-SPRITE_SIZE*i-24
        y = 11*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list


def create_double_room_ground(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(12):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+16*SPRITE_SIZE+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(11):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 36*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+16*SPRITE_SIZE+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(26):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-SPRITE_SIZE*i-24
        y = 16*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(7):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-SPRITE_SIZE*i-24
        y = 28*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(11, 20):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-SPRITE_SIZE*i-24
        y = 28*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(24, 25):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-SPRITE_SIZE*i-24
        y = 28*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list


def create_library(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(4):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*SPRITE_SIZE+8
        y = screen_height-SPRITE_SIZE*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(8, 15):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*SPRITE_SIZE+8
        y = screen_height-SPRITE_SIZE*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # Muro Orizontale
    for i in range(25):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-SPRITE_SIZE*i-24
        y = screen_height-16*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list

# Up Scene


def create_serra(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # muri orizzontali
    for i in range(1, 7):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = screen_height-16*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(12, 32):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = screen_height-16*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(37, 49):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = screen_height-16*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list


def create_bedroom():
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # muri orizzontali
    for i in range(1, 3):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = 20*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(7, 16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = 20*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro verticale
    for i in range(1, 21):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = 16*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list


def create_double_room_up(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # muro orizzontale
    for i in range(1, 10):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = screen_height-SPRITE_SIZE*i+8
        y = 18*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(14, 20):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = screen_height-SPRITE_SIZE*i+8
        y = 18*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(24, 27):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = screen_height-SPRITE_SIZE*i+8
        y = 18*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    # muri verticali
    for i in range(1, 18):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = screen_height-15*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(1, 19):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = screen_height-27*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list


# Posizionamento delle texture

# Texture collidable Ground
def create_lib_texture():
    texture_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Verticale
    texture = arcade.Sprite(
        "resources/ObjSprite/lib1.png")
    texture.center_x = 768
    texture.center_y = 672
    texture_list.append(texture)
    # Orizontale
    texture = arcade.Sprite(
        "resources/ObjSprite/lib2.png")
    texture.center_x = 576
    texture.center_y = 576
    texture_list.append(texture)
    return texture_list


def create_desk_texture():
    texture_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    texture = arcade.Sprite(
        "resources/ObjSprite/scrivania_lab.png")
    texture.center_x = 48
    texture.center_y = 720
    texture_list.append(texture)
    return texture_list


def create_plants():
    texture_list = arcade.SpriteList(is_static=True)
    for i in range(0, 10):
        texture = arcade.Sprite(
            "resources/ObjSprite/pianta1.png", 1)
        x = 80*i+40
        texture.center_x = x
        texture.center_y = 752
        texture_list.append(texture)
    for i in range(0, 10):
        texture = arcade.Sprite(
            "resources/ObjSprite/pianta3.png", 1)
        x = 80*i+40
        texture.center_x = x
        texture.center_y = 688
        texture_list.append(texture)
    for i in range(0, 10):
        texture = arcade.Sprite(
            "resources/ObjSprite/pianta2.png", 1)
        x = 80*i+40
        texture.center_x = x
        texture.center_y = 624
        texture_list.append(texture)
    return texture_list


def create_boiler():
    texture_list = arcade.SpriteList(is_static=True)
    texture = arcade.Sprite(
        "resources/ObjSprite/caldaia.png", 1)
    texture.center_x = 736
    texture.center_y = 88
    texture_list.append(texture)
    return texture_list


def create_generator():
    texture_list = arcade.SpriteList(is_static=True)
    texture = arcade.Sprite(
        "resources/ObjSprite/generatore2.png", 2)
    texture.center_x = 64
    texture.center_y = 668
    texture_list.append(texture)
    return texture_list
# Not Collidible Obj


def create_stair():
    texture_list = arcade.SpriteList(is_static=True)
    texture = arcade.Sprite(
        "resources/stairs.png", 0.9)
    texture.angle = 90
    texture.center_x = 744
    texture.center_y = 504
    texture_list.append(texture)
    return texture_list


def create_lift():
    texture_list = arcade.SpriteList(is_static=True)
    texture = arcade.Sprite(
        "resources/lift.png", 0.97)
    texture.center_x = 320
    texture.center_y = 54
    texture_list.append(texture)
    return texture_list
