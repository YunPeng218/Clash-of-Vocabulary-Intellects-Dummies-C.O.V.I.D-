# Clash-of-Vocabulary-Intellects-Dummies-C.O.V.I.D-
Welcome to Clash of Vocabulary Intellects Dummies (C.O.V.I.D), a simple English quote puzzle game!
# Description
This Python program presents players with a fun and challenging game where they are tasked with solving puzzles based on English quotes. The game randomly selects quotes from a provided list and presents them as puzzles to the players. Players must decipher the quotes by filling in the missing words or phrases, testing their vocabulary, intellect, and wit.

General descriptions about the game
1) COVID is a 3-player turn-based game in which players solve quote puzzles to win money.
2) Each game has a blank quote puzzle, with each blank representing an alphabet in the quote. Punctuation is revealed as needed.
3) The goal of the game is to earn money while solving the puzzle. The player who earns the most is declared the winner.
4) The players are allowed to perform three operations during the game: solve the puzzle, buy a vowel, and guess a consonant. They earn money by solving the puzzle and guessing consonants correctly, while they spend money by buying vowels.
5) To solve the puzzle, the player needs to enter his solution. If his solution is correct, the quote is revealed, the player’s money is doubled, and the winner is declared before the game ends. Otherwise, the player loses his turn to other players.
6) To buy a vowel, the player needs to enter the vowel to buy. If the vowel exists, all existences of the vowel in the quote are revealed, provided that the player has sufficient money to buy. In the case where the player has insufficient money, the player still maintains his turn and can play. However, if the vowel does not exist, the player loses his turn to other players. Each vowel costs RM200.
7) To guess a consonant, the player needs to enter the consonant to guess. Then, a dice is rolled to determine the prize per consonant the player would get if his guess is correct. If the consonant exists, all existences of the consonant in the quote are revealed, and the player earns prizes based on the rolled prize and the number of such consonants in the quote. If the consonant does not exist, the player loses his turn to other players. This is the only operation where dice is rolled.
8) Note that the dice is an octahedron (i.e. a 3D shape with 8 faces) and therefore has 8 values: RM500, RM 600, RM 700, RM 800, RM 900, RM1000, Bankrupt, and Lose A Turn. Both “Bankrupt” and “Lose A Turn” forfeit the player’s turn, with Bankrupt also eliminating the money the player has earned so far.
9) The player gets to maintain his turn (i.e. perform any operations any number of times) unless he gets into any situations mentioned in item (5) to (11) that causes him to lose his turn.
10) The game ends when the puzzle is completely solved by any player.
# Files
1. quotes.txt: This file contains a list of English quotes from which the game will choose. Each line contains a single quote. You can modify this file by adding new quotes or removing existing ones to customize the game experience.

2. psphelper.py: This Python source code contains helpful functions that facilitate the gameplay. These functions are utilized within the main program (covid.py).

3. covid.py: This serves as the main Python source code for the program. It also demonstrates the utilization of the functions provided in psphelper.py to create an interactive quote puzzle game.
# Usage
To play the game, run covid.py. The program will prompt players to solve puzzles based on quotes extracted from quotes.txt. Players can interact with the game, filling in missing words or phrases to complete the quotes. 
# Program Logic