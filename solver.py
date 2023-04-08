import numpy as np
from math import sqrt, sin, cos, pi, copysign
from constants import *


# helper structure
class Cell:
	def __init__(self, parent=(-1, -1), f=np.Inf, g=np.Inf, h=np.Inf):
		self.parent = parent
		self.f = f 
		self.g = g
		self.h = h


# A-STAR ALGORITHM
class AStarAgent:
	def __init__(self, map2d, src, dest):
		self.map2d = map2d
		self.rows, self.cols = map2d.shape
		self.src = src 
		self.dest = dest

		self.cellMap = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]
		self.cellMap[src[0]][src[1]] = Cell(f=0, g=0, h=0, parent=(src[0], src[1]))
		self.openList = {self.src}
		self.closedList = set({})
		self.successors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		# step variables
		# STATE => 0 (validate) => 1 (process cells) => 2 (trace path) => 3 (done) 
		self.grid = np.copy(map2d)
		self.state = 0
		self.Q = None					# current cell to be evaluated
		self.foundDest = False
		self.path = []
		self.traceCell = self.dest 		# cell evaluated for back-tracing path

	# to check if cell lies within grid
	def isValid(self, coord):
		return (0 <= coord[0] < self.rows) and (0 <= coord[1] < self.cols)

	# to check if cell is not blocked by a wall
	def isUnblocked(self, coord):
		return self.map2d[coord[0], coord[1]] != WALL

	# to calculate heuristic value (Manhattan / Diagonal / Euclidean)
	def calcHvalue(self, coord):
		dx = abs(coord[0] - self.dest[0])
		dy = abs(coord[1] - self.dest[1])
		# Manhattan Distance (4)
		return dx + dy
		# # Diagonal Distance (8)
		# return sqrt(2)*min(dx, dy) + abs(dx - dy)
		# # Euclidean Distance (any)
		# return sqrt( dx**2 + dy**2 )

	# single step for simulation
	def step(self):
		# validate map
		if self.state == 0:
			self.state += 1
			if (not self.isValid(self.src) or not self.isValid(self.dest)):
				print("Source or Destination is invalid: ({}, {}), ({}, {})".format(self.src.x, self.src.y, self.dest.x, self.dest.y))
				self.state = 3
			elif (self.src == self.dest):
				print("Source is the destination")
				self.path.append(self.src)
				self.state = 3

		# process cells
		elif self.state == 1:
			# while openlist is not empty
			if (len(self.openList) == 0 and not self.foundDest):
				print("Failed to find destination")
				self.state = 3
			else:
				# find node with least "F" value in openlist
				if not self.Q:
					self.Q = min(self.openList, key=lambda coord: self.cellMap[coord[0]][coord[1]].f)
					self.openList.remove(self.Q)
					self.closedList.add(self.Q)

				x, y = self.Q
				self.grid[x, y] = CLOSED
				for successor in self.successors:
					newX, newY = newQ = (x + successor[0], y + successor[1])
					if (self.isValid(newQ) and self.isUnblocked(newQ)):
						# if successor is destination, stop search
						if (newQ == self.dest):
							self.cellMap[newX][newY].parent = (x, y)
							self.foundDest = True
							print("Destination reached")
							self.state = 2
						else:
							# not in any list => add to openlist, update
							# in openlist => newF < oldF => add to openlist, update
							#             => newF > oldF => skip
							# in closedlist => newF < oldF => add to openlist, update
							#               => newF > oldF => skip
							newG = self.cellMap[x][y].g + 1.0
							newH = self.calcHvalue(newQ)
							newF = newG + newH
							if (self.cellMap[newX][newY].f > newF):
								if (newQ in self.closedList):
									print("found in closedlist", newQ)
									self.closedList.remove(newQ)
								self.openList.add(newQ)
								self.grid[newX, newY] = OPEN
								self.cellMap[newX][newY] = Cell(f=newF, g=newG, h=newH, parent=self.Q)
				self.Q = None

		# trace path
		elif self.state == 2:
			# process dest
			self.path.append(self.traceCell)
			x, y = self.cellMap[self.traceCell[0]][self.traceCell[1]].parent
			if (self.cellMap[x][y].parent == (x, y)):
				# process src
				self.path.append((x, y))
				self.state = 3
			else:
				# process intermediate cells
				self.traceCell = (x, y)
				self.grid[x, y] = PATH
			

		return self.grid, self.state >= 3