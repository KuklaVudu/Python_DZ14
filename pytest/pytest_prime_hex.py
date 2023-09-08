def prime_number(number: int, min: int, max: int) -> str:
    divider = 2
    count = 0

    if (number >= min and number <= max):
        for i in range(divider, number - 1):
            if (number% i == 0):
                count += 1
        if (count <= 0):
            result = 'Число простое'
        else:
            result = 'Число составное'
    else:
        result = 'Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч'
    return result    

def hex_func(number: int, n = 16) -> str:
    hex_number = "0123456789abcdef"
    result_str = ""
    while number > 0:
        result_str = hex_number[number % n] + result_str
        number = number // n
    return f'{result_str=}'