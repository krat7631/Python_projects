import random

# Define the Hi-Lo values
hi_lo_values = {
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
    '7': 0, '8': 0, '9': 0,
    '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

def create_deck():
    """Creates a standard 52-card deck (4 suits, 13 values)."""
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def run_simulation(deck_count=1):
    deck = create_deck() * deck_count
    shuffle_deck(deck)
    running_count = 0

    print(f"🃏 Starting card counting simulation with {deck_count} deck(s)\n")

    for i, card in enumerate(deck, 1):
        value = hi_lo_values[card]
        running_count += value
        print(f"Card {i}: {card} → Running Count: {running_count}")

    print(f"\n✅ Final Running Count: {running_count}")

if __name__ == "__main__":
    decks = input("Enter number of decks to simulate: ")
    run_simulation(int(decks) if decks.isdigit() else 1)
