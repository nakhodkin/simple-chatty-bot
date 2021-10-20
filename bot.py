def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    correct_answer = False
    correct_answer_index = 1

    answers = [
        "To repeat a statement multiple times.",
        "To decompose a program into several small subroutines.",
        "To determine the execution time of a program.",
        "To interrupt the execution of a program."
    ]

    while True:
        print("Why do we use methods?")

        for i, text in enumerate(answers, start=1):
            print(f"{i}. {text}")

        user_answer = int(input())
        if user_answer == correct_answer_index - 1:
            break
        print("Please, try again.")

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
