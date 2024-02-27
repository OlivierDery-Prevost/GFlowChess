"""This module contains the reward function"""


def simple_moves_reward(num_moves: int):
    """
    Returns the reward associated with the number of moves for the simple model.

    Parameters
    ----------
    num_moves: int
        Number of moves completed before ending the sequence. Normally, cannot be
    """
    if num_moves <= 0:
        raise ValueError("num_moves should not be less than 1")
    return 1 / num_moves
