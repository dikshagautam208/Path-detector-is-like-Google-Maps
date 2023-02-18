import numpy as np 
from math import sqrt

EMPTY = 0
OBSTACLE = 1
SRC = 2
DEST = 3


class Cell:

	def __init__(self, x, y parent=(-1, -1), f=np.Inf, g=np.Inf, h=np.Inf):
		self.x = x
		self.y = y
		self.parent = parent
		self.f = f 
		self.g = g
		self.h = h


class Map2D:

	def __init__(self, rows, cols, src, dest):
		self.rows = rows
		self.cols = cols
		self.src = src
		self.dest = dest

		self.map = np.zeros((rows, cols))
		self.map[src[0], src[1]] = SRC
		self.map[dest[0], dest[1]] = DEST
		self.cellMap = [[Cell(x, y) for y in range(self.cols)] for x in range(self.rows)]

	def isValid(self, cell):
		return (0 <= cell.x < self.rows) and (0 <= cell.y < self.cols)

	def calcHvalue(self, cell):
		return sqrt( (cell.x - self.dest.x)**2 + (cell.y - self.dest.y)**2 )

	def addObstacles(self, x, y):
		pass

	def getOptimalRoute(self):
		pass
