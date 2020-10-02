# Some of the common imports (you can add more here)
import random
import string
# Import from psphelper.py file
import psphelper
#Clear screen
psphelper.clearScreen()
#Read dice.txt
def readDicesFromFile(filename):
	dices = list()
	f = open(filename, "r")
	for line in f:
		dices.append(line.strip())
	f.close()
	return dices

#How to read quotes from "quotes.txt"
quotes = psphelper.readQuotesFromFile("quotes.txt");
dices = ['500', '600', '700', '800', '900', '1000', 'Bankrupt', 'Lose a turn']

#Ramdomly choose a quote from "quotes.txt" and change all letter to underscore
myQuote = random.choice(quotes);
myQuote = myQuote.upper()
quotelist = list(myQuote)
for i in range(len(quotelist)):
	quotelist[i] = psphelper.alphaToUnderscore(quotelist[i])
quoteq = ''.join(quotelist)

# Players' Initial Money And Money Screen
PM_list = [0, 0, 0]

#Input Options
v_list = list('AEIOU')
c_list = list('BCDFGHJKLMNPQRSTVWXYZ')

#Current Player and Input Prompt
P = [1, 2, 3]
done_cheat = []
i = 0
t = 1
#A loop of players taking turns
while i <= 2:
	psphelper.clearScreen()
	t = 1
	x = int(i)
	while t == 1:
		#When players filled the board
		if quoteq == myQuote:
			psphelper.clearScreen()
			print(title.center(width));
			psphelper.showQuoteScreen(quoteq, width);
			print()
			print(f'Player 1: RM {PM_list[0]}')
			print(f'Player 2: RM {PM_list[1]}')
			print(f'Player 3: RM {PM_list[2]}')
			print()
			i = 3
			break
		#Start of the game
		else:
			psphelper.clearScreen()
			#Game Title And Quote Screen
			title = "..:: C.O.V.I.D ::..";
			width = 30
			print(title.center(width));
			psphelper.showQuoteScreen(quoteq, width);
			print()
			print(f'Player 1: RM {PM_list[0]}')
			print(f'Player 2: RM {PM_list[1]}')
			print(f'Player 3: RM {PM_list[2]}')
			print()
			print('Input Options:')
			print('   /           :- Solve the puzzle')
			print('   a vowel     :- Buy a vowel')
			print('   a consonant :- Guess a consonant')
			print()
			print(f'Player {P[x]}')
			print('========')
			while True:
				ipt = input('Input > ').upper()
				money = ipt[6:]
				if ipt in v_list or ipt in c_list or ipt == '/' or ipt == 'CHEAT' or (len(ipt) > 6 and ipt[0:6] == 'CHEAT ' and money.isdigit()):
					break
				else:
					print ('Invalid Input.')
			#Player wants to cheat
			if ipt == 'CHEAT':
				m = 0
				a = []
				w = []
				for i in range(len(myQuote)):
					if quoteq[i] == '_':
						if myQuote[i] in c_list:
							a.append(myQuote[i])
				#Player cheated before
				if x in done_cheat:
					print('No more cheat available.')
					enter = input('Press ENTER to continue play.')
					i = x
				#No consonants available
				elif len(a) == 0:
					print('Sorry, no more consonants available.')
					enter = input('Press ENTER to continue play.')
					i = x
				#Consonants available and player havent cheated
				else:
					for i in range(len(a)):
						an = a[i]
						if m < a.count(a[i]):
							m = a.count(a[i])
							w[0:] = a[i]
						elif m == a.count(a[i]) and a[i] not in w:
							w.append(a[i])
					done_cheat.append(x)
					chosen_letter = random.choice(w)
					print(f'There are {m} letter {chosen_letter}.')
					enter = input('Press ENTER to continue play.')
					i = x
			#Player cheats money
			elif len(ipt) > 6 and ipt[0:6] == 'CHEAT ':
				money = ipt[6:]
				#Player cheated before
				if x in done_cheat:
					print('No more cheat available.')
					enter = input('Press ENTER to continue play.')
					i = x
				#Player havent cheated
				else:
					PM_list[x] = int(money)
					done_cheat.append(x)
					print(f'Money changed to RM {money}.')
					enter = input('Your turn ends. Press ENTER to end turn.')
					break
			#Solve the question
			elif ipt == '/':
				ans = input('Solve It > ').upper()
				#solved correctly
				if ans == myQuote:
					PM_list[x] = PM_list[x]*2
					quoteq = myQuote
					enter = input('Congratulations! You have solved it. Your money is doubled.')
					psphelper.clearScreen()
					break
				#Solved incorrectly
				else:
					print('WRONG SOLUTION!')
					enter = input('Your turn ends. Press ENTER to end turn.')
					break
			#Input in quote
			elif ipt in myQuote:
				#if input had been answered
				if ipt in quoteq:
					print(f'Letter {ipt} has been taken.')
					enter = input('Press ENTER to continue play.')
					i = x
				#if not answered
				else:
					#input is vowel
					if ipt in v_list:
						count = 0
						tm = 0
						#Calculate money needed to purchase
						for i in range(len(myQuote)):
							if myQuote[i] == ipt:
								count = count + 1
								tm = count*200
						#Enough money
						if PM_list[x] >= tm:
							PM_list[x] -= tm
							for i in range(len(myQuote)):
								if myQuote[i] == ipt:
									quotelist[i] = ipt
							quoteq = ''.join(quotelist)
							print(f'Found {count} letter {ipt}.')
							print(f'You spent RM {tm}.')
							enter = input('Press ENTER to continue play.')
							i = x
						#Not enough money to buy the vowel
						else:
							print('Insufficient money.')
							enter = input('Press ENTER to continue play.')
							i = x
					#Input is consonant
					elif ipt in c_list:
						myDice = random.choice(dices);
						#If rolled money
						if myDice == dices[0] or myDice == dices[1] or myDice == dices[2] or myDice == dices[3] or myDice == dices[4] or myDice == dices[5]:
							myDice = int(myDice)
							count = 0
							tm = 0
							#Calculate money earned
							for i in range(len(myQuote)):
								if myQuote[i] == ipt:
									count = count + 1
									quotelist[i] = ipt
							quoteq = ''.join(quotelist)
							tm = count*myDice
							PM_list[x] += tm
							print(f'You rolled "RM{myDice}".')
							print(f'Found {count} letter {ipt}.')
							print(f'You earned RM {tm}.')
							enter = input('Press ENTER to continue play.')
							i = x
						#If rolled bankrupt
						elif myDice == dices[6]:
							PM_list[x] = 0
							print(f'You rolled "{myDice}".')
							print('Sorry, you lose all your money.')
							enter = input('Your turn ends. Press ENTER to end turn.')
							break
						#If rolled lose turn
						else:
							print(f'You rolled "{myDice}".')
							enter = input('Your turn ends. Press ENTER to end turn.')
							break
			#Input not in quote
			else:
				print(f'Sorry. There is no letter {ipt}.')
				enter = input('Your turn ends. Press ENTER to end turn.')
				break
	#Switch to next player
	if i == 2:
		i = 0
	else:
		i += 1

#Determine the winner
if PM_list[0] > PM_list[1] and PM_list[0] > PM_list[2]:
	print('Player 1 wins.')
	print( )
	print('Game Ends.')
elif PM_list[1] > PM_list[0] and PM_list[1] > PM_list[2]:
	print('Player 2 wins.')
	print( )
	print('Game Ends.')
elif PM_list[2] > PM_list[0] and PM_list[2] > PM_list[1]:
	print('Player 3 wins.')
	print( )
	print('Game Ends.')
elif PM_list[0] == PM_list[1] and PM_list[0] == PM_list[2]:
	print("It's a tie.")
	print( )
	print('Game Ends.')
elif PM_list[1] == PM_list[0]:
	if PM_list[2] > PM_list[1]:
		print('Player 3 wins.')
		print( )
		print('Game Ends.')
	else:
		print("It's a tie.")
		print( )
		print('Game Ends.')
elif PM_list[1] == PM_list[2]:
	if PM_list[0] > PM_list[1]:
		print('Player 1 wins.')
		print( )
		print('Game Ends.')
	else:
		print("It's a tie.")
		print( )
		print('Game Ends.')
elif PM_list[2] == PM_list[0]:
	if PM_list[1] > PM_list[2]:
		print('Player 2 wins.')
		print( )
		print('Game Ends.')
	else:
		print("It's a tie.")
		print( )
		print('Game Ends.')