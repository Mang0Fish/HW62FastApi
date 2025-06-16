from card import Card
from card_rank import CardRank
from card_suit import CardSuit
from deck import Deck
from deck_error import DeckCheatingError


def main():
    ace_of_spades = Card(CardSuit.Spades, CardRank.Ace)
    king_of_hearts = Card(CardSuit.Hearts, CardRank.King)

    print(f"First card: {ace_of_spades}")
    print(f"Second card: {king_of_hearts}")

    if ace_of_spades > king_of_hearts:
        print(f"{ace_of_spades} is higher than {king_of_hearts}")

    ace_of_spades.flip()
    print(f"After flipping: {ace_of_spades}")

    deck = Deck()
    print(f"Deck size: {len(deck)}")

    try:
        new_deck = deck.shuffle()
        print("Deck shuffled successfully")
    except DeckCheatingError:
        print("Cheating detected! Deck not shuffled properly!")

    card1 = deck.draw()
    card2 = deck.draw()
    print(f"Drawn cards: {card1}, {card2}")
    print(f"Deck size after drawing: {len(deck)}")

    print("\nAccessing cards directly by index:")
    for i in range(5):
        print(f"Card at index {i}: {deck[i]}")

    print("\nIterating through all cards in the deck:")
    for card in deck:
        print(card)


if __name__ == "__main__":
    main()


