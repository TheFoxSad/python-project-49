import prompt


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def start_game(game):
    name = greeting()
    game.rules()
    for current_round, _ in enumerate(range(game.ROUNDS), 1):
        question, right_answer = game.random_data()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            r_a = right_answer
            print(f""""{answer}" is wrong answer ;(. Correct answer was "{r_a}".
Let's try again, {name}!""")
            break
    if current_round == game.ROUNDS:
        print(f'Congratulations, {name}!')
