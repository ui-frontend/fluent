from sdl2.sdlgfx import boxRGBA, roundedBoxRGBA, \
    rectangleRGBA, roundedRectangleRGBA

from fluent.core.property import Color
from fluent.core.widget import RenderWidget
from fluent.core.window import window


class FilledBox(RenderWidget):
    """A class used to represent an filled box (rectangle)

    Parameters
    ----------
    size : tuple
        represents size of the box

    color : tuple, optional
        color that will be using to draw
    """

    def __init__(self, size, color=Color(red=255, green=255, blue=255)):
        self.color = color

        super(FilledBox, self).__init__(size=size)

    def render(self, xy):
        boxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color.rgba[0], self.color.rgba[1], self.color.rgba[2], self.color.rgba[3]
        )


class FilledRoundedBox(RenderWidget):
    """A class used to represent an filled rounded box (rectangle)

    Parameters
    ----------
    size : tuple
        represents size of the box

    color : tuple, optional
        color that will be using to draw

    radius : int, optional
        radius that will be using on corners
    """

    def __init__(self, size, color=Color(red=255, green=255, blue=255), radius=10):
        self.color = color
        self.radius = radius

        super(FilledRoundedBox, self).__init__(size=size)

    def render(self, xy):
        roundedBoxRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1], self.radius,
            self.color.rgba[0], self.color.rgba[1], self.color.rgba[2], self.color.rgba[3]
        )


class OutlineBox(RenderWidget):
    """A class used to represent an outline box (rectangle)

    Parameters
    ----------
    size : tuple
        represents size of the box

    color : tuple, optional
        color that will be using to draw outline
    """

    def __init__(self, size, color=Color(red=255, green=255, blue=255)):
        self.color = color

        super(OutlineBox, self).__init__(size=size)

    def render(self, xy):
        rectangleRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1],
            self.color.rgba[0], self.color.rgba[1], self.color.rgba[2], self.color.rgba[3]
        )


class OutlineRoundedBox(RenderWidget):
    """A class used to represent an outline rounded box (rectangle)

    Parameters
    ----------
    size : tuple
        represents size of the box

    color : tuple, optional
        color that will be using to draw

    radius : int, optional
        radius that will be using on corners
    """

    def __init__(self, size, color=Color(red=255, green=255, blue=255), radius=10):
        self.color = color
        self.radius = radius

        super(OutlineRoundedBox, self).__init__(size=size)

    def render(self, xy):
        roundedRectangleRGBA(
            window.renderer.sdlrenderer,
            xy[0], xy[1], xy[0] + self.size[0], xy[1] + self.size[1], self.radius,
            self.color.rgba[0], self.color.rgba[1], self.color.rgba[2], self.color.rgba[3]
        )
