from app import app
from flask import render_template, request, redirect
from models.game import *

@app.route('/')
def index():
    return render_template('player1.html', title='Rock Paper Scissors')

@app.route('/<choice1>', methods=['POST'])
def on_click1(choice1):
    global player1 
    player1 = Player(request.form['name'], choice1)
    return render_template('player2.html', result1=choice1)

@app.route('/<choice1>/<choice2>', methods=['POST'])
def on_click2(choice1, choice2):
    player2 = Player(request.form['name'], choice2)
    return render_template('winner.html', winner=find_winner(player1,player2), first=player1, second=player2)

