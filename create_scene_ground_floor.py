import arcade

WALL_RESOURCE = "resources/muro.png"


def create_collidable(screen_width, screen_height):
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    walls.extend(create_outer_walls(screen_width, screen_height))
    walls.extend(create_lab(screen_height))
    walls.extend(create_bath())
    walls.extend(create_kitchen(screen_height))
    walls.extend(create_double_room(screen_height))
    walls.extend(create_library())
    walls.extend(create_desk_texture())
    walls.extend(create_lib_texture())
    walls.extend(create_desk_texture())
    return walls


def create_not_collidable():
    texture = arcade.SpriteList(is_static=True)

    texture.extend(create_stair())
    texture.extend(create_lift())

    return texture

# Posizionamento dei muri


def create_outer_walls(screen_width, screen_height):
    print("ground floor")
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
    for i in range(1, int(screen_height/SPRITE_SIZE)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 8
        y = SPRITE_SIZE*i+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro destro
    for i in range(1, int(screen_height/SPRITE_SIZE)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_width-8
        y = SPRITE_SIZE*i+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list


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


def create_double_room(screen_height):
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


def create_library():
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(4):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*SPRITE_SIZE+8
        y = 800-16*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(8, 15):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*SPRITE_SIZE+8
        y = 800-16*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # Muro Orizontale
    for i in range(25):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 800-16*i-24
        y = 800-16*SPRITE_SIZE+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list

# Posizionamento delle texture


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
