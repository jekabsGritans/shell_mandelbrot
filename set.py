from rendering import UnicodeEngine
import numpy as np

def diverges(c):
    def f(z):
        if z == 0: return 0
        return f(z-1)**2+c
    return abs(f(10)) > 4


class MandleSet:
    grid: np.ndarray
    size: int

    def __init__(self, size):
        self.grid = np.zeros((size,size))
        self.size = size

    def generate(self):
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                self.grid[i,j] = not diverges(complex(i, j)/300 - complex(2,2))

    def point_diverges(c):
        def f(z):
            if z == 0: return 0
            return f(z-1)**2+c
        return abs(f(10)) > 4


ms = MandleSet(1000)

ms.generate()
e = UnicodeEngine(75)

e.load_bin(ms.grid)
e.render()
e.display()
