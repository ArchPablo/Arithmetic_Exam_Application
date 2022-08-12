import random as r


def check_level():
    while True:
        try:
            answer = int(input('Which level do you want? Enter a number:\n'
                               '1 - simple operations with numbers 2-9\n'
                               '2 - integral squares of 11-29\n'))
            if answer in [1, 2]:
                return answer
            else:
                print('Incorrect format')
        except ValueError:
            print('Incorrect format')


def check_answer(task: str):
    n = 0
    while True:
        try:
            answer_user = int(input(f'{task}\n'))
            if answer_user == eval(task):
                print('Right!\n')
                n += 1
                return n
            else:
                print('Wrong!\n')
                return n
        except ValueError:
            print('Incorrect format\n')


def get_task(type_task: int):
    if type_task == 1:
        _task = f"{r.randint(2, 9)} {r.choice(['-', '+', '*', '/'])} {r.randint(2, 9)}"
    else:
        _task = f"{r.randint(11, 29) ** 2}"
    return _task


def exam(type_task: int):
    num_correct_ans = 0
    for _ in range(5):
        task = get_task(type_task)
        num_correct_ans += check_answer(task)
    print(f'Your mark is {num_correct_ans}/5')
    get_file_result(num_correct_ans, type_task)


def get_file_result(result: int, level: int):
    answer = input('Would you like to save your result to the file? Enter yes or no\n').lower()
    if answer == 'yes' or (answer[0] == 'y' and len(answer) == 1):
        user_name = input('What is your name?\n')

        if level == 1:
            level_description = 'simple operations with numbers 2-9'
        else:
            level_description = 'integral squares 11-29'

        file = open('results.txt', 'a', encoding='utf-8')
        file.write(f'{user_name}: {result}/5 in level {level} {level_description}\n')
        file.close()
        print('The results are saved in "results.txt".')
    else:
        return


def main():
    ans_1 = check_level()
    if ans_1 == 1:
        exam(1)
    elif ans_1 == 2:
        exam(2)


if __name__ == "__main__":
    main()
