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


def create_all(screen_width, screen_height):

    # istanzio i muri
    walls = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)

    # i muri andranno estesi con tutti i muri da aggiungere
    walls.extend(create_outer_walls(screen_width, screen_height))
    walls.extend(create_lab())
    return walls


def create_lab():
    sprite_size = 16
    wall_list = arcade.SpriteList(
        use_spatial_hash=True, spatial_hash_cell_size=128)
    for i in range(17):
        sprite = arcade.Sprite(
            "resources/muromario2.png")

        x = 17*sprite_size
        y = 800-16*i+8

        sprite.center_x = x
        sprite.center_y = y
        wall_list.append(sprite)
    return wall_list
