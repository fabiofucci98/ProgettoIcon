from agent import Agent
import arcade
import arcade.gui
from arcade.gui import UIManager
import create_scene
import gui

SPRITE_SIZE = 16
SCREEN_WIDTH = 1296
SCREEN_HEIGHT = 800
SCREEN_WIDTH_ROOM = 800
SCREEN_HEIGHT_ROOM = 800

SCREEN_TITLE = "AILab"


class MyGame(arcade.View):

    def __init__(self):
        super().__init__()

        self.texture_list = None
        self.physics_engine = None
        self.action = None

        self.floor = 1
        self.wall_lists = [create_scene.create_collidable(
            SCREEN_WIDTH_ROOM, SCREEN_HEIGHT_ROOM, SCREEN_WIDTH, SCREEN_HEIGHT, floor) for floor in range(1, 4)]
        self.robot_sprite = arcade.Sprite("resources/robottino.png")
        self.robot_sprite.center_x, self.robot_sprite.center_y = 128, 32
        self.robot = Agent(self.wall_lists, 'kb',
                           self.robot_sprite, self.floor)
        self.wall_list = self.wall_lists[0]
        self.timer = .1
        self.ui_manager = UIManager()

        self.texture_list = create_scene.create_not_collidable()

        self.physics_engine = arcade.PhysicsEngineSimple(self.robot_sprite,
                                                         self.wall_list)
        self.to_draw = True

    def on_show_view(self):
        self.ui_manager.purge_ui_elements()
        self.ui_input_box = gui.QueryBox()
        self.ui_manager.add_ui_element(self.ui_input_box)
        self.button = gui.OKButton(
            input_box=self.ui_input_box
        )
        self.ui_manager.add_ui_element(self.button)
        arcade.set_background_color(arcade.color.WHITE)

    def change_floor(self, floor):
        self.floor = floor
        self.wall_list = self.wall_lists[floor-1]
        self.physics_engine.walls = self.wall_list
        self.robot.floor = floor
        self.robot.floor_to_go = None

    def on_update(self, delta_time):

        # Controlli per cambio piano e aggiornamento posizione
        self.update_position(delta_time)
        self.update_ui()
        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.texture_list.draw()
        self.robot_sprite.draw()
        for i, elem in enumerate(self.button.get_cron()):
            if i > 16:
                break
            arcade.draw_text(
                elem, SCREEN_WIDTH_ROOM+8, (SCREEN_HEIGHT/2-40)-20*i, arcade.color.BLACK)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        # aggiungere parte per scroll solo in riquadro basso a dx
        if x > SCREEN_WIDTH_ROOM and x < SCREEN_WIDTH and y > 3*SPRITE_SIZE and y < SCREEN_HEIGHT/2:
            updated_index = self.button.cron_index + int(scroll_y)
            if updated_index >= 0 and updated_index < len(self.button.cron):
                self.button.cron_index = updated_index

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            if self.ui_input_box.focused is True:
                self.button.on_click()

    def update_position(self, delta_time):

        if self.timer <= .1:
            self.timer += delta_time
        if self.robot.path and self.timer > .1:
            self.robot_sprite.position = self.robot.path[0]
            if in_elevator(self.robot.sprite.position) or in_stairs(self.robot.sprite.position):
                self.change_floor(self.robot.floor_to_go)
            del self.robot.path[0]
            self.timer = 0

    def update_ui(self):
        text = self.button.get_text()
        if self.button.pres:
            self.button.pres = False
            self.ui_input_box.text = ''
            self.action, message = self.robot.act(text)
            self.button.cron.append(message)


def in_elevator(robot_pos):
    if robot_pos[0] == 320 and robot_pos[1] == 48:
        return True
    return False


def in_stairs(robot_pos):
    if robot_pos[0] == 720 and robot_pos[1] == 496:
        return True
    return False


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = MyGame()
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()
