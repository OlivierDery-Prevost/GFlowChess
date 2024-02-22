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

    def __init__(self):
        """
        Instantiate a new GFlowChess environment.

        Parameters
        ----------

        """
        self.board = chess.Board()  # Current board of the game
        self.select_piece_action = [(i,0) for i in range(16)] # Up to 16 pieces to select
        self.select_move_action = [(0,j) for j in range(64)] # up to 64 different positions on the board

    # DONE
    def get_action_space(self) -> List[Tuple]:
        """
        Constructs list with all possible actions (excluding end of
        sequence) and including illegal actions.
        """
        # *All* the actions:
        assert isinstance(self.board, Board)
        return self.select_piece_action + self.select_move_action

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
