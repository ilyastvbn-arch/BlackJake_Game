class Card:
    """Card of the game"""
    
    values_map = {
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10,
        "A": 11
    }
    
    # Define ranks and suits for the deck of cards
    ranks = list(values_map.keys())
    suits = ["diamonds", "clubs", "hearts", "spades"]
    
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        
    def get_value(self):
        """Get the value of the card"""
        return self.values_map.get(str(self.rank), 0)