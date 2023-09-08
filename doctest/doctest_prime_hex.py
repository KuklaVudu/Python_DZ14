def prime_number(number: int, min: int, max: int):
    """
    >>> prime_number(5, 0, 100000)
    Число простое
    >>> prime_number(4, 0, 100000)
    Число составное
    >>> prime_number(-5, 0, 100000)
    Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч
    >>> prime_number(200000, 0, 100000)
    Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч
    """

    divider = 2
    count = 0

    if (number >= min and number <= max):
        for i in range(divider, number - 1):
            if (number% i == 0):
                count += 1
        if (count <= 0):
            print('Число простое')
        else:
            print('Число составное')
    else:
        print('Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч')


def hex_func(number: int, n = 16) -> str:
    """
    >>> hex_func(123)
    "result_str='7b'"
    >>> hex_func(3)
    "result_str='3'"
    """

    hex_number = "0123456789abcdef"
    result_str = ""
    while number > 0:
        result_str = hex_number[number % n] + result_str
        number = number // n
    return f'{result_str=}'


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)