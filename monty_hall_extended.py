import random

def initialize_doors(number_of_doors):
	i = 0
	doors = []
	while i < number_of_doors:
		doors.append("goat") # fille doors with goats
		i += 1

	prize = random.randint(0,number_of_doors -1) # pick one door for the prize
	doors[prize] = "prize"

	return doors

def reveal_goats(doors):
	doors_with_goats = []

	# list all possible doors with goats
	for index,door in enumerate(doors):
		if door == "goat" and chosen_door != index:
			doors_with_goats.append(index) 
	if len(doors_with_goats) + 1 == number_of_doors:
		pop_door = random.randint(0,len(doors_with_goats) -1) # randomly pop one door so there is still one door (for doors > 3) to switch to
		doors_with_goats.pop(pop_door)
	
	return doors_with_goats

number_of_doors = 10
rounds = 100000
switch_choice = True

current_round = 0
rounds_won = 0

while current_round < rounds:
	chosen_door = 0 # always choose the first door

	doors = initialize_doors(number_of_doors)
	prize_door = doors.index("prize") # door with the prize
	
	opened_doors = reveal_goats(doors) # show doors with goat

	if switch_choice: # when switching doors, percentage rounds won should approximate to this fraction: (doors - 1) / doors 100
		i = 0
		changed_door = False
		while changed_door == False and i < len(doors):
			if i != chosen_door and i not in opened_doors: # choose a different closed door
				changed_door = True
				chosen_door = i
			i += 1
	
	if doors[chosen_door] == "prize": # jackpot!
		rounds_won += 1

	current_round += 1

percentage_won = (rounds_won / current_round) * 100
print("you have won:",round(percentage_won,2),"%")