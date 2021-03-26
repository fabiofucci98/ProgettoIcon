import arcade

WALL_RESOURCE = "resources/muro.png"


def create_collidable(screen_width, screen_height):

    # istanzio i muri
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # i muri andranno estesi con tutti i muri da aggiungere
    walls.extend(create_outer_walls(screen_width, screen_height))
    walls.extend(create_lab(screen_height))
    walls.extend(create_bath())
    walls.extend(create_kitchen(screen_height))
    walls.extend(create_double_room(screen_height))
    walls.extend(create_library())
    #walls.extend(create_desk_texture())
    return walls
    


def create_not_collidable():
    # istanzio le texture
    texture = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    # le texture andranno estese con le texture da aggiungere
    texture.extend(create_stair())
    texture.extend(create_lift())
    texture.extend(create_lib_texture())
    texture.extend(create_desk_texture())

    return texture

#Posizionamento dei muri
def create_outer_walls(screen_width, screen_height):
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    # muro superiore
    for i in range(int(screen_width/sprite_size)):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = sprite_size*i+8
        y = screen_height-8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro inferiore
    for i in range(int(screen_width/sprite_size)):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = sprite_size*i+8
        y = 8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro sinistro
    for i in range(1, int(screen_height/sprite_size)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 8
        y = sprite_size*i+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # muro destro
    for i in range(1, int(screen_height/sprite_size)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_width-8
        y = sprite_size*i+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list

def create_lab(screen_height):
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(20):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 16*sprite_size+8
        y = screen_height-sprite_size*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(24, 28):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 16*sprite_size+8
        y = screen_height-sprite_size*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = sprite_size*i+24
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
            WALL_RESOURCE)

        x = 16*sprite_size+8
        y = sprite_size*i+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(3):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = sprite_size*i+24
        y = 14*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(7, 16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = sprite_size*i+24
        y = 14*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list

def create_kitchen(screen_height):
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(6):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*sprite_size+8
        y = sprite_size*i+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # Muro Orizontale
    for i in range(26):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-sprite_size*i-24
        y = 11*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list

def create_double_room(screen_height):
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(12):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*sprite_size+8
        y = sprite_size*i+16*sprite_size+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(11):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 36*sprite_size+8
        y = sprite_size*i+16*sprite_size+24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(26):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-sprite_size*i-24
        y = 16*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(7):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-sprite_size*i-24
        y = 28*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(11, 20):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-sprite_size*i-24
        y = 28*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(24, 25):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = screen_height-sprite_size*i-24
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
            WALL_RESOURCE)

        x = 23*sprite_size+8
        y = 800-16*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(8, 15):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 23*sprite_size+8
        y = 800-16*i-24

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    # Muro Orizontale
    for i in range(25):
        sprite = arcade.Sprite(
            WALL_RESOURCE)

        x = 800-16*i-24
        y = 800-16*sprite_size+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)

    return wall_list

#Posizionamento delle texture
def create_stair():
    texture_list = arcade.SpriteList(is_static=True)
    sprite_size = 16
    texture = arcade.Sprite(
        "resources/stairs.png", 0.9)
    x = 800-56
    y = 800-18.5*sprite_size
    texture.angle = 90
    texture.center_x = x
    texture.center_y = y
    texture_list.append(texture)

    return texture_list

def create_lift():
    texture_list = arcade.SpriteList(is_static=True)
    sprite_size = 16
    texture = arcade.Sprite(
        "resources/lift.png", 0.97)
    x = 20*sprite_size
    y = 54
    texture.center_x = x
    texture.center_y = y
    texture_list.append(texture)

    return texture_list

def create_lib_texture():
    texture_list = arcade.SpriteList(is_static=True)
    sprite_size = 16
    #Verticale
    texture = arcade.Sprite(
        "resources/ObjSprite/lib1.png")
    x = 800-32
    y = 800-8*sprite_size
        
    texture.center_x = x
    texture.center_y = y
    texture_list.append(texture)
    #Orizontale
    texture = arcade.Sprite(
        "resources/ObjSprite/lib2.png")
    x = 800-12*sprite_size-32
    y = 800-14*sprite_size
        
    texture.center_x = x
    texture.center_y = y
    texture_list.append(texture)
    
    return texture_list

def create_desk_texture():
    texture_list = arcade.SpriteList(is_static=True)
    sprite_size = 16
    texture = arcade.Sprite(
        "resources/ObjSprite/scrivania_lab.png")
    x = 3*sprite_size
    y = 800-5*sprite_size
    texture.center_x = x
    texture.center_y = y
    texture_list.append(texture)
    return texture_list