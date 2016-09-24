
# -*-coding:Utf-8 -*

TOP_RIGHT = "   |"
EMPTY = "    "
BOTTOM_RIGHT = "_ _|"
BOTTOM_NO_RIGHT = "_ _ "
NO_BOTTOM_RIGHT = "   |"

SOUTH_AND_EAST = 1
SOUTH = 2
EAST = 3
NONE = 4

from maze import Maze

class Game:


	def __init__(self, rows, cols) :
		self.maze = Maze(rows, cols)
		self.maze.generate()
		self.grid = {}
		self.rows = rows
		self.cols = cols

	def __repr__(self):
		for i in range(1, self.cols + 1):
			self.grid[(0, i)] = self.grid[(self.rows * 2 + 1, self.cols + 1)] = BOTTOM_NO_RIGHT
		for j in range(3, self.rows * 2 + 1):
			self.grid[(j, 0)] = " |"
		for k in range(0, 3):
			self.grid[(k, 0)] = "  "

		return self.setGrid()

	def setGrid(self):
		for r in range(0, self.rows):
			for c in range (0, self.cols):
				check_state = self.checkState(self.maze.grid[(r, c)])
				if check_state == SOUTH_AND_EAST:
					self.grid[(r * 2 + 1, c+1)] = TOP_RIGHT # problème à régler avec c et r.
					self.grid[((r + 1) * 2, c+1)] = BOTTOM_RIGHT
				if check_state == SOUTH:
					self.grid[(r * 2 + 1, c+1)] = EMPTY
					self.grid[((r + 1) * 2, c+1)] = BOTTOM_NO_RIGHT
				if check_state == EAST:
					self.grid[(r * 2 + 1, c+1)] = TOP_RIGHT
					self.grid[((r + 1) * 2, c+1)] = NO_BOTTOM_RIGHT
				if check_state == NONE:
					self.grid[(r * 2 + 1, c+1)] = EMPTY
					self.grid[((r + 1) * 2, c+1)] = EMPTY
		
		final_string = ""
		for r in range(0, self.rows * 2 + 1):
			row_string = ""
			for c in range(0, self.cols + 1):
				row_string += self.grid[(r, c)]
			final_string += row_string + "\n"
		return final_string



	def checkState(self, cell):
		if cell.row == self.rows-1:
			if cell.e_wall:
				return SOUTH_AND_EAST
			else:
				return SOUTH
		elif cell.col == self.cols-1:
			if cell.s_wall:
				return SOUTH_AND_EAST
			else:
				return EAST
		else:
			if cell.e_wall and cell.s_wall:
				return SOUTH_AND_EAST
			elif cell.e_wall:
				return EAST
			elif cell.s_wall:
				return SOUTH
			else:
				return NONE



game = Game(20, 20)

print(game)


