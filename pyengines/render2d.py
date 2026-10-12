import pyglet


class Render2D:
    def __init__(self, width=800, height=600, title="pyengines 2D"):
        self.window = pyglet.window.Window(width, height, caption=title)
        self.batch = pyglet.graphics.Batch()
        self.shapes = []

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == pyglet.window.key.ESCAPE:
                pyglet.app.exit()

        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()

    def add_rect(self, x, y, w, h, color=(255, 255, 255, 255)):
        rect = pyglet.shapes.Rectangle(x, y, w, h, color=color, batch=self.batch)
        self.shapes.append(rect)
        return rect

    def run(self):
        pyglet.app.run()
