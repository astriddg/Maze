# -*-coding:Utf-8 -*

SOUTH_AND_EAST = 1
SOUTH = 2
EAST = 3
NONE = 4
L = 5
LR = 6
LB = 7
BR = 8

WEST = (0, -1)
EAST = (0, 1)
NORTH = (-1, 0)
SOUTH = (1, 0)

from maze import Maze

class Game:


	def __init__(self, rows, cols) :
		self.maze = Maze(rows, cols)
		self.maze.generate()
		self.grid = {}
		self.rows = rows
		self.cols = cols
		self.initiated = False
		self.over = False

	def __repr__(self):
		for i in range(1, self.cols + 1):
			self.grid[(0, i)] = self.grid[(self.rows * 2 + 1, self.cols + 1)] = BOTTOM_NO_RIGHT
		for j in range(3, self.rows * 2 + 1):
				self.grid[(j, 0)] = " |"
		if not self.initiated:
			for k in range(0, 3):
				self.grid[(k, 0)] = "  "
		elif self.initiated:
				self.grid[(0, 0)] = self.grid[(2, 0)] = "  "
				self.grid[(1, 0)] = " X"

		return self.setGrid()

	def initiate(self):
		self.initiated = True
		self.current = self.maze.grid[(0, 0)]
		self.current.visited = True
		return self.setGrid()


	def setGrid(self):
		for r in range(0, self.rows):
			for c in range (0, self.cols):
				visited, check_state = self.checkState(self.maze.grid[(r, c)])
				if not visited:
					if check_state == SOUTH_AND_EAST:
						self.grid[(r * 2 + 1, c+1)] = RIGHT # problème à régler avec c et r.
						self.grid[((r + 1) * 2, c+1)] = BOTTOM_RIGHT
					if check_state == SOUTH:
						self.grid[(r * 2 + 1, c+1)] = EMPTY
						self.grid[((r + 1) * 2, c+1)] = BOTTOM_NO_RIGHT
					if check_state == EAST:
						self.grid[(r * 2 + 1, c+1)] = RIGHT
						self.grid[((r + 1) * 2, c+1)] = RIGHT
					if check_state == NONE:
						self.grid[(r * 2 + 1, c+1)] = EMPTY
						self.grid[((r + 1) * 2, c+1)] = EMPTY
				else:
		
		final_string = ""
		for r in range(0, self.rows * 2 + 1):
			row_string = ""
			for c in range(0, self.cols + 1):
				row_string += self.grid[(r, c)]
			final_string += row_string + "\n"
		return final_string



	def checkState(self, cell):
		if not cell.visited:
			if cell.row == self.rows-1:
				if cell.e_wall:
					return False, SOUTH_AND_EAST
				else:
					return False, SOUTH
			elif cell.col == self.cols-1:
				if cell.s_wall:
					return False, SOUTH_AND_EAST
				else:
					return False, EAST
			else:
				if cell.e_wall and cell.s_wall:
					return False, SOUTH_AND_EAST
				elif cell.e_wall:
					return False, EAST
				elif cell.s_wall:
					return False, SOUTH
				else:
					return False, NONE
		else:




	def analyse(self, move):
		if move.lower() in ['w', 'a', 's', 'd']:
			if move.lower() == 'w':
				direction = TOP
			elif move.lower() == 'a':
				direction = LEFT
			elif move.lower() == 's':
				direction = BOTTOM
			else:
				direction = RIGHT


			
		else:
			return false






