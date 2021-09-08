class Player:
    def __init__(self, name, hand=[]) -> None:
        self._starting_hand = sorted(
            hand, key=lambda card: (card.color.value, card.value)
        )
        self._remaining_hand = self._starting_hand
        self.name = name

    @property
    def starting_hand(self):
        self._hand

    @starting_hand.setter
    def starting_hand(self, hand):
        self._starting_hand = hand

    def play_turn(self):
        print(f"{self.name}'s turn")
        print(self._remaining_hand)
        card_index = int(input("Choose card: "))
        return self._remaining_hand.pop(card_index)
