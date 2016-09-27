# -*-coding:Utf-8 -*


from maze import Maze
import designs
import directions


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
			self.grid[(0, i)] = self.grid[(self.rows * 2 + 1, self.cols + 1)] = designs.BOTTOM_NO_RIGHT
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
				neighbours, check_state = self.checkState(self.maze.grid[(r, c)])

				if not neighbours:
					if check_state == directions.SOUTH_AND_EAST:
						self.grid[(r * 2 + 1, c+1)] = designs.RIGHT # problème à régler avec c et r.
						self.grid[((r + 1) * 2, c+1)] = designs.BOTTOM_RIGHT
					elif check_state == directions.SOUTH_O:
						self.grid[(r * 2 + 1, c+1)] = designs.EMPTY
						self.grid[((r + 1) * 2, c+1)] = designs.BOTTOM_NO_RIGHT
					elif check_state ==  directions.EAST:
						self.grid[(r * 2 + 1, c+1)] = designs.RIGHT
						self.grid[((r + 1) * 2, c+1)] = designs.RIGHT
					elif check_state == directions.NONE:
						self.grid[(r * 2 + 1, c+1)] = designs.EMPTY
						self.grid[((r + 1) * 2, c+1)] = designs.EMPTY
				else:
					if neighbours == directions.U or neighbours == directions.B:
						if check_state == directions.SOUTH_AND_EAST or check_state == directions.EAST:
							self.grid[(r * 2 + 1, c+1)] = designs.C_RIGHT
						else:
							self.grid[(r * 2 + 1, c+1)] = designs.C_EMPTY
					elif neighbours == directions.L or neighbours == directions.LB:
						if check_state == directions.SOUTH_AND_EAST or check_state == directions.EAST:
							self.grid[(r * 2 + 1, c+1)] = designs.CL_TOP_RIGHT
						else:
							self.grid[(r * 2 + 1, c+1)] = designs.CL_EMPTY
					elif neighbours == directions.R or neighbours == directions.BR:
						if check_state == directions.SOUTH_O or check_state == directions.NONE:
							self.grid[(r * 2 + 1, c+1)] = designs.CR_EMPTY
					else:
						self.grid[(r * 2 + 1, c+1)] = designs.CLR_EMPTY


					if neighbours == directions.B or neighbours == directions.LB or neighbours == directions.BR:
						if check_state == directions.EAST:
							self.grid[((r + 1) * 2, c+1)] = designs.C_RIGHT
						else:
							self.grid[((r + 1) * 2, c+1)] = designs.C_EMPTY
					else:
						if check_state == directions.SOUTH_AND_EAST:
							self.grid[((r + 1) * 2, c+1)] = designs.BOTTOM_RIGHT
						elif check_state == directions.EAST:
							self.grid[((r + 1) * 2, c+1)] = designs.RIGHT
						elif check_state == directions.NONE:
							self.grid[((r + 1) * 2, c+1)] = designs.EMPTY
						else:
							self.grid[((r + 1) * 2, c+1)] = designs.BOTTOM_NO_RIGHT

		
		final_string = ""
		for r in range(0, self.rows * 2 + 1):
			row_string = ""
			for c in range(0, self.cols + 1):
				row_string += self.grid[(r, c)]
			final_string += row_string + "\n"
		return final_string



	def checkState(self, cell):
			
		if not cell.visited:
			neighbours = False
		else:
			[w, e, s, n] = [directions.WEST, directions.EAST, directions.SOUTH, directions.NORTH]
			
			if self.contained(cell, w) and not cell.w_wall and self.maze.grid[(cell.row + w[0], cell.col + w[1])].visited:
				if self.contained(cell, e) and not cell.e_wall and self.maze.grid[(cell.row + e[0], cell.col + e[1])].visited:
					neighbours = directions.LR
				elif self.contained(cell, s) and not cell.s_wall and self.maze.grid[(cell.row + s[0], cell.col + s[1])].visited:
					neighbours = directions.LB
				else:
					neighbours = directions.L
			elif self.contained(cell, e) and not cell.e_wall and self.maze.grid[(cell.row + e[0], cell.col + e[1])].visited:
				if self.contained(cell, s) and not cell.s_wall and self.maze.grid[(cell.row + s[0], cell.col + s[1])].visited:
					neighbours = directions.BR
				else:
					neighbours = directions.R
			elif self.contained(cell, s) and not cell.s_wall and self.maze.grid[(cell.row + s[0], cell.col + s[1])].visited:
				neighbours = directions.B
			else:
				neighbours = directions.U

			if cell == self.maze.start:
				if neighbours == directions.R:
					neighbours = directions.LR
				elif neighbours == directions.B:
					neighbours = directions.LB
				elif neighbours == directions.U:
					neighbours = directions.L
			elif cell == self.maze.end:
				if self.over:
					if neighbours == directions.L:
						neighbours = directions.LR
					else:
						neighbours = directions.R



		if cell.row == self.rows-1:
			if cell.e_wall:
				check_state = directions.SOUTH_AND_EAST
			else:
				check_state = directions.SOUTH_O
		elif cell.col == self.cols-1:
			if cell.s_wall:
				check_state = directions.SOUTH_AND_EAST
			else:
				check_state = directions.EAST
		else:
			if cell.e_wall and cell.s_wall:
				check_state = directions.SOUTH_AND_EAST
			elif cell.e_wall:
				check_state = directions.EAST
			elif cell.s_wall:
				check_state = directions.SOUTH_O
			else:
				check_state = directions.NONE

		return neighbours, check_state



	def analyse(self, move):
		if move.lower() in ['w', 'a', 's', 'd']:
			if move.lower() == 'w':
				if self.current.n_wall:
					return False
				direction = directions.NORTH
			elif move.lower() == 'a':
				if self.current.w_wall:
					return False
				direction = directions.WEST
			elif move.lower() == 's':
				if self.current.s_wall:
					return False
				direction = directions.SOUTH
			else:
				if self.current.e_wall:
					return False
				direction = directions.EAST

			target_row, target_col = self.current.row + direction[0], self.current.col + direction[1]

			if target_row >= 0 and target_row < self.rows and target_col >= 0 and target_col < self.cols:
				target = self.maze.grid[(target_row, target_col)]
				target.visited = True
				self.current = target

			if self.current == self.maze.end:
				self.over = True

		else:
			return False

	def contained(self, cell, d):
		if 0 <= (cell.row + d[0]) < self.rows and 0 <= (cell.col + d[1]) < self.cols:
			return True
		else:
			return False






