import random  # Importing the random module to generate random numbers

# 🎴 Define suit priorities for comparison (Spades strongest, Clubs weakest)
suit_priority = {"Spades": 4, "Hearts": 3, "Diamonds": 2, "Clubs": 1}


# 🧠 Define the Simple Reflex Agent class for our casino-style card game
class SimpleReflexCasinoAgent:

    # 🚀 Initialization method runs when an object is created
    def __init__(self, num_players):
        self.num_players = num_players  # Total number of players
        self.players = list(range(1, num_players + 1))  # Player IDs: 1 to num_players
        self.cards = self.generate_cards()  # Generate random cards for players
        self.used_players = set()  # Keep track of players who got cards
        self.used_cards = set()  # Keep track of cards that are assigned
        self.assignments = {}  # Dictionary to store which player got which card

    # 🃏 Method to generate a random card (number and suit) for each player
    def generate_cards(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]  # All possible suits
        cards = []
        for i in range(self.num_players):  # Repeat for each player
            number = random.randint(2, 14)  # Card number from 2 to 14 (like 2 to Ace)
            suit = random.choice(suits)  # Randomly choose a suit
            cards.append((number, suit))  # Add the card as a tuple (number, suit)
        return cards  # Return the full list of generated cards

    # 🎲 Simulate a dice roll to pick a random player or card
    def roll_dice(self):
        return random.randint(1, self.num_players)  # Random number between 1 and total players/cards

    # 🎮 Main method to simulate the game and assign cards randomly
    def play_game(self):
        while len(self.used_players) < self.num_players and len(self.used_cards) < self.num_players:
            player_roll = self.roll_dice()  # Roll dice to select a random player
            card_roll = self.roll_dice()  # Roll dice to select a random card

            # ✅ Assign only if both player and card are unused
            if player_roll not in self.used_players and card_roll not in self.used_cards:
                self.used_players.add(player_roll)  # Mark player as used
                self.used_cards.add(card_roll)  # Mark card as used
                self.assignments[player_roll] = self.cards[card_roll - 1]  # Assign card to player
                print(f"Assigned Card {self.cards[card_roll - 1]} to Player {player_roll}")  # Show assignment

    # 👑 Determine and announce the winner based on card value and suit priority
    def announce_winner(self):
        best_player = None  # To track the winner
        best_card = (0, "")  # Initialize with lowest card

        # 🔍 Loop through each assignment to find the best card
        for player, card in self.assignments.items():
            number, suit = card
            # 📈 Compare current card with the best one so far
            if (number > best_card[0]) or (number == best_card[0] and
                                           suit_priority[suit] > suit_priority[best_card[1]]):
                best_card = card  # Update best card
                best_player = player  # Update best player

        # 🎉 Print the final winner with the highest-ranked card
        print(f"\n🎉 Winner is Player {best_player} with Card {best_card[0]} of {best_card[1]}")


# ✅ Example usage
agent = SimpleReflexCasinoAgent(num_players=5)  # Create game instance with 5 players
agent.play_game()  # Run the game
agent.announce_winner()  # Announce the winner
