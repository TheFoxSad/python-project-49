import random

rounds = 3

def rules():
    print(f'What is the result of the expression?')

def random_data():
    start = random.randint(0, 25)
    step = random.randint(2, 5)
    len_prog = 10
    quest = []
    for i in range(len_prog):
        start += step
        quest.append(start)
    index = quest.index(random.choice(quest))
    right_answer = quest[index]
    quest[index] = ".."
    question_num = " ".join(map(str,quest))
    return question_num, str(right_answer)
