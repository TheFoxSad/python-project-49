import random
import math

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_right_answer():
    question = random.randint(1, 100)
    if question < 2:
        right_answer = "no"
        return question, right_answer
    for i in range(2, int(math.sqrt(question) + 1)):
        if question % i == 0:
            right_answer = "no"
            return question, right_answer
    else:
        right_answer = "yes"
        return question, right_answer
