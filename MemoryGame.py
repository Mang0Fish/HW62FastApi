from random import randint

def allGuessed(lst1: list[str]) -> bool:
    for i in lst1:
        if i == 'Guessed':
            continue
        else:
            return False
    return True


letters: list[chr] = ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C',  'D', 'E', 'F']
cards: list[str] = []
p: int = 11
# P is the top index for the randint method
for i in range(12):
    cards.append((letters.pop(randint(0,p))))
    p -= 1
# Random creation of the cards
print("Welcome to the memory game ! \nThere are 6 pairs of letters in a deck of cards, the letters A to F are assigned to the cards")
print("Guess their position in the deck of cards from 1-12 and win !")
print("You can restart the game by typing 'r' and end the game by typing 'End'")
ans: str = ''
while ans.upper() != 'END':
    ans = input("Enter the firsts card position! ")
    # The win line
    if allGuessed(cards):
        print("You won !")
        ans = input("Type 'R' to play again, 'End' to end the game ")
    # The restart line
    if ans.upper() == 'R':
        letters: list[chr] = ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F']
        p: int = 11
        for i in range(12):
            cards.append((letters.pop(randint(0, p))))
            p -= 1
        print("Game Restarted!")
    # First card try
    try:
        print(cards[int(ans)-1])
        tempPos = int(ans)-1
        ans = input("Enter the seconds card position")
        # Second card try
        try:
            print(cards[int(ans) - 1])
            # Cards matched
            if cards[int(ans) - 1] == cards[tempPos] and int(ans) - 1 != tempPos and (cards[int(ans) - 1] != 'Guessed' or cards[tempPos] != "Guessed"):
                print("You matched the cards !")
                cards[int(ans) - 1] = 'Guessed'
                cards[tempPos] = 'Guessed'
            # Same card guessed twice
            elif int(ans) - 1 == tempPos:
                print("You guessed the same number twice")
            # Already guessed card
            elif cards[int(ans) - 1] == 'Guessed' or cards[tempPos] == "Guessed":
                print("You already guessed it")
            # Unmatched cards
            else:
                print("Try again")
        # Index out of range
        except IndexError:
            print("Position out of range")
        # Every other error
        except:
            print("Enter a number")
    # Index out of range
    except IndexError:
        print("Position out of range")
    # Every other error
    except:
        print("Enter a number")