import numpy as np 
from random import randrange, choice, shuffle
from constants import *


class Map2D:
	# should return a map of (EMPTY) and (WALL) cells
	# rows & cols should be odd (not even)
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.r, self.c = (rows - 1)//2, (cols - 1)//2
		self.src = None
		self.dest = None
		self.grid = np.ones((rows, cols)) * WALL
		self.successors = [(0, 2), (2, 0), (0, -2), (-2, 0)]

	# to check if cell lies within the grid
	def isValid(self, coord):
		return (0 <= coord[0] < self.rows) and (0 <= coord[1] < self.cols)

	# to check if cell is blocked by a wall
	def isBlocked(self, coord):
		return self.grid[coord[0], coord[1]] == WALL

	# finding neighbours which are 2 cells away
	# isWall => whether to find blocked neighbours or unblocked
	def findNeighbours(self, coord, isWall=False):
		x, y = coord
		neighbours = [(sx + x, sy + y) for sx, sy in self.successors]
		neighbours = list(filter(lambda ngb: (self.isValid(ngb) and self.isBlocked(ngb)) if isWall else (self.isValid(ngb) and not self.isBlocked(ngb)), 
								neighbours))
		shuffle(neighbours)
		return neighbours

	# ALDOUS-BRODER METHOD
	def aldousBroder(self):
		# choose a random cell
		cx, cy = (randrange(1, self.rows, 2), randrange(1, self.cols, 2))
		self.src = (cx, cy)
		self.grid[cx, cy] = EMPTY
		numVisited = 1

		# grid is outlined by walls => R*C equally spaced cells in (2R+1)*(2C+1) grid
		while numVisited < self.r * self.c:
			# find blocked neighbours
			neighbours = self.findNeighbours((cx, cy), True)
			# switch to visited neighbour and start again
			if len(neighbours) == 0:
				cx, cy = choice(self.findNeighbours((cx, cy)))
				continue
			
			# choose random neighbour and visit it
			for nx, ny in neighbours:
				if self.grid[nx, ny] == WALL:
					# free up the adjoining cell
					self.grid[(nx + cx)//2, (ny + cy)//2] = EMPTY
					self.grid[nx, ny] = EMPTY
					numVisited += 1
					cx, cy = nx, ny
					break

		self.dest = (cx, cy)
		# src => first cell we started with
		# dest => last cell we ended up with
		return (self.grid, self.src, self.dest)
			