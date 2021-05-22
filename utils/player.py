from random import randint
from typing import List

from utils.card import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.cards: List[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: List[Card] = []

    def __str__(self) -> str:
        return f'{self.name.capitalize()} has {self.number_of_cards} cards left'

    def add_card(self, card: Card) -> None:
        """
        """
        self.cards.append(card)
        self.number_of_cards += 1

    def play(self) -> Card:
        """
        """
        card = self.cards.pop(randint(0, len(self.cards) - 1))
        self.number_of_cards -= 1
        self.history.append(card)
        self.turn_count += 1
        #print(f'{self.name.capitalize()} (turn {self.turn_count}) played: {card.value} {card.icon}')
        return card
