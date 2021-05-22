from random import shuffle
from typing import List

from utils.player import Player
from utils.card import Card


class Deck:
    """
    """
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def __str__(self) -> str:
        return f'Deck has {len(self.cards)} cards'

    def fill_deck(self) -> None:
        """
        fill cards with a complete card game (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠]). 
        Your deck should contain 52 cards at the end.
        """
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        symbols = ['♥', '♦', '♣', '♠']
        for i in symbols:
            for j in values:
                self.cards.append(Card(j, i))

    def shuffle(self) -> None:
        """
        shuffle all the list of cards
        """
        shuffle(self.cards)

    def distribute(self, players: List[Player]) -> List[Player]:
        """
        take a list of Player as parameter and will distribute the cards evenly between all the players.
        """
        while len(self.cards) >= len(players):
            for player in players:
                player.add_card(self.cards.pop())
        if len(self.cards) > 0:
            print(f'{len(self.cards)} card could not be distributed') 
            print([card.__str__() for card in self.cards])
        return players


class Board:
    def __init__(self) -> None:
        self.players: List[Player] = []
        self.turn_count: int = 0
        self.active_cards: List[Card] = []
        self.history_cards: List[Card] = []

    def __str__(self) -> str:
        return f'{len(self.players)} players are playing for {self.turn_count} turns'

    def start_game(self) -> None:
        """
        Start the game,
        Fill a Deck,
        Distribute the cards of the Deck to the players.
        Make each Player play() a Card , where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.
        At the end of each turn, print:
        The turn count.
        The list of active cards.
        The number of cards in the history_cards.
        """
        # Start board & player setup
        name = ' '
        names = []
        while name or len(names) < 2:
            name = input('Write player name (ENTER when done): ')
            if name and name not in names:
                names.append(name)
                self.players.append(Player(name))
        # Shuffle players
        shuffle(self.players)
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        self.players = deck.distribute(self.players)

        # Start game loop
        nb_cards_in_hands = 52
        while nb_cards_in_hands > 0:
            print(nb_cards_in_hands)
            nb_cards_in_hands = 0
            for player in self.players:
                # If one turn has passed (cards in self.active_cards), put old cards to graveyard
                if self.turn_count > 0:
                    self.history_cards.append(self.active_cards.pop(0))
                # Check if user has still cards left. If true, play one
                if player.number_of_cards > 0:
                    self.active_cards.append(player.play())
                nb_cards_in_hands += player.number_of_cards
            self.turn_count += 1
            active_cards_str = [card.__str__() for card in self.active_cards]
            print(f'Turn: {self.turn_count}\n\
Cards on board: {active_cards_str}\n\
Graveyard: {len(self.history_cards)}')
