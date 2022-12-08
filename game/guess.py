import random

class Guess:
   
    def __init__(self):
       
        
        self._input = ""
        self._response = ""
        self._update = ""
        

    def input(self, guess):
        self._input = guess.lower()
        return self._input

    def response(self):
        choices = ["rock", "paper", "scissors"]
        self._response = random.choice(choices)
        return self._response

    def check_guess(self, guess):
        
       if self._input == self._response:
            self._update = ("It's a draw!")
       if self._input == "rock" and self._response == "paper": 
            self._update = ("I Win!")
       if self._input == "paper" and self._response == "rock":
            self._update = ("You Win!")
       if self._input == "rock" and self._response == "scissors":
            self._update = ("You Win")
       if self._input == "scissors" and self._response == "rock":
            self._update = ("I Win!")
       if self._input == "scissors" and self._response == "paper":
            self._update = ("You Win!")
       if self._input == "paper" and self._response == "scissors":
            self._update = ("I Win!")   
       if self._input == "scissors" and self._response == "rock":
            self._update = ("I Win!")
       

       return self._update
        