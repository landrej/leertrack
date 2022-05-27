import random

class montyhall:
	def __init__(self,number_of_doors = 3,chosen_door = 0):
		self.number_of_doors = number_of_doors
		self.doors = self.initialize_doors()
		self.chosen_door = chosen_door

	def initialize_doors(self):
		doors = ['goat' for i in range(self.number_of_doors)] # fill doors with the proverbial goats
		doors[random.randint(0,self.number_of_doors -1)] = 'prize' # pick a door to hide the prize
		return doors

	#def choose_door(self): # lol: de random functie van python is aardig niet random; met slechts 3 deuren is de uitkomst behoorlijk onder de 67% (+/- 5%)
	#	self.chosen_door = random.randint(0,self.number_of_doors)
	#	return self.chosen_door
	
	def reveal_goats(self):
		doors_with_goats = []
		for index,door in enumerate(self.doors):
			if door == "goat" and self.chosen_door != index:
				doors_with_goats.append(index) 
		if len(doors_with_goats) + 1 == self.number_of_doors: # when the player's choice is the door with the prize; not all doors with goats must be opened
			doors_with_goats.pop(random.randint(0,len(doors_with_goats) -1)) # randomly pop one door so there is still one door to switch to for the player
		self.opened_doors = doors_with_goats
		return self.opened_doors

	def switch_door(self): # choose a different closed door
		for i in range(len(self.doors)):
			if i != self.chosen_door and i not in self.opened_doors:
				self.chosen_door = i
				break
		return self.chosen_door

	def jackpot(self):
		if self.doors[self.chosen_door] == 'prize': # jackpot
			self.won_the_game = True
		else:
			self.won_the_game = False
		return self.won_the_game

def run_the_game(number_of_doors,number_of_rounds):
	rounds_won = 0
	for i in range(number_of_rounds):
		game = montyhall(number_of_doors)
		#game.choose_door()
		game.reveal_goats()
		game.switch_door()
		if game.jackpot():
			rounds_won += 1

	return round((rounds_won / number_of_rounds) * 100,2)

print("Percentage of rounds won:", run_the_game(3,100000), "%") # parameters for the game: number of doors, number of round to play