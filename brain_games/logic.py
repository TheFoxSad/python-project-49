import prompt
import random

def even_parity():
    print(f'Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    count_question = 0
    while  count_question < 3:
        question_num = random.randint(1, 100)
        if question_num % 2 == 0:
            check_even = 'yes'
        elif question_num %2 != 0:
            check_even = 'no'
        print(f'Question: {question_num}')
        answer = input('Your answer: ')
        if check_even == answer:
            print(f'Correct')
            count_question += 1
        elif check_even != answer:
            print(f""""{answer}" is wrong answer ;(. Correct answer was "{check_even}".
Let's try again, {name}!""")
            break
        if count_question == 3:
            print(f'Congratuletion, {name}!')
