# rpsgame.py
A project which was guided by FHNW Windisch-Brugg and [SjF](https://sjf.ch/review-studienwoche-fascinating-informatics-2020/) (Schweizer Jugend forscht)


There are three states "R" = Rock, "P" = Paper, "S" = Scissor

Playing RPS against an AI 

## Dependencies:
- Needs Python 3 (verified to work with Python 3.6)

- Needs pygame

- Needs numpy


**To start a game just execute rpsgame.py**

It also contains a few variables you can change such as:

Setting the size of the window. (In pixels)

      size = (x, y)  
Setting the FPS

      fps = 30

You can also remove pygame.FULLSCREEN at the bottom of the script to execute the game in windowed mode.

Close and open the script to restart a game.

# game.py
game.py uses Markov chains to predict the player's next move. 

It has two classes. A Mc(Markov chain) class and a selector class.

To use game.py you only need to create an object with Selector(number_of_markov_chains=5, focus_length=5)


focus_length is an interger that looks at the past results. It sets the length to look for the past moves 

You first need to import this with:

      import game

For example:

      ai = game.Selector()

To predict the players next move use:

      ai.turn()  #Prediction will be random if you dont update after a player move

update with:

      ai.update(playermove) #Must be one of the states ("R","P" or "S")

      

