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
    
    return walls


def create_collidable_up(screen_width_room, screen_height_room, screen_width, screen_height):
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    walls.extend(create_outer_walls(screen_width_room,
                                    screen_height_room, screen_width, screen_height_room))
    walls.extend(create_serra(screen_height_room))
    walls.extend(create_bedroom())
    walls.extend(create_double_room_up(screen_height_room))
    

    return walls


def create_collidable_down(screen_width_room, screen_height_room, screen_width, screen_height):
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    walls.extend(create_outer_walls(screen_width_room,
                                    screen_height_room, screen_width, screen_height_room))
    walls.extend(create_garage())
   
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
        sprite.center_x = SPRITE_SIZE*i+8
        sprite.center_y = screen_height-8
        wall_list.append(sprite)

    # muro inferiore
    for i in range(int(screen_width/SPRITE_SIZE)):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+8
        sprite.center_y = 8
        wall_list.append(sprite)

    # muro sinistro
    for i in range(1, int(screen_height_room/SPRITE_SIZE)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 8
        sprite.center_y = SPRITE_SIZE*i+8
        wall_list.append(sprite)

    # muro destro
    for i in range(1, int(screen_height_room/SPRITE_SIZE)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_width-8
        sprite.center_y = SPRITE_SIZE*i+8
        wall_list.append(sprite)

    # muro centrale
    for i in range(1, int(screen_height_room/SPRITE_SIZE)-1):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_width_room-8
        sprite.center_y = SPRITE_SIZE*i+8
        wall_list.append(sprite)

    # muro division interfaccia
    for i in range(int(screen_width_room/SPRITE_SIZE), int(screen_width/SPRITE_SIZE)):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+8
        sprite.center_y = screen_height/2-8
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
        sprite.center_x = 16*SPRITE_SIZE+8
        sprite.center_y = screen_height-SPRITE_SIZE*i-24
        wall_list.append(sprite)
    for i in range(24, 28):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 16*SPRITE_SIZE+8
        sprite.center_y = screen_height-SPRITE_SIZE*i-24
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+24
        sprite.center_y = (20*SPRITE_SIZE)+8
        wall_list.append(sprite)
    #TEXTURE
    texture = arcade.Sprite(
        "resources/ObjSprite/Ground/scrivania_lab.png")
    texture.center_x = 48
    texture.center_y = 720
    wall_list.append(texture)
    texture=arcade.Sprite("resources/light.png")
    texture.center_x=20
    texture.center_y=480
    texture.angle=90
    wall_list.append(texture)
    return wall_list


def create_bath():
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(14):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 16*SPRITE_SIZE+8
        sprite.center_y = SPRITE_SIZE*i+24
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(3):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+24
        sprite.center_y = 14*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(7, 16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+24
        sprite.center_y = 14*SPRITE_SIZE+8
        wall_list.append(sprite)
    
    #TEXTURE
    texture=arcade.Sprite("resources/ObjSprite/Ground/bagno.png",1.5)
    texture.center_x=40
    texture.center_y=112
    texture.angle=180
    wall_list.append(texture)
    texture=arcade.Sprite("resources/light.png")
    texture.center_x=250
    texture.center_y=128
    texture.angle=-90
    wall_list.append(texture)
    return wall_list


def create_kitchen(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(6):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 23*SPRITE_SIZE+8
        sprite.center_y = SPRITE_SIZE*i+24
        wall_list.append(sprite)

    # Muro Orizontale
    for i in range(26):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i-24
        sprite.center_y = 11*SPRITE_SIZE+8
        wall_list.append(sprite)
    #TEXTURE
    texture = arcade.Sprite("resources/ObjSprite/Ground/cucina1.png")
    texture.center_x = 768
    texture.center_y = 96
    texture.angle = 90
    wall_list.append(texture)
    texture = arcade.Sprite("resources/ObjSprite/Ground/cucina2.png")
    texture.center_x = 632
    texture.center_y = 32
    wall_list.append(texture)
    texture=arcade.Sprite("resources/light.png")
    texture.center_x=592
    texture.center_y=170
    texture.angle=0
    wall_list.append(texture)
    return wall_list


def create_double_room_ground(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(12):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 23*SPRITE_SIZE+8
        sprite.center_y = SPRITE_SIZE*i+16*SPRITE_SIZE+24
        wall_list.append(sprite)
    for i in range(11):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 36*SPRITE_SIZE+8
        sprite.center_y = SPRITE_SIZE*i+16*SPRITE_SIZE+24
        wall_list.append(sprite)
    # Muri Orizontali
    for i in range(26):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i-24
        sprite.center_y = 16*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(6):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i-24
        sprite.center_y = 28*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(10, 19):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i-24
        sprite.center_y = 28*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(23, 25):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i-24
        sprite.center_y = 28*SPRITE_SIZE+8
        wall_list.append(sprite)
    #TEXTURE
    texture=arcade.Sprite("resources/ObjSprite/Ground/armadietti.png")
    texture.center_x=768
    texture.center_y=360
    wall_list.append(texture)
    texture=arcade.Sprite("resources/ObjSprite/Ground/armadietti.png")
    texture.center_x=608
    texture.center_y=360
    texture.angle=180
    wall_list.append(texture)
    texture=arcade.Sprite("resources/ObjSprite/Ground/meccanica.png")
    texture.center_x=560
    texture.center_y=360
    wall_list.append(texture)
    texture=arcade.Sprite("resources/ObjSprite/Ground/meccanica.png")
    texture.center_x=400
    texture.center_y=360
    wall_list.append(texture)
    return wall_list


def create_library(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # Muri verticali
    for i in range(4):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 23*SPRITE_SIZE+8
        sprite.center_y = screen_height-SPRITE_SIZE*i-24
        wall_list.append(sprite)
    for i in range(8, 15):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 23*SPRITE_SIZE+8
        sprite.center_y = screen_height-SPRITE_SIZE*i-24
        wall_list.append(sprite)

    # Muro Orizontale
    for i in range(25):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i-24
        sprite.center_y = screen_height-16*SPRITE_SIZE+8
        wall_list.append(sprite)
        
    #TEXTURE
    texture = arcade.Sprite(
        "resources/ObjSprite/Ground/lib1.png")
    texture.center_x = 768
    texture.center_y = 672
    wall_list.append(texture)
    
    texture = arcade.Sprite(
        "resources/ObjSprite/Ground/lib2.png")
    texture.center_x = 576
    texture.center_y = 576
    wall_list.append(texture)
    texture=arcade.Sprite("resources/light.png")
    texture.center_x=560
    texture.center_y=778
    texture.angle=0
    wall_list.append(texture)
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
        sprite.center_x = SPRITE_SIZE*i+8
        sprite.center_y = screen_height-16*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(12, 32):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+8
        sprite.center_y = screen_height-16*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(37, 49):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+8
        sprite.center_y = screen_height-16*SPRITE_SIZE+8
        wall_list.append(sprite)
    #TEXTURE
    
    for i in range(1, 9):
        texture = arcade.Sprite(
            "resources/ObjSprite/Up/pianta3.png", 1.5)
        texture.center_x = 90*i
        texture.center_y = 720
        wall_list.append(texture)
    for i in range(1, 9):
        texture = arcade.Sprite(
            "resources/ObjSprite/Up/pianta2.png", 1.5)
        texture.center_x = 90*i
        texture.center_y = 632
        wall_list.append(texture)
    texture=arcade.Sprite("resources/light.png")
    texture.center_x=384
    texture.center_y=778
    texture.angle=0
    wall_list.append(texture)
    #commenta questo pezzo di codice se vuoi usare la funzione create_pipe()
    texture = arcade.Sprite(
        "resources/ObjSprite/Up/pipe.png")
    texture.center_x = 354
    texture.center_y = 680
    wall_list.append(texture)
    #fine commento
    return wall_list


def create_bedroom():
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # muri orizzontali
    for i in range(1, 3):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+8
        sprite.center_y = 20*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(7, 16):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = SPRITE_SIZE*i+8
        sprite.center_y = 20*SPRITE_SIZE+8
        wall_list.append(sprite)

    # muro verticale
    for i in range(1, 21):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = 16*SPRITE_SIZE+8
        sprite.center_y = SPRITE_SIZE*i+8
        wall_list.append(sprite)

    #TEXTURE
    texture = arcade.Sprite("resources/ObjSprite/Up/lettocasa.png")
    texture.center_x=128
    texture.center_y=56
    texture.angle=180
    wall_list.append(texture)
    texture = arcade.Sprite("resources/ObjSprite/Up/lib1.png")
    texture.center_x=240
    texture.center_y=160
    wall_list.append(texture)
    texture=arcade.Sprite("resources/light.png")
    texture.center_x=20
    texture.center_y=160
    texture.angle=90
    wall_list.append(texture)
    return wall_list


def create_double_room_up(screen_height):
    SPRITE_SIZE = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    # muro orizzontale
    for i in range(1, 10):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i+8
        sprite.center_y = 18*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(14, 20):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i+8
        sprite.center_y = 18*SPRITE_SIZE+8
        wall_list.append(sprite)
    for i in range(24, 27):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-SPRITE_SIZE*i+8
        sprite.center_y = 18*SPRITE_SIZE+8
        wall_list.append(sprite)
    # muri verticali
    for i in range(1, 18):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-15*SPRITE_SIZE+8
        sprite.center_y = SPRITE_SIZE*i+8
        wall_list.append(sprite)
    for i in range(1, 19):
        sprite = arcade.Sprite(
            WALL_RESOURCE)
        sprite.center_x = screen_height-27*SPRITE_SIZE+8
        sprite.center_y = SPRITE_SIZE*i+8
        wall_list.append(sprite)
    
    #SPRITE
    texture = arcade.Sprite("resources/ObjSprite/Up/bagno.png",1.5)
    texture.center_x=464
    texture.center_y=40
    texture.angle=-90
    wall_list.append(texture)

    return wall_list

#Down Scene

def create_garage():
    wall_list = arcade.SpriteList(is_static=True)
    texture = arcade.Sprite(
        "resources/ObjSprite/Down/generatore2.png", 2)
    texture.center_x = 64
    texture.center_y = 668
    wall_list.append(texture)

    texture = arcade.Sprite(
        "resources/ObjSprite/Down/caldaia.png", 1)
    texture.center_x = 736
    texture.center_y = 88
    wall_list.append(texture)

    texture = arcade.Sprite(
        "resources/ObjSprite/Down/car.png", 1)
    texture.center_x = 400
    texture.center_y = 400
    wall_list.append(texture)
    texture=arcade.Sprite("resources/light.png")
    texture.center_x=416
    texture.center_y=778
    texture.angle=0
    wall_list.append(texture)
    return wall_list

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


"""in caso ti serva una funzione a parte per non collidable

def create_pipe():
    texture_list = arcade.SpriteList(is_static=True)
    texture = arcade.Sprite(
        "resources/ObjSprite/Up/pipe.png")
    texture.center_x = 354
    texture.center_y = 680
    texture_list.append(texture)
    return texture_list
    
    commenta il pezzo evidenziato in create_serra()"""