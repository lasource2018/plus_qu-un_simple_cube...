
from tkinter import *

from tkinter import font



class GameOfLife(Frame):



	def __init__(self, parent):

		self.size_y = 28

		self.cell_buttons = []

		self.generate_next = True


		self.initialUI()



	def initialUI(self):	

		self.parent.title("Game of Life")


		# frame for title and line of instruction

		self.title_frame = Frame(self.parent)

		self.title_frame.grid(row = 0, column = 0, columnspan = 4)



		self.titleFont = font.Font(family="Helvetica", size=14)

		title = Label(self.title_frame, text = "Conway's Game of Life", font = self.titleFont)

		title.pack(side = TOP)

		# tableau de boutons pour la config

		self.build_grid()

		# bouton pour lancer le jeu

		self.start_button = Button(self.parent, text = "Start Game", command = self.simulate_game)

		self.start_button.grid(row = 1, column = 1, sticky = E)



		self.reset_button = Button(self.parent, text = "Reset", state = DISABLED, command = self.reset_game)

		self.reset_button.grid(row =1 , column = 2, sticky = W)



	def build_grid(self):

		# limites du tableau de boutons

		self.game_frame = Frame(

			self.parent, width = self.size_x + 2, height = self.size_y + 2, borderwidth = 1, relief = SUNKEN)

		self.game_frame.grid(row = 2, column = 0, columnspan = 4)



		#boutons pour choisir la config de base

		self.cell_buttons = [[Button(self.game_frame, bg = "white", width = 2, height = 1) for i in range(self.size_x + 2)] for j in range(self.size_y + 2)]

		# 2d tableau de bouton 

		for i in range(1, self.size_y + 1):

			for j in range(1, self.size_x + 1):	

				self.cell_buttons[i][j].grid(row = i, column = j, sticky = W+E)

				self.cell_buttons[i][j]['command'] = lambda i=i, j=j:self.cell_toggle(self.cell_buttons[i][j])



	def simulate_game(self):

		self.disable_buttons()

		# la liste des boutons dont on peut changer l'etat et va sez stocker dans ma class l'etat de la cellule
		buttons_to_toggle = []

		for i in range(1, self.size_y + 1):

			for j in range(1, self.size_x + 1):

				coord = (i, j)

				# if cell dead and has 3 neighbors, add coordinate to list of coords to toggle

				if self.cell_buttons[i][j]['bg'] == "white" and self.neighbor_count(i, j) == 3:

					buttons_to_toggle.append(coord)

				# if cell alive and does not have 2 or 3 neighbors,, add coordinate to list of coords to toggle

				elif self.cell_buttons[i][j]['bg'] == "black" and self.neighbor_count(i, j) != 3 and self.neighbor_count(i, j) != 2:

					buttons_to_toggle.append(coord)

		# mets a jour l'erat des cellules

		for coord in buttons_to_toggle:

			self.cell_toggle(self.cell_buttons[coord[0]][coord[1]])			

		if self.generate_next:

			self.after(100, self.simulate_game)
		else:
			self.enable_buttons()

			
	def disable_buttons(self):

		if self.cell_buttons[1][1] != DISABLED:

			for i in range(0, self.size_y + 2):

				for j in range(0, self.size_x + 2):

					self.cell_buttons[i][j].configure(state = DISABLED)


			self.reset_button.configure(state = NORMAL)

			self.start_button.configure(state = DISABLED)



	def enable_buttons(self):
	    # bouton de reset
		for i in range(0, self.size_y + 2):

			for j in range(0, self.size_x + 2):

				self.cell_buttons[i][j]['bg'] = "white"

				self.cell_buttons[i][j].configure(state = NORMAL)

		self.reset_button.configure(state = DISABLED)

		self.start_button.configure(state = NORMAL)

		self.generate_next = True

	def neighbor_count(self, x_coord, y_coord):

		count = 0

		for i in range(x_coord - 1, x_coord + 2):

			for j in range(y_coord - 1, y_coord + 2):

				if (i != x_coord or j != y_coord) and self.cell_buttons[i][j]['bg'] == "black":

					count += 1

		return count

	
	def cell_toggle(self, cell):

		if cell['bg'] == "white":

			cell['bg'] = "black"
		else:
			cell['bg'] = "white"


	def reset_game(self):

		self.generate_next = False



if __name__ == '__main__':  #permet d'utiliser un module comme script sans avoir a l'importer dans la console

	root = Tk()  #ouvre le fenetre principalede tkinter

	game = GameOfLife(root) #lance la fonction class

	root.mainloop()  #mets fin excution programme
