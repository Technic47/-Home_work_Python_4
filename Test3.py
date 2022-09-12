# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
from random import randint


class List:
    def __init__(self, length: int):
        self.length = length
        self.numbers = []

    def rand_list(self, n, minn, maxx):
        """
        Функция для создания одномерного списка
        с псевдослучайным заполнениемю
        :param n: - длина списка
        :param minn: - минимальное число
        :param maxx: - максимальное число
        :return: - заполненный список
        """
        numbers = [randint(minn, maxx) for i in range(n)]
        print('Изначальный массив: {}'.format(numbers))
        self.numbers = numbers
        return numbers

    def list_of_unique(self):
        """
        Function creates a list with unique numbers from original list
        :return:
        """
        unique = []
        for i in range(self.length):
            if self.numbers.count(self.numbers[i]) == 1:
                unique.append(self.numbers[i])
        print(unique)


n = int(input('Enter list length: '))
numbers = List(n)
numbers.rand_list(n, 0, 9)
numbers.list_of_unique()
