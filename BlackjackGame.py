import random

def create_deck():
    """Creates a standard deck of 52 cards with their values."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank + " of " + suit, values[rank]))
    return deck

def calculate_hand_value(hand):
    """Calculates the total value of the hand and adjusts for Aces."""
    value = sum(card[1] for card in hand)
    aces = sum(1 for card in hand if card[0].startswith('Ace'))
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(player, hand):
    """Displays the cards in player's hand."""
    print(f"{player}'s hand: {[card[0] for card in hand]}")

def blackjack_game():
    """Runs a single game of Blackjack."""
    print('\nWelcome to Blackjack!')

    # Create and shuffle the deck
    deck = create_deck()
    random.shuffle(deck)

    # Deal two cards each to the player and dealer
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Display initial hands
    display_hand("Player", player_hand)
    print(f"Dealer's visible card: {dealer_hand[0][0]}")

    # Player's turn
    while True:
        player_value = calculate_hand_value(player_hand)
        print(f"Player value: {player_value}")
        if player_value > 21:
            print("Player busts! Dealer wins.")
            return
        choice = input("Do you want to (H)it or (S)tand? ").strip().lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            display_hand("Player", player_hand)
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please choose H or S.")

    # Dealer's turn
    display_hand("Dealer", dealer_hand)
    while True:
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Dealer's hand value: {dealer_value}")
        if dealer_value > 21:
            print("Dealer busts! Player wins.")
            return
        elif dealer_value >= 17:
            break
        else:
            print("Dealer hits.")
            dealer_hand.append(deck.pop())
            display_hand("Dealer", dealer_hand)

    # Determine the winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Final Player value: {player_value}, Final Dealer value: {dealer_value}")
    if player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("Push! It's a draw!")

def play_blackjack():
    """Runs the Blackjack game with a play again feature."""
    play_again = True
    while play_again:
        blackjack_game()
        response = input("Do you want to play again? (Y/N): ").strip().upper()
        play_again = response == 'Y'
    print("Thanks for playing Blackjack!")

# Run the game
if __name__ == '__main__':
    play_blackjack()
