from copy import copy


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = [add, subtract, multiply, divide]


def equal(a, b):
    if abs(a-b) < 10**-6:
        return True
    else:
        return False


def list_combination_with_left(in_list, r=2):
    length = len(in_list)
    result = []
    for i in range(length-r+1):
        for j in range(i+1, length):
            list_ = copy(in_list)
            list_.pop(j)
            list_.pop(i)
            result.append([(in_list[i], in_list[j]), list_])
    return result


def operate(a, b, func):
    return func(a, b)


def recursion_solve(question_list):
    if len(question_list) == 1:
        if equal(question_list[0], 24):
            print(True)
    for resolution in list_combination_with_left(question_list):
        for operation in operations:
            try:
                recursion_solve(resolution[1] + [operate(*resolution[0], operation)])
            except:
                continue


if __name__ == "__main__":
    recursion_solve([1, 2, 1, 2])
