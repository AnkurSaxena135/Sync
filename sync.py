from collections import defaultdict
from faker import Faker

from component import Deck, Trick
from player import Player

PLAYER_COUNT = 4
TURNS = 2
fake = Faker()


class SyncGame:
    def __init__(
        self,
    ) -> None:
        self.deck = Deck()
        self.players = self._create_players()
        self.tricks = defaultdict(Trick)

    def _create_players(self):
        deck = self.deck
        return [Player(fake.name(), hand) for hand in deck.deal(PLAYER_COUNT)]

    def _play_trick(self, trick_num):
        trick = Trick(trick_num)

        print(f"Starting trick: {trick_num}")
        for player in self.players:
            trick.add(player.play_turn())
            print(trick)
        print(f"End of trick: {trick_num}. Trick score: {trick.score}")

        self.tricks[trick_num] = trick

    def _print_stats(self):
        print(self.tricks)
        total = sum([t.score for t in self.tricks.values()])
        average = total // TURNS
        print(f"Total: {total}")
        print(f"Average: {average}")

    def play(self):
        for trick_num in range(1, TURNS + 1):
            self._play_trick(trick_num)
        self._print_stats()


if __name__ == "__main__":

    SyncGame().play()
