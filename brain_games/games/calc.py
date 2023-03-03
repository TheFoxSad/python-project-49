import random

ROUNDS = 3


def rules():
    print('What is the result of the expression?')


def random_data():
    operator = random.choice(["+", "-", "*"])
    first_num = random.randint(1, 10)
    second_num = random.randint(1, 10)
    question = str(first_num) + operator + str(second_num)
    if operator == "+":
        right_answer = first_num + second_num
    elif operator == "-":
        right_answer = first_num - second_num
    elif operator == "*":
        right_answer = first_num * second_num
    return question, str(right_answer)
