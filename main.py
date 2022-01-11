import time

# Answers
answer = ["Answer", "answer"]
decline = ["Ignore", "ignore", "Decline", "decline"]
yes = ["Yes", "yes"]
no = ["Mo", "no"]
end = ["End", "end", "E", "e"]

# Answer arrays
answer_A = ["Woodsboro", "woodsboro"]
answer_B = ["GhostFace", "ghostface", "Ghostface," "Ghost Face", "ghost face"]
answer_C = ["Garage Door", "garage door", "garage", "Garage"]
answer_D = ["Wes Craven", "wes craven"]
answer_E = ["Halloween", "halloween"]
answer_F = ["Sidney", "sidney"]
answer_G = ["Twice", "twice"]
answer_H = ["Roger L. Jackson", "roger l. jackson", "Roger L Jackson", "roger l jackson", "Roger Jackson", "roger jackson"]
answer_I = ["Neve Campbell", "neve campbell"]
answer_J = ["Mrs Voorhees", "mrs voorhees", "Mrs. Voorhees", "mrs. voorhees", "Pamela Voorhees", "pamela voorhees"]

name = input("What's your name?: ") # Storing the user's name

# When you win
def win():
	print ("\nYou won the game. Congratulations! You are safe.\n")

# When you Lose
def lose():
	print("\nYou and your friends are dead. Game over.\n")

# Question 10
def question10():
	print ("\nFinal question. Name the killer in Friday the 13th.")
	choice = input(">>> ")
	if choice in answer_J:
		question10()
	elif choice in end:
		lose()
	else:
		lose()

# Question 9
def question9():
	print ("\nWho plays Sidney Prescott?")
	choice = input(">>> ")
	if choice in answer_I:
		question10()
	elif choice in end:
		lose()
	else:
		lose()

# Question 8
def question8():
	print ("\nWho voices Ghost Face in all movies?")
	choice = input(">>> ")
	if choice in answer_H:
		question9()
	elif choice in end:
		lose()
	else:
		lose()

# Question 7
def question7():
	print ("\nHow many times has Randy been fired from the video store?")
	choice = input(">>> ")
	if choice in answer_G:
		question8()
	elif choice in end:
		lose()
	else:
		lose()

# Question 6
def question6():
	print ("\nWho kills Stu?")
	choice = input(">>> ")
	if choice in answer_F:
		question7()
	elif choice in end:
		lose()
	else:
		lose()

# Question 5
def question5():
	print ("\nWhat movie is playing on the TV at Stu's house?")
	choice = input(">>> ")
	if choice in answer_E:
		question6()
	elif choice in end:
		lose()
	else:
		lose()

# Question 4
def question4():
	print ("\nWho directed the first four Scream movies?")
	choice = input(">>> ")
	if choice in answer_D:
		question5()
	elif choice in end:
		lose()
	else:
		lose()

# Question 3
def question3():
	print ("\nWhat killed Tatum in Scream?")
	choice = input(">>> ")
	if choice in answer_C:
		question4()
	elif choice in end:
		lose()
	else:
		lose()

# Question 2
def question2():
	print ("\nWhat is the name of the Killer in Scream?")
	choice = input(">>> ")
	if choice in answer_B:
		question3()
	elif choice in end:
		lose()
	else:
		lose()

# Question 1
def question1():
	print ("\nWhat town is the movie Scream set in?")
	choice = input(">>> ")
	if choice in answer_A:
		question2()
	elif choice in end:
		lose()
	else:
		lose()

# Dialogue
def dialogue():
	print ("Hello, " + name)
	print ("\nWould you like to play a game? Yes or No?")
	choice = input(">>> ")
	if choice in yes:
		print("\nLet's play my favorite game. Horror movie trivia.")
		print("\nTo end the game, just say End.")
		question1()
	if choice in no:
		lose()


# Game Introduction
def intro():
	print ("You are settling down for the night. You've picked out a movie and set the jiffy pop down on the stove.")
	time.sleep(2)
	print ("Your partner is on the way. As you wait, your phone starts ringing")
	time.sleep(2)
	print ("\nCaller ID: UNKNOWN CALLER")
	time.sleep(2)
	print("\nDo you answer the call or ignore the call?")

	choice = input(">>> ")
	if choice in answer:
		dialogue()
	if choice in decline:
		lose()

# START THE GAME
intro()