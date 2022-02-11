from typing import List
import numpy as np
from time import sleep
iterations=100



class UnicodeEngine:
    size: int
    grid: np.ndarray
    rendered_grid: np.ndarray
    opacity_map = {0.99:'@', 0.75:'x', 0.5:'*', 0.1:'.'}

    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size))
        self.rendered_grid = np.chararray((size, size))

    def load_bin(self,ar):
        scale = ar.shape[0] // self.size
        grid = np.zeros((self.size,self.size))
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i,j] = ar[i*scale:(i+1)*scale, j*scale:(j+1)*scale].sum()/(scale**2)
    
    def color(self, val):
        for sym in self.opacity_map:
            if val > sym:
                return self.opacity_map.get(sym)
        return ' '
    
    def render(self):
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                self.rendered_grid[i,j] = self.color(self.grid[i,j])
    
    def display(self):
        for row in self.rendered_grid.T.decode():
            s = ""
            for c in row:
                s+=2*c
            print(s)
