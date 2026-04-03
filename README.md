#  BlackJack Game

A console-based Blackjack card game written in Python.

##  How to Play

The goal is to get as close to **21 points** as possible without going over, beating the dealer.

**Game flow:**
1. Both the player and dealer are dealt 2 cards
2. The dealer shows only one of their cards
3. On each turn you choose: **Hit** (take a card) or **Stand** (stop)
4. After the player stands, the dealer draws cards until reaching 17+ points
5. Whoever is closest to 21 without busting wins

**Card values:**
- Number cards → face value (2–10)
- Face cards (J, Q, K) → 10 points
- Ace (A) → 11 points, or 1 if 11 would cause a bust

##  Project Structure

```
BlackJake_Game/
├── MainLauncher.py     # Entry point — starts the game
├── BlackJackLogic.py   # Core game logic
└── Card.py             # Card model (ranks, suits, values)
```

##  How to Run

No dependencies required — only standard Python.

1. Clone the repository:
```bash
git clone https://github.com/ilyastvbn-arch/BlackJake_Game.git
cd BlackJake_Game
```

2. Run the game:
```bash
python MainLauncher.py
```

##  Example Gameplay

```
Dealer's cards: K ♠, ??
Your cards: 7 ♥, 9 ♦
Your total: 16

Hit or stand? hit

Dealer's cards: K ♠, 6 ♣, 5 ♦
Dealer total: 21

=== RESULT ===
You lose!
```

## Requirements

- Python 3.10+
