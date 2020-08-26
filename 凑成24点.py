from copy import copy


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def list_combination_with_left(in_list, r):
    length = len(in_list)
    result = []
    for i in range(length-r):
        for j in range(i+1, length):
            list_ = copy(in_list)
            list_.pop(j)
            list_.pop(i)
            result.append([(in_list[i], in_list[j]), list_])
    return result

list_combination_with_left([1,2,3,4],2)