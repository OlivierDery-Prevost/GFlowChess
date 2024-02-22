from typing import Callable, List, Tuple

import chess
import numpy as np
from chess import Board, Move
from gflownet.envs.base import GFlowNetEnv

# Ressource: Starting at 5:25:00, live coding demonstration:
# https://www.youtube.com/watch?v=tMVJnzFqa6w&ab_channel=Mila-QuebecArtificialIntelligenceInstitute

# Actions: Actions are representd as a single tuple, containing
# the index of the action.


class GFlowChessEnv(GFlowNetEnv):
    """
    Since most common functionality is implemented by the base
    GFlowNetEnv, the only methods that a new discrete environment must
    implement are:

    - __init__(): defines attributes, EOS action, source state, etc.
    - get_action_space(): constructs the list of possible actions
      (tuples).
    - step(action): given an action, update the environment's state.
    - get_parents(state): obtains the list of parents of a given
      state, and their corresponding actions.
    - get_mask_invalid_actions_forward(state): determines the invalid
      actions from a given state.
    - State conversions: states2proxy(), states2policy(),
      state2readable(), readable2state().
    """

    # DONE
    def __init__(self, next_play_func: Callable[[Board], Board], move2action: Callable[[Move], Tuple[int]]):
        """
        Instantiate a new GFlowChess environment.

        Parameters
        ----------

        next_play: Callable[[Board], Board]
            This function will be used to generate the next play of the model's
            opponent and returns the updated board. Typically, this would be a
            function for calling the next move from stockfish and returning the
            corresponding board.

        move2action: Callable,
            This function is used to convert a move from python-chess into an
            action.
        """
        self.board = chess.Board()  # Current state of the game
        self.state: List[Tuple[int]] = []  # NOTE: This is a sequence of actions.
        self.move2action = (
            move2action  # TODO: This function should be a part of the environment, not an external function
        )
        self.next_play_func = next_play_func

    # TODO
    def get_action_space(self) -> List[Tuple]:
        """
        Constructs list with all possible actions (excluding end of
        sequence).
        """
        # All the legal actions:
        assert isinstance(self.board, Board)
        return list(self.board.legal_moves)

    # TODO
    def step(
        self, action: Tuple[int], skip_mask_check: bool = False
    ) -> Tuple[List[int], Tuple[int], bool]:
        """
        Executes step given an action.

        Args
        ----
        action : tuple
            Action from the action space.

        skip_mask_check : bool
            If True, skip computing forward mask of invalid actions to check if the
            action is valid.

        Returns
        -------
        self.state : list
            The sequence after executing the action

        action : int
            Action index

        valid : bool
            False, if the action is not allowed for the current state, e.g. stop at the
            root state
        """
        # From the action

        do_step, self.state, action = self._pre_step(action, skip_mask_check)
        if not do_step:
            return self.state, action, False
        valid = True
        self.n_actions += 1
        if self.board.gives_check(action):  # Verifies if this action ends the game
            self.done = True
            return self.state, action, valid
        # Update the state
        else:
            
        return [None, None, None]

    # TODO
    def get_parents(state):
        """
        Obtains the list of parents of a given state, and their correcponding actions
        """
        pass

    # TODO
    def get_mask_invalid_actions_forward(self, state):
        """
        Determines the invalid actions from a given state
        """
        pass

    # TODO
    def states2proxy():
        pass

    # TODO
    def states2policy():
        pass

    # TODO
    def states2readable():
        pass

    # TODO
    def readables2state():
        pass
