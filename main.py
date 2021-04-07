import arcade
import create_scene_ground_floor
import create_scene_up_floor
import create_scene_down_floor
from graph import Graph
from path_finding import A_star


SPRITE_SIZE = 32
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
SCREEN_WIDTH_ROOM = 800

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
        self.timer = None
        self.timer_scene = 2

        arcade.set_background_color(arcade.color.WHITE)

    def setup_ground_floor(self, robot_pos):
        self.check = 1
        self.player_list = arcade.SpriteList()
        self.wall_list = create_scene_ground_floor.create_collidable(
            SCREEN_WIDTH_ROOM, SCREEN_HEIGHT)
        self.texture_list = create_scene_ground_floor.create_not_collidable()
        self.player = arcade.Sprite(
            "resources/robottino.png")
        self.player.center_x, self.player.center_y = robot_pos

        self.player_list.append(self.player)
        self.graph = Graph(self.wall_list)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.wall_list)

    def setup_up_floor(self, robot_pos):
        self.check = 2
        self.player_list = arcade.SpriteList()
        self.wall_list = create_scene_up_floor.create_collidable(
            SCREEN_WIDTH_ROOM, SCREEN_HEIGHT)
        self.texture_list = create_scene_up_floor.create_not_collidable()
        self.player = arcade.Sprite(
            "resources/robottino.png")
        self.player.center_x, self.player.center_y = robot_pos

        self.player_list.append(self.player)
        self.graph = Graph(self.wall_list)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.wall_list)

    def setup_down_floor(self, robot_pos):
        self.check = 3
        self.player_list = arcade.SpriteList()
        self.wall_list = create_scene_down_floor.create_collidable(
            SCREEN_WIDTH_ROOM, SCREEN_HEIGHT)
        self.texture_list = create_scene_down_floor.create_not_collidable()
        self.player = arcade.Sprite(
            "resources/robottino.png")
        self.player.center_x, self.player.center_y = robot_pos
        self.player_list.append(self.player)
        self.graph = Graph(self.wall_list)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.wall_list)

    def in_stairs(self):
        if (self.player.position[0] > 271.5 and self.player.position[0] < 368.5) and (self.player.position[1] > 15.2 and self.player.position[1] < 92.8):
            return True
        return False

    def in_elevator(self):
        if (self.player.position[0] > 703.5 and self.player.position[0] < 784.5) and (self.player.position[1] > 463.5 and self.player.position[1] < 544.5):
            return True
        return False

    def on_update(self, delta_time):
        if self.timer != None:
            self.timer += delta_time
        if self.timer == None and self.path:
            self.timer = 0
        if self.path and self.timer > .1:
            self.player.position = self.path[0]
            del self.path[0]
            self.timer = 0
            if len(self.path) == 0:
                self.timer = None
        self.physics_engine.update()

        # fare controllo di posizione e scena, se scena 1 e posizione in ascensore o scale, richiama scena 2
        # [0] = x, [1] = y;
        self.timer_scene += delta_time
        if self.in_stairs() or self.in_elevator():
            if self.timer_scene > 2:
                self.timer_scene = 0
                self.cambia(self.player.position)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.texture_list.draw()
        self.player_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if x < 800:
            x, y = x-x % 16, y-y % 16
            robot_pos = self.player.position
            self.path = A_star(self.graph, [robot_pos], (x, y))

    def cambia(self, robot_pos):
        if self.check == 1:
            self.clear()
            self.setup_up_floor(robot_pos)
        else:
            self.clear()
            self.setup_ground_floor(robot_pos)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup_ground_floor((32*5, 32))
    arcade.run()


if __name__ == "__main__":
    main()
