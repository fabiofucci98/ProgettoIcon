from engine import Clause, parse
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
        arcade.set_background_color(arcade.color.WHITE)

        self.texture_list = create_scene.create_not_collidable()
        self.wall_lists = [create_scene.create_collidable(
            SCREEN_WIDTH_ROOM, SCREEN_HEIGHT_ROOM, SCREEN_WIDTH, SCREEN_HEIGHT, floor) for floor in range(1, 4)]
        self.wall_list = self.wall_lists[0]

        self.floor = 1
        self.robot_sprite = arcade.Sprite("resources/robottino.png")
        self.robot_sprite.center_x, self.robot_sprite.center_y = 128, 32
        self.robot = Agent(self.wall_lists, 'kb',
                           self.robot_sprite, self.floor)

        self.ass_lbls = [str(ass) for ass in self.robot.engine.ass]
        self.ass_colors = [True for i in range(len(self.ass_lbls))]
        self.ass_index = 0
        self.messages_index = 0
        self.messages = []

        self.timer = .1
        self.ui_manager = UIManager()
        self.ui_input_box = gui.QueryBox()
        self.ui_manager.add_ui_element(self.ui_input_box)
        self.button = gui.OkButton(self.ui_input_box, self.messages)
        self.ui_manager.add_ui_element(self.button)

        self.physics_engine = arcade.PhysicsEngineSimple(self.robot_sprite,
                                                         self.wall_list)

    def on_update(self, delta_time):
        self.update_position(delta_time)
        self.robot.update_path(delta_time,
                               self.ass_lbls, self.ass_colors)
        self.update_ui()
        self.update_assumables()
        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.texture_list.draw()
        self.robot_sprite.draw()
        self.draw_messages()
        self.draw_ass_lbls()

    def draw_messages(self):
        for i, elem in enumerate(self.messages[self.messages_index:]):
            if i >= 14:
                break
            arcade.draw_text(
                elem, SCREEN_WIDTH_ROOM+8, (SCREEN_HEIGHT/2-40)-24*i, arcade.color.BLACK, font_size=16)

    def draw_ass_lbls(self):
        for i, elem in enumerate(self.ass_lbls[self.ass_index:]):
            if i >= 16:
                break
            color = arcade.color.GREEN if self.ass_colors[self.ass_index +
                                                          i] else arcade.color.RED
            arcade.draw_text(
                elem, SCREEN_WIDTH_ROOM+8, (SCREEN_HEIGHT-40)-24*i, color, font_size=16)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        if x > SCREEN_WIDTH_ROOM and x < SCREEN_WIDTH and y > 3*SPRITE_SIZE and y < SCREEN_HEIGHT/2:
            updated_index = self.messages_index + int(scroll_y)
            if updated_index >= 0 and updated_index < len(self.messages):
                self.messages_index = updated_index

        if x > SCREEN_WIDTH_ROOM and x < SCREEN_WIDTH and y < SCREEN_HEIGHT and y > SCREEN_HEIGHT/2:
            updated_index = self.ass_index + int(scroll_y)
            if updated_index >= 0 and updated_index < len(self.ass_lbls):
                self.ass_index = updated_index

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        index = -(y//24-32)
        if x > SCREEN_WIDTH_ROOM and x < SCREEN_WIDTH and y < SCREEN_HEIGHT-16 and y > SCREEN_HEIGHT/2 and index < len(self.ass_colors[self.ass_index:]):
            self.ass_colors[self.ass_index +
                            index] = not self.ass_colors[self.ass_index+index]

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
        if self.button.pres:
            text = self.button.get_text()
            self.button.pres = False
            self.ui_input_box.text = ''
            self.robot.act(text)

        if self.robot.message:
            self.messages.extend(self.robot.message)
            self.robot.message = []

    def update_assumables(self):
        str_ass = [str(ass) for ass in self.robot.engine.ass]
        for i, ass in enumerate(self.ass_lbls):
            parsed = parse(ass+'.')[0]
            color = self.ass_colors[i]
            if color and str(parsed) not in str_ass:
                self.robot.engine.kb.append(Clause(parsed))
                self.robot.engine.ass.append(parsed)
            elif not color and str(parsed) in str_ass:
                del self.robot.engine.ass[self.robot.engine.ass.index(parsed)]
                del self.robot.engine.kb[self.robot.engine.kb.index(
                    Clause(parsed))]

    def change_floor(self, floor):
        self.floor = floor
        self.wall_list = self.wall_lists[floor-1]
        self.physics_engine.walls = self.wall_list
        self.robot.floor = floor
        self.robot.floor_to_go = None


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
