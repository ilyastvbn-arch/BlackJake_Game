from Card import Card
import random

class BlackJack:
    """The game BlackJack. Logic"""
    
    def hand_value(self, hand: list[Card]) -> int:
        """Convert list of cards to general points"""
        total = sum(card.get_value() for card in hand)
        aces = sum(1 for card in hand if card.rank == "A")
        while total > 21 and aces:
            total -= 10
            aces -= 1
                
        return total
    
    def show_hand(self, hand:list[Card]) -> str:
        """Convert list of cards to string"""
        return ", ".join(f"{card.rank} {card.suit}" for card in hand)
    
    def launch_the_game(self):
       
        #Define ranks and suits for the deck of cards
        ranks = Card.ranks
        suits = Card.suits
       
        #Create a deck of cards
        deck = [Card(rank, suit) for suit in suits for rank in ranks]
        
        #Shuffle the deck
        random.shuffle(deck)

        #Initialize hands for the player and the dealer
        player_hand = []
        pc_hand = []
        
        #Deal two cards to the player and the dealer
        for _ in range(2):
            player_hand.append(deck.pop())
            pc_hand.append(deck.pop())
        
        #Main logic of the game    
        while True:
            
            # Show the player's hand and the dealer's first card, 
            # and the total points of the player's hand
            print(
                "\nDealer's cards:", f"{pc_hand[0].rank} {pc_hand[0].suit}, ??",
                "\nYour cards:", self.show_hand(player_hand),
                "\nYour total:", self.hand_value(player_hand)
            )

            # Check if player has 21 points for lose
            if self.hand_value(player_hand) > 21:
                break

            while True:
                
                #If player "hit" - add one more card to his hand, 
                #if "stand" - end the game to finals
                action = input("Hit or stand? ").lower().strip()
                
                if action == "hit":
                    player_hand.append(deck.pop())
                    break
                elif action == "stand":
                    break
                else:
                    print("Invalid input! Please type 'hit' or 'stand'.")
            if action == "stand":
                break

        #Logic of the dealer's game. He must take cards until he has 17 or more points
        while self.hand_value(pc_hand) < 17:
            pc_hand.append(deck.pop())
            
        #Output the dealer's hand and total points for player   
        print("Dealer's cards:", self.show_hand(pc_hand))
        print("Dealer total:", self.hand_value(pc_hand))

        #Total points of the player and the dealer
        player_total = self.hand_value(player_hand)
        dealer_total = self.hand_value(pc_hand)

        #Result of the game
        print("\n=== RESULT ===")
        
        if player_total > 21 and dealer_total > 21: #if both have moer points
            print("Draw!")                    
        elif player_total > 21: #if player has more than 21 points, he lose
            print("You lose!")  
        elif dealer_total > 21: #if dealer has more than 21 points, he lose
            print("Dealer busted! You win! ")  
        elif player_total > dealer_total: #if player has more points than dealer, he win
            print("You win! ")
        elif player_total < dealer_total: #if dealer has more points than player, he win
            print("You lose!")
        else:
            print("ERROR: Unexpected result!")