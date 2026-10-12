from .render2d import Render2D

py2d = 0

def start():
    if py2d == 1:
        Render2D().run()
    elif py2d == 0:
        print("pyengines: 2D engine is off (py2d = 0).")
    else:
        print(f"pyengines: invalid py2d value: {py2d!r}. Use 0 or 1.")
