import enum
import random
from termcolor import colored


class Color(enum.Enum):
    Red = "red"
    Blue = "blue"
    Green = "green"
    Yellow = "yellow"


START_NUM = 1
END_NUM = 10


class Card:
    def __init__(self, value, color) -> None:
        self.value = value
        self.color = color

    def __repr__(self) -> str:
        return f"|{colored(self.value, self.color.value)}|"


class Deck:
    def __init__(self, shuffle=True) -> None:
        self.cards = self._create_deck()
        if shuffle:
            random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def _create_deck(self):
        return [
            Card(val, color) for color in Color for val in range(START_NUM, END_NUM + 1)
        ]

    def deal(self, player_count):
        hand_size = len(self) // player_count
        return [self.cards[i : i + hand_size] for i in range(0, len(self), hand_size)]


class Trick:
    def __init__(self, trick_num) -> None:
        self.cards = []
        self.trick_num = trick_num

    def __repr__(self) -> str:
        return f"{[card for card in self.cards]}"

    def add(self, card):
        self.cards.append(card)

    @property
    def score(self):
        return abs(21 - sum([card.value for card in self.cards]))
