import random
import math

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_number():
    quest_number = random.randint(1, 100)
    return quest_number


def get_question_and_right_answer():
    question = generate_number()
    if question < 2:
        right_answer = "no"
        return question, right_answer
    for i in range(2, int(math.sqrt(question) + 1)):
        if question % i == 0:
            right_answer = "no"
            return question, right_answer
    right_answer = "yes"
    return question, right_answer
