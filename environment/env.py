from gflownet.envs.base import GFlowNetEnv
from typing import Tuple, List
import chess


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

    # TODO
    def __init__(self):
        self.board = chess.Board()
        self.state = self.board

    # TODO
    def get_action_space(self) -> List[chess.Move]:
        """
        Constructs list with all possible actions (excluding end of
        sequence).
        """
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
        _, self.state, action = self._pre_step(action, skip_mask_check)
        return [None, None, None]

    # TODO
    def get_parents(state):
        """
        Obtains the list of parents of a given state, and their correcponding actions
        """
        pass

    # TODO
    def get_mask_invalida_actions_forward(state):
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
