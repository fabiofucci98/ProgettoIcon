import arcade
import os

import create_scene

SPRITE_IMAGE_SIZE = 128
SPRITE_SCALING = 0.25
SPRITE_SIZE = SPRITE_IMAGE_SIZE * SPRITE_SCALING

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SCREEN_TITLE = ""

MOVEMENT_SPEED = 5

VIEWPORT_MARGIN = 100


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.wall_list = None
        self.texture_list = None
        self.enemy_list = None

        # Set up the player info
        self.player = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.physics_engine = None
        self.physics_engine2 = None

        # --- Related to paths
        # List of points that makes up a path between two points
        self.path = None
        # List of points we checked to see if there is a barrier there
        self.barrier_list = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        self.wall_list = create_scene.create_wall(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.texture_list = create_scene.create_texture()
        """
            self.enemy_list = arcade.SpriteList()
            """
        # Set up the player
        self.player = arcade.Sprite(
            "resources/robottino.png", 1)
        self.player.center_x = SPRITE_SIZE * 5
        self.player.center_y = SPRITE_SIZE * 1
        self.player_list.append(self.player)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.wall_list)
        self.physics_engine2 = arcade.PhysicsEngineSimple(self.player,
                                                         self.texture_list)
        """
        # --- Path related
        # This variable holds the travel-path. We keep it as an attribute so
        # we can calculate it in on_update, and draw it in on_draw.
        self.path = None
        # Grid size for calculations. The smaller the grid, the longer the time
        # for calculations. Make sure the grid aligns with the sprite wall grid,
        # or some openings might be missed.
        grid_size = SPRITE_SIZE

        # Calculate the playing field size. We can't generate paths outside of
        # this.
        playing_field_left_boundary = -SPRITE_SIZE * 2
        playing_field_right_boundary = SPRITE_SIZE * 35
        playing_field_top_boundary = SPRITE_SIZE * 17
        playing_field_bottom_boundary = -SPRITE_SIZE * 2

        # This calculates a list of barriers. By calculating it here in the
        # init, we are assuming this list does not change. In this example,
        # our walls don't move, so that is ok. If we want moving barriers (such as
        # moving platforms or enemies) we need to recalculate. This can be an
        # time-intensive process depending on the playing field size and grid
        # resolution.

        # Note: If the enemy sprites are the same size, we only need to calculate
        # one of these. We do NOT need a different one for each enemy. The sprite
        # is just used for a size calculation.
        
            self.barrier_list = arcade.AStarBarrierList(enemy,
                                                        self.wall_list,
                                                        grid_size,
                                                        playing_field_left_boundary,
                                                        playing_field_right_boundary,
                                                        playing_field_bottom_boundary,
                                                        playing_field_top_boundary)
            """

    def on_update(self, delta_time):
        """ Movement and game logic """

        try:
            # Calculate speed based on the keys pressed
            self.player.change_x = 0
            self.player.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player.change_y = MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player.change_y = -MOVEMENT_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player.change_x = -MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player.change_x = MOVEMENT_SPEED

            # Update the character
            self.physics_engine.update()
            self.physics_engine2.update()

            """
                # Calculate a path to the player
                enemy = self.enemy_list[0]
                # Set to True if we can move diagonally. Note that diagnonal movement
                # might cause the enemy to clip corners.
                self.path = arcade.astar_calculate_path(enemy.position,
                                                        self.player.position,
                                                        self.barrier_list,
                                                        diagonal_movement=False)
                # print(self.path,"->", self.player.position)
            """

        except Exception:
            import traceback
            traceback.print_exc()

    def on_draw(self):
        try:
            # This command has to happen before we start drawing
            arcade.start_render()

            # Draw all the sprites.
            
            self.wall_list.draw()
            self.texture_list.draw()
            self.player_list.draw()

            # self.enemy_list.draw()

            if self.path:
                arcade.draw_line_strip(self.path, arcade.color.BLUE, 2)

        except Exception:

            import traceback
            traceback.print_exc()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
