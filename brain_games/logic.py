import prompt

ROUNDS = 3


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def start_game(game):
    name = greeting()
    print(game.RULES)
    for current_round, _ in enumerate(range(ROUNDS), 1):
        question, right_answer = game.get_question_and_right_answer()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if right_answer == answer:
            print('Correct!')
            if current_round == ROUNDS:
                print(f'Congratulations, {name}!')
        else:
            r_a = right_answer
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "{r_a}".
Let's try again, {name}!''')
            break
