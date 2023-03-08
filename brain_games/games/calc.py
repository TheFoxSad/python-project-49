import random
import operator

RULES = 'What is the result of the expression?'


def get_question_and_right_answer():
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul}
    op_name = random.choice(["+", "-", "*"])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f"{num1} {op_name} {num2}"
    if op_name in operators:
        right_answer = operators[op_name](num1, num2)
    return question, str(right_answer)
