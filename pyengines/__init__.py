from .render2d import Render2D

def start(mode="2d", width=800, height=600):
    if mode == "2d":
        Render2D(width, height).run()
    else:
        raise ValueError(f"pyengines: unknown mode {mode!r}. Try mode='2d'.")
