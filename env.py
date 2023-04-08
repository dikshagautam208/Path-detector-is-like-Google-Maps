import pygame
from constants import *


class Env:
	def __init__(self, screenWidth, screenHeight, gameSpeed):
		pygame.init()
		self.screen = pygame.display.set_mode((screenWidth, screenHeight))
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight
		pygame.display.set_caption("Maze")
		# refresh rate
		self.clock = pygame.time.Clock()
		self.gameSpeed = gameSpeed

	def reset(self):
		self.close()
		self.__init__(self.screenWidth, self.screenHeight)

	# flip the screen state
	def render(self, grid, src, dest):
		self.draw(grid, src, dest)
		pygame.display.flip()
		self.clock.tick(self.gameSpeed)

	# draw different cells, src & dest on top of everything
	def draw(self, grid, src, dest):
		self.screen.fill(COLORS[WALL])
		self.cellWidth = self.screenWidth//grid.shape[1]
		self.cellHeight = self.screenHeight//grid.shape[0]
		for x in range(grid.shape[0]):
			for y in range(grid.shape[1]):
				pygame.draw.rect(self.screen, COLORS[grid[x, y]], (y*self.cellWidth,
																x*self.cellHeight,
																self.cellWidth,
																self.cellHeight) )

		pygame.draw.rect(self.screen, COLORS[SRC], (src[1]*self.cellWidth,
													src[0]*self.cellHeight,
													self.cellWidth,
													self.cellHeight) )

		pygame.draw.rect(self.screen, COLORS[DEST], (dest[1]*self.cellWidth,
													dest[0]*self.cellHeight,
													self.cellWidth,
													self.cellHeight) )

	def close(self):
		pygame.display.quit()
		pygame.quit()