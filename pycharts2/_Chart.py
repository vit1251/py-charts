#

from __future__ import absolute_import

from PIL.Image import new
from PIL.ImageDraw import Draw


class AxisX(object):
    """
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.step = 8
        self.size = 8
        self.marker = 5
        self.marker_size = 16
        self.padding_left = 50
        self.padding_right = 2
        self.padding_top = 2
        self.padding_bottom = 50

    @property
    def start_x(self):
        start_x = self.padding_left - 2 * self.step
        return start_x

    @property
    def grid_start_x(self):
        start_x = self.padding_left
        return start_x

    @property
    def grid_stop_x(self):
        stop_x = self.width - self.padding_right
        return stop_x

    @property
    def start_y(self):
        start_y = self.height - self.padding_bottom
        return start_y

    @property
    def stop_x(self):
        stop_x = self.width - self.padding_right
        return stop_x

    @property
    def stop_y(self):
        stop_y = self.height - self.padding_bottom
        return stop_y

    @property
    def color(self):
        return (0, 0, 0)

    @property
    def grid(self):
        return True

    @property
    def grid_color(self):
        return (192, 192, 192)

    @property
    def grid_stop_y(self):
        return self.height - self.padding_bottom


class Chart(object):

    def __init__(self):
        self._items = []


    def register_interval(self, y, start_x, stop_x):
        self._items.append((y, start_x, stop_x))


    def _render_axis_x(self, draw, width, height, axis_x):
        # Step 1. Draw line
        draw.line([(axis_x.start_x, axis_x.start_y), (axis_x.stop_x, axis_x.stop_y)], fill=axis_x.color, width=0)
        # Step 2. Draw small scale
        for x in range(axis_x.grid_start_x, axis_x.grid_stop_x, axis_x.step):
            start = (x, axis_x.start_y)
            stop  = (x, axis_x.start_y + axis_x.size)
            draw.line([start, stop], fill=axis_x.color, width=0)
        # Step 3. Draw scale
        for x in range(axis_x.grid_start_x, axis_x.grid_stop_x, axis_x.step * axis_x.marker):
            start = (x, axis_x.start_y)
            stop  = (x, axis_x.start_y + axis_x.marker_size)
            draw.line([start, stop], fill=axis_x.color, width=0)


    def _render_grid_x(self, draw, width, height, axis_x):
        for x in range(axis_x.grid_start_x, axis_x.grid_stop_x, axis_x.step * axis_x.marker):
            start = (x, 50)
            stop  = (x, axis_x.start_y)
            draw.line([start, stop], fill=axis_x.grid_color, width=0)


    def _render_axes(self, draw, width, height, axis_x):
        """ Render Axes and grid
        """
        # Step 1. Render X-axes
        if axis_x.grid:
            self._render_grid_x(draw, width, height, axis_x)
        self._render_axis_x(draw, width, height, axis_x)
        # Step 2. Render Y-axes
        #if grid:


    def _render_values(self, draw, width, height, axis_x, color=None):
        """ Render values
        """
        if not color:
            color = (0, 0, 255)
        #
        for value_y, value_start_x, value_stop_x in self._items:
            start = (axis_x.grid_start_x + axis_x.step * value_start_x, axis_x.grid_stop_y - axis_x.step * value_y)
            stop = (axis_x.grid_start_x + axis_x.step * value_stop_x, axis_x.grid_stop_y - axis_x.step * value_y)
            draw.line([start, stop], fill=color, width=3)

    def render(self, path, width=None, height=None):
        """ Render chart

        @param str path:
        @param int width:
        @param int height:
        """
        if not width:
            width = 320
        if not height:
            height = 240
        #
        mode = "RGB"
        size = (width, height)
        color = (255, 255, 255)
        im = new(mode, size, color=color)
        draw = Draw(im)
        axis_x = AxisX(width, height)
        self._render_axes(draw, width, height, axis_x=axis_x)
        self._render_values(draw, width, height, axis_x=axis_x)
        #
        im.save(path, format="PNG")
