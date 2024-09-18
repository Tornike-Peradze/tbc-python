import random

suits = ['♣', '♦', '♥', '♠']
values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

# Getting random suit and value
random_suit = random.choice(suits)
random_value = random.choice(values)

print(f"It's: {random_value}{random_suit}")
