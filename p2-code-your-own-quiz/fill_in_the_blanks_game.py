# Intro to Programming Nanodegree
# Project 2 - Code Your Own Quiz
# Ricardo Yoshitomi

# All the functions I used in this project I found here https://docs.python.org/2/library/ and here http://stackoverflow.com/

# I imported some modules here that I found useful for this project
import os
import textwrap
import random

global WIDTH, FILL_CHARS, CHARS_TO_FILL
WIDTH = 50
FILL_CHARS = " "
CHARS_TO_FILL = 50

# I could store these strings in a txt file. Maybe it makes the code clearer and organized, but people would see the answers (:
# file = open("string.txt", "r")
# test_string = file.read()

#List with the answers for the easy level
parts_of_string1 = ["double", "name", "works", "concatenation", "math", "characters", "error", "bugs", "assignment", "equals", "five", "writing"]

easy_string1 = """When we want to create a name to refer to a value we can use a variable. 
The way to introduce a variable is using an assignment statement. In the assignment 
statement we have the name of the variable, followed by an equals sign, followed by the 
expression. It is important to note that the equals sign in programming is different from 
math. In math the equals sign refers to equality while in programming it refers to assignment."""

easy_string2 = """Programmers know that it is impossible to avoid making mistakes during writing a 
program. These mistakes, called bugs, are inevitable and it is not worth try to avoid them entirely.
Instead, make a strategy to get rid of them in a systematical way is a better approach. It is about
understand how the system works and then find out what is not working. Debugging is the process of 
finding and fixing the bugs of a program. It is one of the five ways programmers think."""

easy_string3 = """In Python, we can create a string using a sequence of characters between two single
quotes. It is also possible to use double quotes instead. We can use plus with strings as we do with 
numbers, the result is the join of two or more strings, concatenation is the operation of joining 
strings. But, if we want to add a string with a number we get an error."""

easy_list = [easy_string1, easy_string2, easy_string3]

#List with the answers for the medium level
parts_of_string2 = ["none", "test", "boolean", "block", "greater", "called", "decisions", "operator", "inputs", "body", "programming", "compare"]

medium_string1 = """A function is a sequence of program instructions that perform a specific task.
Once coded, it can be called several times and reused in other places. A function is defined with 
the keyword def followed by the function name and the inputs between parentheses. Any number of 
inputs can be placed within the parentheses, but it has to match the number of inputs the function 
expects. A colon (:) must end the line. In the next line, we have the body of the function which 
contains the instructions. A return statement is used to produce the output of the function. 
A return statement can also have no arguments, it is the same as return none."""

medium_string2 = """A comparison operator is used to compare the values of two expressions. Similar to 
arithmetics expressions, an operator can be a less than sign (<), greater than (>), a less than or 
equal (<=), equal (==), not equal (!=) and so on. The output of a comparison is a boolean value, and 
it can be either the value True or the value False."""

medium_string3 = """Conditional statements are features in programming which are used to make decisions. 
Depending on a specific condition, the code performs different actions. The way to do this is using the 
if statement. The structure of an if statement is: the keyword if, followed by a test expression, followed
by a colon. Inside the if we have the block with the code, when the test expression is True the code in the
block will run. If the test expression is not True, then the block does not execute."""

medium_list = [medium_string1, medium_string2, medium_string3]

#List with the answers for the hard level
parts_of_string3 = ["variable", "structure", "panic", "mutation", "solvers", "iterations", "while", "index", "outputs", "elements", "two", "steps"]

hard_string1 = """The most basic data structure in Python is the list. Each element of a list is assigned a 
number (its position or index). The first position is zero, the second is one, the third is two, and so forth.
A string is a kind of data structure, but different from a string which can only store characters a list can
store anything, and it can be characters, numbers and other lists. The second difference between strings and 
lists is that list support mutation. The meaning of mutation is we can change the value of a list after we've
created it."""

hard_string2 = """There are some helpful tips that make we better problem solvers. For a good development of 
a program we must follow these rules. When we confront to a tough problem the first rule is to ask what are 
the inputs?, how the inputs are represented?. The next thing we need to understand is what are the outputs?. 
What all computation problems have in common is they have inputs, relationships between these inputs and 
desired outputs. It is worth to note that there is one rule before the first rule, that's the zeroth rule. 
The zeroth rule is don't panic. If we panic, we will never solve the problem. The third rule is to make sure
we understand the problem by working through some examples by hand. The fourth rule is try to develop a simple
mechanical solution. The simpler it is, the more likely the program will run correctly. Lastly, the final rule
is to develop a solution incrementally in small steps and test as we go."""

hard_string3 = """When we want to loop through all elements of a list, we can use the while-loop or the for-loop.
Unlike the while-loop, the for-loop has an explicit loop counter or loop variable. Each element of a list will be
assigned to the loop variable in the order that these elements appear in the list. For-loops are also used when the
numbers of iterations are specified. For-loops is a simpler way to make loops when the numbers of iterations is known, 
as every for-loop could be written as a while-loop."""

hard_list = [hard_string1, hard_string2, hard_string3]

# Main Program prints the menu option on the screen
user_level = "1"
def main(user_level):
	invalid_option = True
	while invalid_option:
		print WIDTH*"=", "\n", "Welcome to the FILL IN THE BLANKS GAME!".center(WIDTH, FILL_CHARS), "\n", WIDTH*"=", "\n", "Select an option:", "\n", "1. start       2. settings".center(WIDTH, FILL_CHARS)
		user_option = raw_input(">>> Type your option (1 or 2): ")

		if user_option == "1":
			start_game(user_level)

		elif user_option == "2":
			level_selection()

		else:
			os.system('cls')
			print "Sorry, invalid option"
			invalid_option = True

# Plays the game with the list of random strings in game_string
def play_game(game_string, parts_of_string, count_str):

	[replaced, answer] = replace_blank(game_string, parts_of_string, count_str)

	[position, trys] = make_lists(answer)
	# The game will start here
	# The program will check if the input word is equal to its respective element in the list answer
	while len(position) > 0:
		[user_number, user_word] = player_inputs(position)

		if answer[int(user_number) - 1] == user_word:
			replaced = replace_answer(user_number, user_word, replaced)
			position.remove(user_number)

		else:
			trys[int(user_number) - 1] = trys[int(user_number) - 1] - 1
			if trys[int(user_number) - 1] == 0:
				print ""
				return
			trys_left(trys)

		print textwrap.fill(replaced, CHARS_TO_FILL), "\n"

	# Checks if the player completed the three quizzes of each level
	count_str += 1
	level_complete_length = 3
	if count_str == level_complete_length:
		select_option()
		return

	step_selection(game_string, parts_of_string, count_str)
	return

# Starts the game, the function takes into account the selected level
def start_game(user_level):
	os.system('cls')
	print WIDTH*"=", "\n", "Welcome to the FILL IN THE BLANKS GAME!".center(WIDTH, FILL_CHARS), "\n", WIDTH*"=", "\n"
	# Makes a list with random strings based on the chosen level
	list_length = 3
	if user_level == "1":
		string = random.sample(easy_list, list_length)
		parts_of_string = parts_of_string1

	elif user_level == "2":
		string = random.sample(medium_list, list_length)
		parts_of_string = parts_of_string2

	elif user_level == "3":
		string = random.sample(hard_list, list_length)
		parts_of_string = parts_of_string3

	count_str = 0
	play_game(string, parts_of_string, count_str)

	return

# Returns the level chosen by the player
def level_selection():
	os.system('cls')
	print WIDTH*"=", "\n", "Welcome to the FILL IN THE BLANKS GAME!".center(WIDTH, FILL_CHARS), "\n", WIDTH*"="

	invalid_level = True
	while invalid_level:
		print "Please, choose the game level:", "\n", "1. easy    2. medium    3. hard".center(WIDTH, FILL_CHARS), "\n"
		user_level = raw_input(">>> Type your option (1 - 3): ")

		level = ["Easy", "Medium", "Hard"]
		start_pos = 1
		end_pos = len(level) + 1
		num_level = str(range(start_pos, end_pos))
		
		if user_level in num_level:
			print "\n", level[int(user_level) - 1] + " level selected", "\n"
			invalid_level = False
			main(user_level)
		else:
			print "\n", "Sorry, invalid level", "\n"
			invalid_level = True

	return user_level

# Replaces the answers in game_string with the blanks and creates a list with the answers
def replace_blank(game_string, parts_of_string, count_str):
	answer = []
	replaced = []
	game_string0 = game_string[count_str]
	game_string0 = game_string0.split()

	for word in game_string0:
		replacement = word_in_pos(word, parts_of_string)
		if replacement != None:
			if replacement not in answer:
				answer.append(replacement)
			word = word.replace(replacement, "___(" + str(answer.index(replacement) + 1 ) + ")___")
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)

	print "You will have 4 guesses for each gap", "\n"
	print textwrap.fill(replaced, CHARS_TO_FILL), "\n"

	return replaced, answer

# Checks if the word is a substring in parts_of_string
def word_in_pos(word, parts_of_string):
    for pos in parts_of_string:
        if pos in word:
            return pos
    return None

# Creates a list of numbers corresponding to the positions of the answers and creates a list of trys
def make_lists(answer):
	start_pos = 1
	end_pos = len(answer) + 1
	position = range(start_pos, end_pos)
	position = map(str, position)
	trys = [4]*len(answer)

	return position, trys

# The player chooses a blank and inputs a word in user_word
def player_inputs(position):
	user_number = raw_input("Select a number: ")
	while user_number not in position:
		print "Choose another number"
		user_number = raw_input("Select a number: ")

	user_word = raw_input("Type a word: ").lower()

	return user_number, user_word

# Replaces the blanks with the correct answers
def replace_answer(user_number, user_word, replaced):
	print "\n", WIDTH*"-", "\n", "CORRECT ANSWER!!", "\n"
	replacement = "___(" + user_number + ")___"
	replaced = replaced.replace(replacement, user_word)

	return replaced

# Counts the trys left for each blank
def trys_left(trys):
	print "\n", WIDTH*"-", "\n", "THE ANSWER IS NOT CORRECT, PLEASE TRY AGAIN"
	count = 0
	for p in trys:
		count += 1
		print "You have " + str(p) + " trys left for the gap " + str(count)
	print ""

	return

# Player must type 1 to exit the game when the level is finished
def select_option():
	print "\n", WIDTH*"-", "\n", "***CONGRATULATIONS***".center(WIDTH, FILL_CHARS), "\n", "You have completed this level".center(WIDTH, FILL_CHARS), "\n"
	invalid_number = True
	while invalid_number == True:
		exit_option = raw_input(">>> Type number 1 to return to menu: ")

		if exit_option == "1":
			invalid_number = False
			return
		else:
			print "Sorry, invalid number", "\n"
			invalid_number = True
	return

# Chooses the next step when the quiz is finished
def step_selection(game_string, parts_of_string, count_str):
	print "\n", WIDTH*"-", "\n", "CONGRATULATIONS!!!".center(WIDTH, FILL_CHARS), "\n"

	invalid_step = True
	while invalid_step == True:
		print "What is your next step?", "\n", "1. go to the next quiz       2. return to menu".center(WIDTH, FILL_CHARS)
		next_step = raw_input(">>> Type your option (1 or 2): ")
		print ""

		if next_step == "1":
			invalid_step = False
			play_game(game_string, parts_of_string, count_str)

		elif next_step == "2":
			invalid_step = False

		else:
			print "Sorry, invalid step", "\n"
			invalid_step = True

	os.system('cls')
	return


main(user_level)

# Maybe there is a simpler way to write this program
