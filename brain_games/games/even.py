import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    question = random.randint(0, 100)
    if question % 2 == 0:
        right_answer = 'yes'
    elif question % 2 != 0:
        right_answer = 'no'
    return question, right_answer
