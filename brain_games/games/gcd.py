import random

ROUNDS = 3


def rules():
    print('Find the greatest common divisor of given numbers.')


def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def random_data():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    question = f'{first_num} {second_num}'
    right_answer = gcd(first_num, second_num)
    return question, str(right_answer)
