"""
Решение задачи FizzBuzz.
См. описание в description.md.

Содержит три варианта решения задачи:
1) check_number_v1 - наивное решение;
2) check_number_v2 - лаконичное решение;
3) check_number_v3 - короткое решение.
"""


def check_number_v1(number):
    """Проверка числа для игры FizzBuzz.
    Проверка на делимость "в лоб". Встречается повторяющийся код.
    :param number: проверяемое число.
    :type number: int
    :return: строка 'FizzBuzz', если число кратно 3 и 5,
             строку 'Fizz', если число кратно 3,
             строку 'Buzz', если число кратно 5, иначе само число.
    :rtype: int или str
    """
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


def check_number_v2(number):
    """Проверка числа для игры FizzBuzz.
    Более лаконичное решение по сравнению с check_number_v1.
    :param number: проверяемое число.
    :type number: int
    :return: строка 'FizzBuzz', если число кратно 3 и 5,
             строку 'Fizz', если число кратно 3,
             строку 'Buzz', если число кратно 5, иначе само число.
    :rtype: int или str
    """
    result = ''
    if number % 3 == 0:
        result += 'Fizz'
    if number % 5 == 0:
        result += 'Buzz'
    return result if result else number


def check_number_v3(number):
    """Проверка числа для игры FizzBuzz.
    Короткая версия решения. Здесь используется свойство логического
    типа, а именно его эквивалентность 0 или 1.
    :param number: проверяемое число.
    :type number: int
    :return: строка 'FizzBuzz', если число кратно 3 и 5,
             строку 'Fizz', если число кратно 3,
             строку 'Buzz', если число кратно 5, иначе само число.
    :rtype: int или str
    """
    result = 'Fizz' * (not number % 3) + 'Buzz' * (not number % 5)
    return result if result else number


def fizzbuzz(number, version=1):
    """Игра FizzBuzz.
    :param number: верхняя граница (ключительно).
    :type number: int
    :param version: версия решения: 1 - наивное,
                    2 - лаконичное, 3 - короткое.
    :type version: int
    """
    for i in range(1, number + 1):
        if version == 1:
            print(check_number_v1(i))
        elif version == 2:
            print(check_number_v2(i))
        else:
            print(check_number_v3(i))


def main():
    n = input('Введите n: ')
    if n.isdigit() and int(n) >= 1:
        n = int(n)
    else:
        print('Введено некорректное значение')
        return

    version = input('Введите версию программы: ')
    if version.isdigit() and 1 <= int(version) <= 3:
        version = int(version)
    else:
        version = 1
        print('Введено некорректное значение. Используется значение 1')

    fizzbuzz(n, version)


if __name__ == '__main__':
    main()
