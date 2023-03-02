import random
import math

rounds = 3

def rules():
    print(f'Answer "yes" if given number is prime. Otherwise answer "no".')

def random_data():
    question = random.randint(1, 100)
    if question < 2:
        right_answer = "no"
    for i in range(2, int(math.sqrt(question) + 1)):
        if question % i == 0:
            right_answer = "no"
        else:
            right_answer = "yes"
    return question, right_answer
