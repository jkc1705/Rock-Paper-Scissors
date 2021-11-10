# Rock Paper Scissors Mastery Problem
print("Welcome to Rock, Paper, Scissors!")

PlayerName1 = str(input("Player1, enter your name: "))
PlayerName2 = str(input("Player2, enter your name: "))

Play1 = str(input(PlayerName1 + ", which of the following do you choose: \nRock\nPaper\nScissors\nEnter: "))
Play2 = str(input(PlayerName2 + ", which of the following do you choose: \nRock\nPaper\nScissors\nEnter: "))

if Play1 == "Rock" and Play2 == "Scissors":
    print("Rock Wins! Congratulations " + PlayerName1)

if Play1 == "Paper" and Play2 == "Rock":
    print("Paper Wins! Congratulations " + PlayerName1)

if Play1 == "Scissors" and Play2 == "Paper":
    print("Scissors Wins! Congratulations " + PlayerName1)

if Play1 == "Scissors" and Play2 == "Rock":
    print("Rock Wins! Congratulations " + PlayerName2)

if Play1 == "Rock" and Play2 == "Paper":
    print("Paper Wins! Congratulations " + PlayerName2)

if Play1 == "Paper" and Play2 == "Scissors":
    print("Scissors Wins! Congratulations " + PlayerName2)

if Play1 == "Paper" and Play2 == "Paper":
    print("Tie! Restart the game and try again!")

if Play1 == "Scissors" and Play2 == "Scissors":
    print("Tie! Restart the game and try again!")

if Play1 == "Rock" and Play2 == "Rock":
    print("Tie! Restart the game and try again!")
    
else:
    print("Error, please try again! This game is sensitive to capitalization and spelling.")
