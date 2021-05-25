import arcade
import arcade.gui

SPRITE_SIZE = 16
SCREEN_WIDTH = 1296
SCREEN_HEIGHT = 800


class ComandLabel(arcade.gui.UILabel):
    def __init__(self, text, p):
        super().__init__(
            text=text,
            center_x=1040,
            center_y=SCREEN_HEIGHT-2*SPRITE_SIZE-8-p*2*SPRITE_SIZE,
            width=28*SPRITE_SIZE,
            align='left'
        )

        self.set_style_attrs(
            font_size=SPRITE_SIZE,
            font_color=arcade.color.GO_GREEN,
            font_color_focus=arcade.color.GO_GREEN,
            font_color_hover=arcade.color.GO_GREEN,
            font_color_press=arcade.color.RED
        )
        self.click = False

    def on_click(self):
        if self.click == False:
            self.set_style_attrs(
                font_color=arcade.color.RED,
                font_color_focus=arcade.color.RED,
                font_color_hover=arcade.color.RED,
                font_color_press=arcade.color.GO_GREEN
            )
            self.click = True
        else:
            self.set_style_attrs(
                font_color=arcade.color.GO_GREEN,
                font_color_focus=arcade.color.GO_GREEN,
                font_color_hover=arcade.color.GO_GREEN,
                font_color_press=arcade.color.RED
            )
            self.click = False


class OKButton(arcade.gui.UIFlatButton):
    def __init__(self, input_box):
        super().__init__(
            'OK',
            center_x=SCREEN_WIDTH-3*SPRITE_SIZE,
            center_y=2*SPRITE_SIZE,
            width=4*SPRITE_SIZE,
            height=2*SPRITE_SIZE

        )
        self.input_box = input_box
        self.set_style_attrs(
            bg_color=arcade.color.BLUE,
            bg_color_hover=arcade.color.RED,
            bg_color_press=arcade.color.GREEN)
        self.cron = []
        self.cron_index = 0
        self.pres = False

    def on_click(self):
        self.cron.append('>>'+self.input_box.text)
        self.pres = True

    def get_text(self):
        return self.input_box.text

    def get_cron(self):
        return self.cron[self.cron_index:]


class QueryBox(arcade.gui.UIInputBox):
    def __init__(self):
        super().__init__(
            center_x=SCREEN_WIDTH-18*SPRITE_SIZE,
            center_y=2*SPRITE_SIZE,
            width=26*SPRITE_SIZE,
            height=2*SPRITE_SIZE,
            text=''
        )
        self.set_style_attrs(
            bg_color=arcade.color.WHITE,
            bg_color_hover=arcade.color.WHITE_SMOKE,
            bg_color_focus=arcade.color.WHITE_SMOKE,
            font_color=arcade.color.GRAY,
            font_color_hover=arcade.color.GRAY,
            font_color_focus=arcade.color.GRAY,
            border_color=arcade.color.BABY_BLUE,
            border_color_hover=arcade.color.BABY_BLUE,
            border_color_focus=arcade.color.BABY_BLUE,
            border_width=2

        )

    def on_click(self):
        self.text = ''
        self.set_style_attrs(
            font_color=arcade.color.BLACK,
            font_color_hover=arcade.color.BLACK,
            font_color_focus=arcade.color.BLACK)
