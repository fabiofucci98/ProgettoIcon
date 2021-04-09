import arcade
import arcade.gui
from arcade.gui import UIManager
from arcade.sprite_list import SpriteList
import create_scene
from path_finding.graph import Graph
from path_finding.path_finding import A_star


SPRITE_SIZE = 32
SCREEN_WIDTH = 1296
SCREEN_HEIGHT = 800
SCREEN_WIDTH_ROOM = 800
SCREEN_HEIGHT_ROOM = 800

SCREEN_TITLE = "AILab"


class MyGame(arcade.View):

    def __init__(self):

        super().__init__()

        self.robot = None
        self.wall_list = None
        self.texture_list = None
        self.robot = None
        self.physics_engine = None
        self.path = None
        self.barrier_list = None
        self.graph = None
        self.wall_list = None
        self.graph = None

        self.timer = .1
        self.timer_scene = 2
        self.floor = 3
        self.ui_manager = UIManager()
        self.robot = arcade.Sprite(
            "resources/robottino.png")
        self.robot.center_x, self.robot.center_y = 32*4, 32

        self.texture_list = create_scene.create_not_collidable()

        self.physics_engine = arcade.PhysicsEngineSimple(self.robot,
                                                         SpriteList())

    def on_show_view(self):
        self.change_floor()
        self.setup_interface()
        arcade.set_background_color(arcade.color.WHITE)

    def setup_interface(self):
        self.ui_manager.purge_ui_elements()

        ui_input_box = arcade.gui.UIInputBox(
            center_x=1000,
            center_y=650,
            width=300

        )
        ui_input_box.text = 'Tettegrosse'
        self.ui_manager.add_ui_element(ui_input_box)
        self.button = MyFlatButton(
            input_box=ui_input_box
        )
        self.ui_manager.add_ui_element(self.button)

    def change_floor(self):
        changes = {1: 2, 2: 3, 3: 1}
        self.floor = changes[self.floor]
        self.wall_list = create_scene.create_collidable(
            SCREEN_WIDTH_ROOM, SCREEN_HEIGHT_ROOM, SCREEN_WIDTH, SCREEN_HEIGHT, self.floor)

        self.graph = Graph(self.wall_list)
        self.physics_engine.walls = self.wall_list

    def in_elevator(self):  # 271.5 - 368.5 / 15.2 - 92.8
        if (self.robot.position[0] > 271.5 and self.robot.position[0] < 368.5) and (self.robot.position[1] > 15.2 and self.robot.position[1] < 64.1):
            return True
        return False

    def in_stairs(self):  # 703.5 - 784.5 / 463.5 - 544.5
        if (self.robot.position[0] > 719.5 and self.robot.position[0] < 784.5) and (self.robot.position[1] > 463.5 and self.robot.position[1] < 544.5):
            return True
        return False

    def on_update(self, delta_time):
        # Controlli per aggiornamento posizione
        if self.timer <= .1:
            self.timer += delta_time
        if self.path and self.timer > .1:
            self.robot.position = self.path[0]
            del self.path[0]
            self.timer = 0

        # Controlli per cambio piano
        if self.timer_scene <= 2:
            self.timer_scene += delta_time

        if self.in_elevator():
            if self.timer_scene > 2:
                self.timer_scene = 0
                self.path = A_star(
                    self.graph, [self.robot.position], (320, 112))
                self.change_floor()
        elif self.in_stairs():
            if self.timer_scene > 2:
                self.timer_scene = 0
                self.path = A_star(
                    self.graph, [self.robot.position], (688, 512))
                self.change_floor()

        if self.button.test != None:
            self.path = A_star(self.graph, [self.robot.position], (320, 64))
            self.button.test = None

        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.texture_list.draw()
        self.robot.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if x < SCREEN_WIDTH_ROOM:
            x, y = x-x % 16, y-y % 16
            robot_pos = self.robot.position
            self.path = A_star(self.graph, [robot_pos], (x, y))


class MyFlatButton(arcade.gui.UIFlatButton):
    def __init__(self, input_box):
        super().__init__(
            'CUCINA',
            center_x=1000,
            center_y=600,
            width=150,
            height=30

        )
        self.test = None
        self.input_box = input_box
        self.set_style_attrs(
            bg_color=arcade.color.BLUE,
            bg_color_hover=arcade.color.RED,
            bg_color_press=arcade.color.GREEN)

    def on_click(self):
        self.test = self.input_box.text


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = MyGame()
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()
