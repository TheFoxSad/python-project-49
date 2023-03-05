import sys
from brain_games import logic
from brain_games.games import calc, even, prime, gcd, progression


my_dict = {"brain-calc"        : calc,
           "brain-even"        : even,
           "brain-prime"       : prime,
           "brain-_gcd"         : gcd,
           "brain-progression" : progression}


def main():
    value = my_dict.get(sys.argv[0])
    logic.start_game(value)

