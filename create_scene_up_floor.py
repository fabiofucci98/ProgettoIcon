import arcade

WALL_RESOURCE = "resources/muro.png"


def create_collidable(screen_width, screen_height):
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    walls.extend(create_outer_walls(screen_width, screen_height))
    walls.extend(create_serra())
    walls.extend(create_bedroom())
    walls.extend(create_double_room())

    return walls

def create_not_collidable():
    texture = arcade.SpriteList(is_static=True)

    texture.extend(create_stair())
    texture.extend(create_lift())

    return texture

def create_outer_walls(screen_width, screen_height):
    print("up floor")
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

def create_serra():
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    #muri orizzontali
    for i in range(1,7):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = 800-16*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(12,32):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = 800-16*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(37,49):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = 800-16*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    
    return wall_list

def create_bedroom():
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    #muri orizzontali
    for i in range (1,3):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = 20*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range (7,16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = SPRITE_SIZE*i+8
        y = 20*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    
    #muro verticale
    for i in range (1,21):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = 16*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list

def create_double_room():
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    #muro orizzontale
    for i in range(1,10):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = 800-SPRITE_SIZE*i+8
        y = 18*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(14,20):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = 800-SPRITE_SIZE*i+8
        y = 18*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(24,27):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = 800-SPRITE_SIZE*i+8
        y = 18*SPRITE_SIZE+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    #muri verticali
    for i in range(1,18):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = 800-15*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    for i in range(1,19):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        x = 800-27*SPRITE_SIZE+8
        y = SPRITE_SIZE*i+8
        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list
    


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