from gflownet.envs.base import GFlowNetEnv
from chess import Board


class GFlowChessEnv(GFlowNetEnv):
    """
    Environment for the GFlowChess.
    """

    def __init__(self):
        self.board = Board()

    def get_action_space(self):
        """
        Constructs list with all possible actions (excluding end of
        sequence)
        """
        pass

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
        return None, None, None
