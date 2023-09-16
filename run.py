import random

class Card:
    """

    """
    def __init__(self, symbol, value, logo):
        self.symbol = symbol
        self.value = value       
        self.logo = logo

    def __str__(self):
        return f"Card: {self.symbol} {self.value} {self.logo}"

class Deck:
    """

    """
    def __init__(self):
        """

        """
        self.cards = []
        # Creating Card Objects and appending them to Cards List
        for symbol in ["Hearts","Diamonds","Clubs","Spades"]:
            for value in range(2, 11):
                self.cards.append(Card(symbol, value, str(value)))

            for logo in ["Jack","Queen","King"]:
                self.cards.append(Card(symbol, 10, logo))

            self.cards.append(Card(symbol, 11, "Ace"))

    def print_cards(self):
        """

        """
        print(len(self.cards))
        for card in self.cards:
            print(f"Symbol: {card.symbol} Logo: {card.logo}")

    def shuffle(self):
        """

        """
        random.shuffle(self.cards)

    def draw_card(self):
        """

        """
        if len(self.cards)>0:
            return self.cards.pop()
        else:
            print("The deck is empty")

class Participant:
    """

    """
    def __init__(self, name):
        """
        """
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        """

        """
        self.hand.append(card)

    def show_hand(self):
        """

        """
        print(f"{self.name}'s hand: ")
        for card in self.hand:
            print(card)
    
    def hand_value(self):
        """

        """
        hand_value = sum(card.value for card in self.hand)

        ### Aces will get treated as 1 while: ###
        num_aces = sum(1 for card in self.hand if card.value == 11)       
        while hand_value > 21 and num_aces:
            hand_value -= 10
            num_aces -= 1

        return hand_value

class Player(Participant):
    pass

class Dealer(Participant):
    def show_hand(self, first_card_secret = True):
        """

        """
        print(f"{self.name}'s hand: ")
        if first_card_secret == True:
            print("   Hidden Card")
            for card in self.hand[1:]:
                print(card)
        else:
            super().show_hand()

def main():
    """
    ### Test Deck and Card
    deck = Deck()
    print(deck.print_cards())
    print(deck.shuffle())
    print(deck.print_cards())
    print(deck.draw_card().__str__())
    print(deck.draw_card().__str__())
    print("End test Deck,Card and functions\n")

    ### Test Participant
    participant = Participant("Oscar")
    participant.add_card_to_hand(deck.draw_card())
    participant.add_card_to_hand(deck.draw_card())
    print("expected output = participant name and cards value")
    participant.show_hand()
    print(participant.hand_value())
    print("End test Participant Class and functions\n")

    ### Test Player
    player = Player("Henry")
    player.add_card_to_hand(deck.draw_card())
    player.add_card_to_hand(deck.draw_card())
    print("expected output = player name and cards value")
    player.show_hand()
    print(player.hand_value())
    print("End test Player Class and functions\n")

    ### Test Dealer
    dealer = Dealer("Del Pierro")
    dealer.add_card_to_hand(deck.draw_card())
    dealer.add_card_to_hand(deck.draw_card())
    print("expected output = player name and cards value but first card hidden")
    dealer.show_hand()
    print(dealer.hand_value())
    print("End test Dealer Class and functions\n")
    """

    ### Test Game

    deck_one = Deck()
    deck.shuffle()

    player = Player("Ronaldo")
    dealer = Dealer("Bestdealer")

    # every player gets two cards
    for _ in range(2)
        player.add_card_to_hand(deck.draw_card())
        dealer.add_card_to_hand(deck.draw_card())

    # showing starting hands
    player.show_hand()
    dealer.show_hand()

    # Player draws card
    

    
    

main()

