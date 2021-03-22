import arcade


def create_outer_walls(screen_width, screen_height):
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    # muro superiore
    for i in range(int(screen_width/16)):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 16*i+8
        y = screen_height-8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro inferiore
    for i in range(int(screen_width/16)):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 16*i+8
        y = 8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro sinistro
    for i in range(1, int(screen_height/16)-1):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 8
        y = 16*i+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro destro
    for i in range(1, int(screen_height/16)-1):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = screen_width-8
        y = 16*i+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list


def create_wall(screen_width, screen_height):

    # istanzio i muri
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    # i muri andranno estesi con tutti i muri da aggiungere
    walls.extend(create_outer_walls(screen_width, screen_height))
    walls.extend(create_lab())
    walls.extend(create_bath())
    walls.extend(create_kitchen())
    walls.extend(create_double_room())
    walls.extend(create_library())
    return walls

def create_texture():
    #istanzio le texture
    texture = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    
    #le texture andranno estese con le texture da aggiungere
    texture.extend(create_stair())
    texture.extend(create_lift())

    return texture

def create_lab():
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(20):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 16*sprite_size+8
        y = 800-16*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(24,28):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 16*sprite_size+8
        y = 800-16*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(16):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 16*i+24
        y = (20*sprite_size)+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list

def create_bath():
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(14):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 16*sprite_size+8
        y = 16*i+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    #Muri Orizontali
    for i in range(3):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 16*i+24
        y = 14*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(7,16):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 16*i+24
        y = 14*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list

def create_kitchen():
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(6):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 23*sprite_size+8
        y = 16*i+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    
    #Muro Orizontale
    for i in range(26):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 800-16*i-24
        y = 11*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    
    return wall_list

def create_double_room():
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(12):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 23*sprite_size+8
        y = 16*i+16*sprite_size+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(11):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 36*sprite_size+8
        y = 16*i+16*sprite_size+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    #Muri Orizontali
    for i in range(26):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 800-16*i-24
        y = 16*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(7):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 800-16*i-24
        y = 28*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(11,20):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 800-16*i-24
        y = 28*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(24,25):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 800-16*i-24
        y = 28*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    

    return wall_list

def create_library():
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(4):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 23*sprite_size+8
        y = 800-16*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(8,15):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 23*sprite_size+8
        y = 800-16*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    
    #Muro Orizontale
    for i in range(25):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 800-16*i-24
        y = 800-16*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    
    return wall_list

def create_stair():
    texture_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    sprite_size=16
    stair = arcade.Sprite(
        "resources/stairs.png")
    x = 800-56
    y = 800-18.5*sprite_size
    stair.angle=90
    stair.scale=0.9
    stair.center_x=x
    stair.center_y=y
    texture_list.append(stair)

    return texture_list

def create_lift():
    texture_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    sprite_size=16
    stair = arcade.Sprite(
        "resources/lift.png")
    x = 20*sprite_size
    y = 54
    stair.scale=0.97
    stair.center_x=x
    stair.center_y=y
    texture_list.append(stair)

    return texture_list
    