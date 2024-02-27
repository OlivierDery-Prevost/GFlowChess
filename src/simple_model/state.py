from chess import Board
from typing import Optional, List
from enum import Enum


# Example of FEN with black king, white queen and kings:
# 8/8/4k3/8/8/8/2Q5/4K3 w - - 0 1


# class Action(Enum):
#     MOVE = 1
#     DISTANCE = 2


class StateSpace:
    """Class for keeping track of the state of the game"""

    def __init__(
        self,
        fen: Optional[str] = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    ):
        """Initialize the State space.

        Parameters
        ----------
        initial_position: str.
            Initial position on the board. By default, it uses a
            traditional, full board with fen value:
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

        """

        self.board = Board(fen) if fen is not None else Board()  # Board
        # This attributes keeps track of what the next move is: Is it
        # a move (moving a piece) or is the move already decided and
        # we need to select the distance traveled by the piece.
        # self.move_or_distance = (
        #     Action.MOVE
        # )  # In the initial state, the next action should be a move.

        self.mapped = {
            # Map of the EPD representation to number. Minus for
            # blacks, positive for whites and 0 for empty positions.
            "P": 1,  # White Pawn
            "p": -1,  # Black Pawn
            "N": 2,  # White Knight
            "n": -2,  # Black Knight
            "B": 3,  # White Bishop
            "b": -3,  # Black Bishop
            "R": 4,  # White Rook
            "r": -4,  # Black Rook
            "Q": 5,  # White Queen
            "q": -5,  # Black Queen
            "K": 6,  # White King
            "k": -6,  # Black King
            ".": 0,  # Empty position
        }

        self.parent_states = []
        self.parent_actions = []

    def convert_to_list(self):
        """
        Converts the board EPD into a matrix of positions. Returns a list of integer.
        """
        epd_string = self.board.epd()
        list_int = []
        for i in epd_string:
            if i == " ":
                return list_int
            elif i != "/":
                if i in self.mapped:
                    list_int.append(self.mapped[i])
                else:
                    for _ in range(0, int(i)):
                        list_int.append(0)
