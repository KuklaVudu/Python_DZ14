import unittest


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


class TestPrimeHexNumber(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(prime_number(2, 0, 100000), 'Число простое')

    def test_composite_number(self):
        self.assertEqual(prime_number(4, 0, 100000),'Число составное')

    def test_input_limit(self):
        self.assertEqual(prime_number(-5, 0, 100000),'Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч')    
 
    def test_max_limit(self):
        self.assertEqual(prime_number(200000, 0, 100000),'Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч')
    
    def test_hex_func_123(self):
        self.assertEqual(hex_func(123),"result_str='7b'")
    
    def test_hex_func_3(self):
        self.assertEqual(hex_func(3),"result_str='3'")   


if __name__ == "__main__":
   unittest.main(verbosity=2)