import arcade
import create_scene
from graph import Graph
from path_finding import A_star


SPRITE_SIZE = 32
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SCREEN_TITLE = "Culo"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.player_list = None
        self.wall_list = None
        self.texture_list = None
        self.player = None
        self.physics_engine = None
        self.path = None
        self.barrier_list = None
        self.graph = None
        self.timer = 0

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = create_scene.create_collidable(
            SCREEN_WIDTH, SCREEN_HEIGHT)
        self.texture_list = create_scene.create_not_collidable()
        self.player = arcade.Sprite(
            "resources/robottino.png")
        self.player.center_x = SPRITE_SIZE * 5
        self.player.center_y = SPRITE_SIZE * 1
        self.player_list.append(self.player)
        self.graph = Graph(self.wall_list)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.wall_list)

    def on_update(self, delta_time):
        self.timer += delta_time
        if self.path and self.timer > .1:

            self.player.position = self.path[0]
            del self.path[0]
            self.timer = 0

        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.texture_list.draw()
        self.player_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        x, y = x-x % 16, y-y % 16
        robot_pos = self.player.position
        self.path = A_star(self.graph, [robot_pos], (x, y))


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
