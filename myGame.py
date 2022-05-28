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
            result="draw"
        elif self.computer=="R" and self.my_hand=="P":
            result="win"
        elif self.computer=="S" and self.my_hand=="R":
            result="win"
        elif self.computer=="P" and self.my_hand=="S":
            result="win"
        else:
            result="lose"
        return result