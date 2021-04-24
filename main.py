import arcade
import arcade.gui
from arcade.gui import UIManager
import keyboard
from arcade.sprite_list import SpriteList
import create_scene
import GUI
from path_finding.graph import Graph
from path_finding.path_finding import A_star


SPRITE_SIZE = 16
SCREEN_WIDTH = 1296
SCREEN_HEIGHT = 800
SCREEN_WIDTH_ROOM = 800
SCREEN_HEIGHT_ROOM = 800

SCREEN_TITLE = "AILab"

Stanze = {}
Stanze['Cucina'] = (368, 128)
Stanze['Laboratorio'] = (256, 416)
Stanze['Bagno'] = (80, 224)
Stanze['Libreria'] = (368, 688)
Stanze['Meccanica'] = (416, 448)
Stanze['Elettronica'] = (624, 448)
Stanze['Scale'] = (720, 496)
Stanze['Ascensore'] = (320, 48)
Stanze['Serra'] = (560, 544)
Stanze['Camera da letto'] = (64, 320)
Stanze['Sgabuzzino'] = (608, 228)


class MyGame(arcade.View):

    def __init__(self):

        super().__init__()

        self.robot = None
        self.wall_list = None
        self.texture_list = None
        self.physics_engine = None
        self.path = None
        self.barrier_list = None
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
        self.to_draw = True

    def on_show_view(self):
        self.change_floor()
        self.setup_interface()
        arcade.set_background_color(arcade.color.WHITE)

    def setup_interface(self):
        self.ui_manager.purge_ui_elements()
        self.ui_input_box = GUI.QueryBox()
        self.ui_manager.add_ui_element(self.ui_input_box)
        self.button = GUI.OKButton(
            input_box=self.ui_input_box
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

        in_elevator = self.in_elevator()
        in_stairs = self.in_stairs()
        if in_elevator or in_stairs:
            if self.timer_scene > 2:
                self.timer_scene = 0
                self.path = A_star(
                    self.graph, [self.robot.position], (688, 512) if in_stairs else (320, 112))
                self.change_floor()

        text = self.button.get_text()
        if self.button.pres and text in Stanze:
            self.path = A_star(
                self.graph, [self.robot.position], Stanze[text])
            self.button.pres = False
            self.ui_input_box.text = ''
        elif self.button.pres and text not in Stanze and text != "QueryBox":
            self.button.pres = False
            self.button.cron.remove(self.ui_input_box.text)
            self.button.cron.append("[Invalid Query]")
            self.ui_input_box.text = ''
            

        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.texture_list.draw()
        self.robot.draw()
        #print(len(self.button.get_cron()))
        for i, elem in enumerate(self.button.get_cron()):
            arcade.draw_text(
                elem, SCREEN_WIDTH_ROOM+8, (SCREEN_HEIGHT/2-40)-20*i, arcade.color.BLACK)
            

    def on_mouse_press(self, x, y, button, modifiers):
        if x < SCREEN_WIDTH_ROOM:
            x, y = x-x % 16, y-y % 16
            robot_pos = self.robot.position
            self.path = A_star(self.graph, [robot_pos], (x, y))

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        # aggiungere parte per scroll solo in riquadro basso a dx
        if x > SCREEN_WIDTH_ROOM and x < SCREEN_WIDTH and y > 3*SPRITE_SIZE and y < SCREEN_HEIGHT/2:
            self.button.cron_index += scroll_y
    
    def on_key_press(self,key,modifiers):
        if key == arcade.key.ENTER:
            if self.ui_input_box.focused is True:
                self.button.on_click()
                
    

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = MyGame()
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()
