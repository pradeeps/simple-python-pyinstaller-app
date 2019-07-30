class Dealer:
    def __init__(self):
        print("Dealer INIT")
        self.hand = []

    def new_round(self):
        print("Dealter New_round")
        self.hand = ["A", "2"]
        print(self.hand)


class DealerWithEmotion(Dealer):
    def __init__(self, emotion):
        Dealer.__init__(self)

    def cheats(self):
        print("DealterWithEmotion CHEATS")
        self.hand = []
