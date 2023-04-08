from constants import *
from env import *
from map import *
from solver import *


def main():
	# environment to render maze
	env = Env(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_SPEED)
	# maze generator
	map2d = Map2D(ROWS, COLS)
	grid, src, dest = map2d.aldousBroder()
	# maze solver
	solver = AStarAgent(grid, src, dest)

	# rendering loop
	done = False
	while True:
		newGrid, done = solver.step()
		env.render(newGrid, src, dest)
	env.close()


if __name__ == "__main__":
	main()