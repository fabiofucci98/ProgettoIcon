import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Casa dello scienziato pazzo"


class Game(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the background texture
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        # Get ready to draw
        arcade.start_render()
        # Draw external wall
        arcade.draw_rectangle_outline(
            400, 400, 800, 800, arcade.color.BLACK, 15, 0)

        # Draw line with tuple (start x,start y),(finish x, finish y),
        # Draw Orizontal Wall
        point_list = ((15, 250), (40, 250),  # Bagno con porta in
                      (100, 250), (250, 250),  # Bagno con porta fin
                      (15, 300), (250, 300),  # Laboratorio
                      (350, 180), (800-15, 180),  # Cucina
                      (350, 230), (800-15, 230),  # Componenti sud
                      (350, 430), (370, 430),  # Componenti Ell porta in
                      (430, 430), (600, 430),  # Compnenti muro interm
                      (660, 430), (800-15, 430),  # Componenti Mecc Fin
                      (350, 520), (800-15, 520)  # Libreria sud
                      )
        arcade.draw_lines(point_list, arcade.color.BLACK, 5)
        # Draw Vertical Wall
        point_list = ((250, 15), (250, 252.5),  # Bagno
                      (250, 300-2.5), (250, 350),  # Laboratorio porta in
                      (250, 410), (250, 800-15),  # Laboratorio porta fin
                      (350, 15), (350, 100),  # Cucina porta in
                      (350, 160), (350, 182.5),  # Cucina porta fin
                      (350, 227.5), (350, 432.5),  # Componenti muro west
                      (575, 227.5), (575, 432.5),  # Componenti muro Divisorio
                      (350, 517.5), (350, 640),  # Libreria porta in
                      (350, 700), (350, 800-15)  # Libreria porta fin
                      )
        arcade.draw_lines(point_list, arcade.color.BLACK, 5)

        # Texture
        texture = arcade.load_texture(
            ":resources:images/space_shooter/playerShip1_orange.png")
        scale = .5
        arcade.draw_scaled_texture_rectangle(150, 150, texture, scale, 0)

        stairs = arcade.load_texture(
            "Bitmap/stairs.png")
        arcade.draw_scaled_texture_rectangle(742.5, 475, stairs, .95, 90)
        lift = arcade.load_texture(
            "Bitmap/lift.png")
        arcade.draw_scaled_texture_rectangle(300, 55, lift, 0.95, 0)

        # Finish drawing
        arcade.finish_render()


def main():
    """ Main method """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    print(arcade.get_pixel(50, 50))
    arcade.run()


if __name__ == "__main__":
    main()
