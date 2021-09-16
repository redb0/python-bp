"""Бессмысленный и беспощадный способ реализации hello world"""

import random


def str_printer_decorator(number_of_str):
    """Декоратор печати последовательности элементов

    :param number_of_str: количество элементов
    :type number_of_str: int
    """
    def decorator(func):
        def str_printer(*args):
            count = 0
            sentinel = object()
            def get_next_str():
                nonlocal count
                count += 1
                if count <= number_of_str:
                    return func(*args)
                return sentinel

            print(' '.join(iter(get_next_str, sentinel)))
        return str_printer
    return decorator


class StringPrinterMeta(type):
    """Конструктор "печатающих" классов"""
    def __new__(cls, *args, **kwargs):
        model = type.__new__(cls, *args, **kwargs)
        @str_printer_decorator(model.number)
        def print_strings():
            with open(__file__) as file:
                lines = file.readlines()
                i = 0
                while True:
                    print(f'{i = }')
                    line = random.choice(lines).strip()
                    try:
                        exec(f'{line}', {}, globals())
                        return string
                    except:
                        pass
                    i += 1
        print_strings()


class StringPrinter(metaclass=StringPrinterMeta):
    """Печатающий класс"""
    string = 'hello world'
    number = 2
