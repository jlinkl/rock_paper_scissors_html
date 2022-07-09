from models.player import Player
import random

def find_winner(player1, player2):
    if player1.choice == player2.choice:
        return None
    elif player1.choice.lower() == "rock" and player2.choice.lower() == "scissors":
        return player1.name
    elif player1.choice.lower() == "scissors" and player2.choice.lower() == "paper":
        return player1.name
    elif player1.choice.lower() == "paper" and player2.choice.lower() == "rock":
        return player1.name
    else:
        return player2.name

def computer():
    return random.choice(['rock', 'paper', 'scissors'])
