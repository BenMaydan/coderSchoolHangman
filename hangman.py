import turtle
import time
import sys
import os


class User(object):
	"""
	Occupies the host functions and the guesser functions
	"""

	def __init__(self, secretWord, stage, secretWordMade, allLettersRevealed, lettersChosenWrong):
		self.secretWord = secretWord
		self.stage = stage
		self.secretWordMade = secretWordMade
		self.allLettersRevealed = allLettersRevealed
		self.lettersChosenWrong = lettersChosenWrong


	def menu(self):
		"""
		Populates the terminal with choices for the guesser to make
		"""
		if self.secretWordMade == False:
			print('\n1. Host: Choose Secret Word')
			print('2. Quit Program')
			print('-------------------')
			choice = input('Please make a selection: ')


			if choice == '1':
				if len(self.secretWord) == 0:
					self.makeSecretWord()
				else:
					print('There is already a secret word silly!')
			elif choice == '2':
				sys.exit()
			else:
				print('Unrecognized Input!')
				self.menu()

		else:
			print('\n1. Guesser: Guess A Letter')
			print('2. Quit Program')
			print('-------------------')
			choice = input('Please make a selection: ')

			if choice == '1':
				self.guessLetter()
			elif choice == '2':
				sys.exit()
			else:
				print('Unrecognized Input!')
				self.menu()


	def makeSecretWord(self):
		"""
		Asks the 'host' for a secret word and checks if it is acceptable
		"""
		secretWordInput = input('Secret Word/Sentence: ')
		charactersNotAllowed = '!@#$%^&*()-_=+`~[]}{,.<>/?;:"1234567890\\|' + "'"
		secretWordAcceptable = True

		for character in secretWordInput:
			if character in charactersNotAllowed:
				secretWordAcceptable = False
				break
			else:
				pass

		if secretWordAcceptable:
			if len(secretWordInput) == 0 or len(secretWordInput) > 42:
				print('Either too long or not long enough!\n')
				self.makeSecretWord()
			else:
				self.secretWordMade = True
				self.newSecretWord = ''
				self.secretWord = secretWordInput
				os.system('clear')
				turtle.printDashes()
				self.menu()
		else:
			print('Not An Acceptable Secret Word!\n')
			self.makeSecretWord()


	def guessLetter(self):
		"""
		Allows the guesser to guess a letter
		"""
		letterGuessed = input('Guess A Letter: ')

		if len(letterGuessed) > 1:
			print('That is multiple letters!')
			self.guessLetter()

		else:
			if letterGuessed in self.secretWord:
				print("Yay! The character '" + letterGuessed + "' is in the secret word!")

				if self.allLettersRevealed == True:
					os.system('clear')
					print('Congratulations Guesser! You Won The Game!')
					sys.exit()
				else:
					turtle.printLetter(letterGuessed)
					self.menu()

			else:
				print("The character '" + letterGuessed + "' is not in the secret word")
				self.lettersChosenWrong += letterGuessed

				if self.stage <= 3:
					turtle.drawHangman()
					turtle.printLettersChosenWrong()
					self.menu()
				elif self.stage == 4:
					os.system('clear')
					print('Congratulations Host! You Won The Game!')
					sys.exit()
				else:
					self.menu()



class Turtle(object):
	"""
	Hosts all the methods for the turtle
	Mainly drawing and the goTo method
	"""


	def printDashes(self):
		"""
		When the word is made from host
		This should print appropriate number of dashes and underscores
		That is drawn from the length of the word chosen
		"""
		dashesUnderscoresPrint = ''
		characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

		for letter in user.secretWord:
			if letter in characters:
				dashesUnderscoresPrint += '_'
			else:
				dashesUnderscoresPrint += '-'


		print(dashesUnderscoresPrint)
		self.goTo(0, -100, 0)
		drawer.write(dashesUnderscoresPrint, align='center', font=("Arial", 30, "normal"))


	def printLetter(self, letter):
		"""
		'Reveals' the letter/s the guesser guessed
		"""
		wordToPrint = ''

		for character in user.secretWord:
			if letter == character:
				wordToPrint += letter
			elif letter == ' ':
				wordToPrint += '-'
			else:
				wordToPrint += '_'

		self.goTo(0, -100, 0)
		drawer.write(wordToPrint, align='center', font=("Arial", 30, "normal"))


	def printLettersChosenWrong(self):
		"""
		This function prints the letters to the turtle screen that the guesser chose wrong
		"""
		wordToPrint = ''
		addDash = False
		lettersToPrint = user.lettersChosenWrong
		abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

		for letter in lettersToPrint:
			if addDash:
				wordToPrint += letter
				addDash = False
			else:
				wordToPrint += letter
				addDash = True

		self.goTo(-100, -150, 0)
		drawer.write(wordToPrint, font=("Arial", 25, "normal"))


	def goTo(self, x, y, p):
		"""
		Goes to coordinates on the turtle screen without drawing while moving to coordinates specified
		"""
		drawer.hideturtle()
		drawer.penup()
		drawer.goto(x,y)
		drawer.setheading(p)
		drawer.pendown()


	def drawHangman(self):
		"""
		Draws the hangman's based on stages
		"""
		drawer.speed(0)

		if user.stage == 0:
			self.goTo(-300,0,0)
			drawer.forward(600)
			self.goTo(-100,0, 90)
			drawer.forward(200)
			drawer.right(90)
			drawer.forward(100)
			drawer.right(90)
			drawer.forward(25)
		elif user.stage == 1:
			self.goTo(0, 150, 0)
			drawer.circle(12.5)
		elif user.stage == 2:
			self.goTo(0,150, -90)
			drawer.forward(50)
		elif user.stage == 3:
			self.goTo(0,140, -45)
			drawer.forward(25)
			self.goTo(0,140, -135)
			drawer.forward(25)
		elif user.stage == 4:
			self.goTo(0,100, -45)
			drawer.forward(25)
			self.goTo(0,100, -135)
			drawer.forward(25)
		user.stage += 1



drawer = turtle.Turtle()
turtle = Turtle()
user = User('', 0, False, False, '')
user.menu()

