import numpy as np
class RPS_game:
    my_rps = ["R","S","P"]
    my_hand=""
    computer=""
    def __init__(self,computer,me):
        self.my_hand=self.my_rps[np.argmax(me)]
        self.computer=computer
    def match(self):
        result=""
        if self.computer==self.my_hand:
            result="Draw"
        elif self.computer=="R" and self.my_hand=="P":
            result="Win"
        elif self.computer=="S" and self.my_hand=="R":
            result="Win"
        elif self.computer=="P" and self.my_hand=="S":
            result="Win"
        else:
            result="Lose"
        return result