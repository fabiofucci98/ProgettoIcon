import arcade
import arcade.gui
from arcade.gui import UIManager

SPRITE_SIZE=16
SCREEN_WIDTH = 1296
SCREEN_HEIGHT = 800

class OKButton(arcade.gui.UIFlatButton):
    def __init__(self, input_box):
        super().__init__(
            'OK',
            center_x=SCREEN_WIDTH-3*SPRITE_SIZE,
            center_y=2*SPRITE_SIZE,
            width=4*SPRITE_SIZE,
            height=2*SPRITE_SIZE

        )
        self.test = None
        self.input_box = input_box
        self.set_style_attrs(
            bg_color=arcade.color.BLUE,
            bg_color_hover=arcade.color.RED,
            bg_color_press=arcade.color.GREEN)

    def on_click(self):
        self.test = self.input_box.text
        


class QueryBox(arcade.gui.UIInputBox):
    def __init__(self):
        super().__init__(
            center_x=SCREEN_WIDTH-18*SPRITE_SIZE,
            center_y=2*SPRITE_SIZE,
            width=26*SPRITE_SIZE,
            height= 2*SPRITE_SIZE,
            text ='Ciao'
        )
        self.set_style_attrs(
            bg_color= arcade.color.WHITE,
            bg_color_hover= arcade.color.WHITE_SMOKE,
            bg_color_focus = arcade.color.WHITE_SMOKE,
            font_color= arcade.color.BLACK,
            font_color_hover = arcade.color.BLACK,
            font_color_focus = arcade.color.BLACK,
            border_color= arcade.color.BABY_BLUE,
            border_color_hover = arcade.color.BABY_BLUE,
            border_color_focus =arcade.color.BABY_BLUE,
            border_width=2
            
        )
