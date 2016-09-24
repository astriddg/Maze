

import random

N = (-1, 0)
S = (1, 0)
W = (0, -1)
E = (0, 1) 

class Cell:

	def __init__(self, row, col):
		self.row = row
		self.col = col

		self.n_wall = True
		self.s_wall = True
		self.e_wall = True
		self.w_wall = True

	def closed(self):
		return self.n_wall and self.s_wall and self.e_wall and self.w_wall



class Maze:


	def __init__(self, rows, cols) :
		self.rows = rows
		self.cols = cols
		self.grid = {}

	def generate(self):
		self.reset()
		self.total = self.rows * self.cols
		self.current_cell = self.start
		self.visited = 1
		cell_stack = []

		while self.visited < self.total:
			
			neighbours = self.findNeighbours(self.current_cell)
			if len(neighbours) >= 1: # may not work
				neighbour = random.choice(neighbours)
				if neighbour[1] == N:
					self.current_cell.n_wall = False
					neighbour[0].s_wall = False
				elif neighbour[1] == S:
					self.current_cell.s_wall = False
					neighbour[0].n_wall = False
				elif neighbour[1] == W:
					self.current_cell.w_wall = False
					neighbour[0].e_wall = False
				elif neighbour[1] == E:
					self.current_cell.e_wall = False
					neighbour[0].w_wall = False
				cell_stack.append(self.current_cell)
				self.current_cell = neighbour[0]
				self.visited += 1
			else:
				self.current_cell = cell_stack.pop()
			
		self.end.e_wall = False


	def reset(self):
		for r in range(self.rows):
			for c in range(self.cols):
				self.grid[(r, c)] = Cell(r, c)
		self.start = self.grid[(0, 0)] 
		self.end = self.grid[(self.rows-1, self.cols-1)]

	def findNeighbours(self, current_cell):
		directions = [N, S, W, E]
		neighbours = []
		for d in directions:
			temp_r, temp_c = current_cell.row + d[0], current_cell.col + d[1]
			if temp_r >= 0 and temp_c >= 0 and temp_r < self.rows and temp_c < self.cols:
				if self.grid[(temp_r, temp_c)].closed():
					" mon chien"
					neighbour = self.grid[(temp_r, temp_c)]
					neighbours.append((neighbour, d))
		return neighbours



		
