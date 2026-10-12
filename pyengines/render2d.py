import pyglet

# ---- optional real-life light detection ----
_light_available = True
_light_missing = None
try:
    import requests
    from astral import LocationInfo
    from astral.sun import sun
    from datetime import datetime, date
except ImportError as e:
    _light_available = False
    _light_missing = e.name


def _get_real_light_phase():
    try:
        geo = requests.get("http://ip-api.com/json/", timeout=5).json()
        lat, lon, tz = geo["lat"], geo["lon"], geo["timezone"]
    except Exception as e:
        print(f"pyengines: could not detect location: {e}")
        return None

    loc = LocationInfo(latitude=lat, longitude=lon, timezone=tz)
    s = sun(loc.observer, date=date.today(), tzinfo=loc.timezone)
    now = datetime.now(s["sunrise"].tzinfo)

    if now < s["sunrise"]:
        return "night"
    if now < s["noon"]:
        return "morning"
    if now < s["sunset"]:
        return "afternoon"
    return "sunset"


_PHASE_COLORS = {
    "night":     (20, 25, 60),
    "morning":   (180, 200, 255),
    "afternoon": (255, 245, 220),
    "sunset":    (255, 140, 80),
}


class Render2D:
    def __init__(self, width=800, height=600, title="pyengines 2D",
                 physics=0, real_time=0, real_life=0, extra=0):
        self.physics = physics
        self.real_time = real_time
        self.real_life = real_life
        self.extra = extra

        self.window = pyglet.window.Window(width, height, caption=title)
        self.batch = pyglet.graphics.Batch()

        self.light_phase = None
        if self.real_life == 1:
            if not _light_available:
                print(f"pyengines: no library found: {_light_missing}")
                print(f"pyengines: install it with: pip install {_light_missing}")
            else:
                self.light_phase = _get_real_light_phase()
                if self.light_phase:
                    print(f"pyengines: real-life light phase = {self.light_phase}")

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == pyglet.window.key.ESCAPE:
                pyglet.app.exit()

        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()

    def background_color(self):
        if self.light_phase:
            r, g, b = _PHASE_COLORS.get(self.light_phase, (0, 0, 0))
            return (r, g, b, 255)
        return (0, 0, 0, 255)

    def run(self):
        r, g, b, a = self.background_color()
        pyglet.gl.glClearColor(r / 255, g / 255, b / 255, a / 255)
        pyglet.app.run()
