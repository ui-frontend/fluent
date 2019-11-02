from rocket.render import stringRGBA, window
from rocket.widget import GenericWidget, color


class String(GenericWidget):
    def __init__(self, text, color=color.white):
        self.text = text
        self.color = color
        # TODO: Add text size calculation

        super(String, self).__init__(size=(0, 0))

    def render(self, xy):
        stringRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], bytes(self.text, 'utf-8'),
            self.color.red, self.color.green, self.color.blue, self.color.alpha
        )