# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint
from numpy import roots


class Equation:
    def __init__(self):
        self.path = None
        self._degree = None

    def create_equation(self, degree: int, path):
        """
        Function creates equation with selected degree and write it in path.
        :param degree: - number of degrees
        :param path: - where to write equation
        :return:
        """
        self._degree = degree
        self.path = path
        with open(self.path, 'w') as data:
            for i in range(self._degree, 0, -1):
                num = randint(0, 100)
                data.write(f'{num}*x^{i} + ')
            num = randint(0, 100)
            data.write(f'{num} = 0')


deg = int(input('Enter degree of equation: '))
equation1 = Equation()
equation1.create_equation(deg, r'C:\Users\Pavel\Documents\GeekBrain\Python_Homework\Seminar4\Test4_1.txt')
equation2 = Equation()
equation2.create_equation(deg, r'C:\Users\Pavel\Documents\GeekBrain\Python_Homework\Seminar4\Test4_2.txt')


class Text:
    def __init__(self, path):
        self.path = path
        self.text = ''
        self.numbers = []
        self.coefficients = []

    def split(self):
        """
        Function splits imported text using '*' and ' ' splitters.
        :return:
        """
        with open(self.path, 'r') as data:
            self.text = data.read().replace('*', ' ').replace('^', ' ').split(' ')

    def print(self):
        """
        Function prints line of text
        :return:
        """
        print(self.text)

    def get_numbers(self):
        """
        Function takes digits from tex line and put it inside list.
        :return:
        """
        for i in range(len(self.text)):
            if self.text[i].isdigit():
                self.numbers.append(int(self.text[i]))
        print(self.numbers)
        return self.numbers

    def summ(self, list_of_numbers):
        """
        Function creates a sum of two lists with numbers.
        :param list_of_numbers: - second list with numbers
        :return:
        """
        numbers2 = list_of_numbers
        for i in range(0, len(self.numbers), 2):
            summ = self.numbers[i] + numbers2[i]
            self.coefficients.append(summ)
        print(f'Coefficients of your equation are:\n{self.coefficients}')

    def send_summ(self, write_path):
        """
        Function write new equation to selected path.
        :param write_path: - path for writing equation
        :return:
        """
        with open(write_path, 'w') as data:
            index = (len(self.coefficients) - 1)
            for i in range(len(self.coefficients)):
                if i < len(self.coefficients) - 1:
                    data.write(f'{self.coefficients[i]}*x^{index} + ')
                else:
                    data.write(f'{self.coefficients[i]} ')
                index -= 1
            data.write(' = 0')

    def find_roots(self):
        """
        Function calculate roots of the equation.
        NumPy
        :return:
        """
        res = roots(self.coefficients)
        print(f'Roots of the equation are:\n{res}')


text1 = Text(r'C:\Users\Pavel\Documents\GeekBrain\Python_Homework\Seminar4\Test4_1.txt')
text2 = Text(r'C:\Users\Pavel\Documents\GeekBrain\Python_Homework\Seminar4\Test4_2.txt')

text1.split()
text1.print()
text1.get_numbers()

text2.split()
text2.print()
text2.get_numbers()

text1.summ(text2.numbers)
text1.send_summ(r'C:\Users\Pavel\Documents\GeekBrain\Python_Homework\Seminar4\Test4_3.txt')

text1.find_roots()