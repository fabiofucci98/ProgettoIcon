from PIL.Image import NONE
import arcade
import os
import create_scene
from graph import Graph, Node
from path_finding import A_star, euclidean_distance
import math


SPRITE_SIZE = 32
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SCREEN_TITLE = "Culo"

MOVEMENT_SPEED = 5

VIEWPORT_MARGIN = 100


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.wall_list = None
        self.texture_list = None
        self.player = None
        self.physics_engine = None

        self.path = None
        # List of points we checked to see if there is a barrier there
        self.barrier_list = None
        self.graph = None

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = create_scene.create_collidable(
            SCREEN_WIDTH, SCREEN_HEIGHT)
        self.texture_list = create_scene.create_not_collidable()
        # Set up the player
        self.player = arcade.Sprite(
            "resources/robottino.png", 1)
        self.player.center_x = SPRITE_SIZE * 5
        self.player.center_y = SPRITE_SIZE * 1
        self.player_list.append(self.player)
        self.graph = Graph(self.wall_list)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.wall_list)

    def on_update(self, delta_time):
        if self.path:
            x_diff = self.path[0][0] - self.player.position[0]
            y_diff = self.path[0][1] - self.player.position[1]
            if x_diff == 0 and y_diff == 0:
                del self.path[0]

            self.player.change_x = MOVEMENT_SPEED * \
                (0 if x_diff == 0 else x_diff/abs(x_diff))
            self.player.change_y = MOVEMENT_SPEED * \
                (0 if y_diff == 0 else y_diff/abs(y_diff))
            print(self.player.position, self.path)

        self.physics_engine.update()

    def on_draw(self):
        try:
            arcade.start_render()

            self.wall_list.draw()
            self.texture_list.draw()
            self.player_list.draw()

        except Exception:

            import traceback
            traceback.print_exc()

    def on_mouse_press(self, x, y, button, modifiers):
        robot_pos = self.player.position[0] - \
            self.player.position[0] % 50, self.player.position[1] - \
            self.player.position[1] % 50
        end_pos = x-x % 50, y-y % 50
        start = Node(robot_pos)
        self.graph.end_node = Node(end_pos)
        self.path = arcade.astar_calculate_path(
            self.player.position, (x, y), arcade.AStarBarrierList(self.player, self.wall_list, 16, 0, 800, 0, 800))
        # self.path = [node.value for node in A_star(self.graph, [
        #    start], lambda node: node == self.graph.end_node, euclidean_distance)]


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
