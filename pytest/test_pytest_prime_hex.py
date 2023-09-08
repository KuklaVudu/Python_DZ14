from pytest_prime_hex import prime_number, hex_func
import pytest


def test_prime_number():
    assert prime_number(2, 0, 100000) == 'Число простое'


def test_composite_number():
    assert prime_number(4, 0, 100000) == 'Число составное'


def test_input_limit():
    assert prime_number(-5, 0, 100000) == 'Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч'    
 

def test_max_limit():
    assert prime_number(200000, 0, 100000) == 'Ограничение на ввод отрицательных чисел и чисел больше 100 тысяч'
    

def test_hex_func_123():
    assert hex_func(123) == "result_str='7b'"
   
    
def test_hex_func_3():
    assert hex_func(3) == "result_str='3'"   


if __name__ == "__main__":
   pytest.main(['-vv'])