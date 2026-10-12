from .render2d import Render2D

# 2D engine settings
py2d = 0
pysics2D = 0
pyrealT2D = 0
pyrealL2D = 0
pyextra2D = 0


def start():
    if py2d == 1:
        Render2D(
            physics=pysics2D,
            real_time=pyrealT2D,
            real_life=pyrealL2D,
            extra=pyextra2D,
        ).run()
    elif py2d == 0:
        print("pyengines: 2D engine is off (py2d = 0).")
    else:
        print(f"pyengines: invalid py2d value: {py2d!r}. Use 0 or 1.")
