import torch.nn as nn


class FlowModel(nn.Module):
    def __init__(self, num_hid: int):
        super().__init__()
        self.mlp_move = nn.Sequential(
            nn.Linear(
                64, num_hid
            ),  # Input state is a one hot vector representing the position of the pieces on the board
            nn.LeakyReLU(),
            nn.Linear(
                num_hid, 8
            ),  # Output 8 numbers for the 8 directions (child states).
        )

        # self.mlp_dist = nn.Sequential(
        #     nn.Linear(
        #         64, num_hid
        #     ),  # Input state is a one hot vector representing the position of the piece
        #     # presence and/or absence.
        #     nn.LeakyReLU(),
        #     nn.Linear(
        #         num_hid, 8
        #     ),  # Output 8 numbers for the 8 directions (child states).
        # )

    def forward(
        self,
        x,
    ):
        """
        Computes the flow
        """
        # Flows must be positive, so we take the exponential.

        # if state.move_or_distance.name == "DISTANCE":
        #     return self.mlp_dist(x).exp()
        # if state.move_or_distance.name == "MOVE":
        return self.mlp_move(x).exp()
