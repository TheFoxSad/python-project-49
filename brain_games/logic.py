import prompt


def start_game(game):
    print(f'Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    game.rules()
    current_round = 0
    while  current_round < game.rounds:
        question, right_answer = game.random_data()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if right_answer == answer:
            print(f'Correct!')
            current_round += 1
        elif right_answer != answer:
            print(f""""{answer}" is wrong answer ;(. Correct answer was "{right_answer}".
Let's try again, {name}!""")
            break
        if current_round == game.rounds:
            print(f'Congratuletion, {name}!')
