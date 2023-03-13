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
    current_round = 0
    while current_round < ROUNDS:
        question, right_answer = game.get_question_and_right_answer()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if right_answer == answer:
            print('Correct!')
            current_round += 1
            if current_round == ROUNDS:
                print(f'Congratulations, {name}!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            break
