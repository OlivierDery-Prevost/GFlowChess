# Notes and questions

## Context
We are implementing GFlowNet with the help of python's chess library and the
chess engine _stockfish_. The chess library is capapble of generating every
_legal_ moves and keeps the game's board updated (the state), while the
_stockfish_ engine is capapble of giving a score to the moves.  But none of
those libraries have an obvious way of generating every possible action (illegal
and legal).

## GFlowNetEnv

- What is an action in the context of a GFlowNetEnv?
  Is it only the index of the action?

- function `get_action_space(self) -> List[Tuple]`:

  - Does this function returns only legal moves or every moves ?

- function `get_mask_invalid_actions_forward`:

  - Is it really necessary?
  - Could I limit myself to only legal moves (actions)? There are a **lot** of
    possible moves given a board (state).

- Are the following functions necessary?

```python
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
```

## Proxy

- What is a proxy?
- Do we need a proxy?
  - If we do need a proxy, what are the necessary functions to implement it?

## Reward function

Our reward function is based around a chess engine called stockfish. It
evaluates the score of different chess moves. What are the necessary functions
to implement the reward function?

## Other

- Do we need anything else to implement the GFlowNet?

