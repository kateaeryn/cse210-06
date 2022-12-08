from game.terminal_service import TerminalService 
from game.guess import Guess


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: (class): For getting and displaying information on the terminal.
        guess: (string): For storing user input
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._guess = Guess()
        self._input = ""
        self._response = ""
        self._update = ""
        self._score = 0
        self._comp_score = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Rock, Paper, Scissors. You vs. Me, Let's go!")
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_scoring()

    def _get_inputs(self):
        """Gets the guess from the User.

        Args:
            self (Director): An instance of Director.
        """
        self._input = self._terminal_service.read_guess(
            "\nRock, Paper, or Scissors?:")
        print()
        self._input = self._guess.input(self._input)
        self._response = self._guess.response()

    def _do_updates(self):
        
        
        input = self._input
        response = self._response
        self._update = self._guess.check_guess(self._input)
        self._terminal_service.write_text(f"You chose: {input}. I chose: {response}.")
        self._terminal_service.write_text(self._update)

    def _do_scoring(self):

        if self._update == ("You Win!"):
            self._score += 1
        if self._update == ("I Win!"):
            self._comp_score += 1
        else:
            self._score + 0
            self._comp_score + 0

        if self._score == 3:
            self._is_playing = False
            self._terminal_service.write_text("Game Over, You Won!")
        if self._comp_score == 3:
            self._is_playing == False
            self._terminal_service.write_text("Game Over, I Won!")