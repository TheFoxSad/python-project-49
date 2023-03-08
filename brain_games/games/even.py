import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def random_data():
    question = random.randint(0, 100)
    if question % 2 == 0:
        right_answer = 'yes'
    elif question % 2 != 0:
        right_answer = 'no'
    return question, right_answer
