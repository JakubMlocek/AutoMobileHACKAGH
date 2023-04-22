from kivy.graphics import RoundedRectangle
from kivy.properties import ListProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.textinput import TextInput


class RoundedTextInput(TextInput, FocusBehavior):
    """A rounded text input widget"""

    # color of the border when the text input is in focus
    border_color_focus = ListProperty([0, 0.7, 1, 1])

    def __init__(self, **kwargs):
        super(RoundedTextInput, self).__init__(**kwargs)

        # set background images for normal and active states
        self.background_normal = "rounded_normal.png"
        self.background_active = "rounded_active.png"

    def on_size(self, *args):
        """Redraw the border when the size of the widget changes"""

        # calculate the radius of the corners based on the widget height
        radius = self.height / 2.0

        # create a rounded rectangle with the current widget size and corner radius
        self.canvas.before.clear()
        with self.canvas.before:
            RoundedRectangle(pos=self.pos, size=self.size, radius=[radius])
