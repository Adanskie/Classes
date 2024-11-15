from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        # Loop para sa 10 rolls, hindi nakadepende sa sides
        for _ in range(10):
            # Pag-roll ng 3 iba't ibang dice
            print(randint(1, self.sides), end=" ")           # Normal roll (1 hanggang sides)
            print(randint(1, self.sides + 4), end=" ")       # Roll na may dagdag na 4
            print(randint(1, self.sides + 14), end=" ")      # Roll na may dagdag na 14
            print()  # Para mag bagong linya pagkatapos ng bawat set ng rolls

# Paglikha ng isang Die object
get_value = Die()

# Pag-roll ng dice 10 beses
get_value.roll_die()
