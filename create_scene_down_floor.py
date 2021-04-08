import arcade

WALL_RESOURCE = "resources/muro.png"


def create_collidable(screen_width, screen_height):
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    walls.extend(create_outer_walls(screen_width, screen_height))
    walls.extend(create_boiler())
    walls.extend(create_generator())
    return walls


def create_not_collidable():
    texture = arcade.SpriteList(is_static=True)

    texture.extend(create_stair())
    texture.extend(create_lift())
    

    return texture

# Posizionamento dei muri


def create_outer_walls(screen_width, screen_height):
    print("down floor")
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

def create_boiler():
    texture_list = arcade.SpriteList(is_static=True)
    texture = arcade.Sprite(
        "resources/ObjSprite/caldaia.png",1)
    texture.center_x = 736
    texture.center_y = 88
    texture_list.append(texture)
    return texture_list

def create_generator():
    texture_list = arcade.SpriteList(is_static=True)
    texture = arcade.Sprite(
        "resources/ObjSprite/generatore2.png",2)
    texture.center_x = 64
    texture.center_y = 668
    texture_list.append(texture)
    return texture_list