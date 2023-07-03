import math as m
import unittest

class TestMethods(unittest.TestCase):

    def test_centerX(self):
        self.assertEqual(f("3"), 1.609)

    def test_bigX(self):
        self.assertEqual(f("5"), 1.108)

    def test_smallX(self):
        self.assertEqual(f("-1"), -1.54)

    def test_incorrectInput(self):
        self.assertIsNone(f("fail"))

def f(x: str):

    # Проверка введенного значения
    try:
        x = float(x)
    except:
        print("Значение 'X' введено некорректно")
        return

    # Вычисление y
    if x < 3:
        y = round(x * m.cos(m.pow(x,3)) + x, 3) 
    else:
        y =  round(m.sqrt(x) * m.cos(0.0421 * m.pow(x,2)), 3)
    return y

if __name__ == '__main__':

    # unittest.main()

    x = input("Введите x: ")
    y = f(x)
    print(y)