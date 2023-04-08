# pygame constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_SPEED = 50

# rows, cols should be odd (2r + 1)
ROWS = 69
COLS = 69
SUCCESSORS = 4

# cell codes
EMPTY = 0
WALL = 1
SRC = 2
DEST = 3
PATH = 4
OPEN = 5
CLOSED = 6

# cell color scheme
COLORS = {
	0: (255,255,255),	# white
	1: (0,0,0),			# black
	2: (255,0,0),		# red
	3: (0,128,0),		# green
	4: (165,42,42),		# brown
	5: (255,255,0),		# yellow
	6: (255,165,0),		# orange
}