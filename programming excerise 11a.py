import random

class Card:
    """Represents a standard playing card."""
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{Card.ranks[self.rank]} of {Card.suits[self.suit]}"

class Deck:
    """Represents a deck of cards."""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

def deal_hand(deck, num_cards):
    """Deals a specified number of cards from the deck."""
    hand = [deck.deal_card() for _ in range(num_cards)]
    return hand

def display_hand(hand):
    """Displays the current hand of cards."""
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card}")

def replace_cards(hand, deck, indices):
    """Replaces selected cards in the hand."""
    for index in sorted(indices, reverse=True):
        hand[index] = deck.deal_card()

def main():
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Deal an initial hand of five cards
    hand = deal_hand(deck, 5)
    print("Your initial hand:")
    display_hand(hand)

    # Prompt user to select cards to replace
    replace_indices = input("Enter the numbers of the cards you want to replace (e.g., 1 3 5): ")
    replace_indices = [int(i) - 1 for i in replace_indices.split()]

    # Replace selected cards
    replace_cards(hand, deck, replace_indices)

    # Display the final hand
    print("Your final hand:")
    display_hand(hand)

if __name__ == "__main__":
    main()
