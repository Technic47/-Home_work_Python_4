# Вычислить число Gb c заданной точностью d
# 3,1415926535897932384626433832795

import time
from math import factorial
from decimal import *


class Number:
    def __init__(self, accuracy=5):
        """
        :param accuracy: - numbers after zero.
        """
        self.accuracy = accuracy

    def reference(self):
        """
        Function shows pi number shortened with accuracy value.
        :return:
        """
        pi = round(3.1415926535897932384626433832795, self.accuracy)
        print(f'{pi} - Reference Pi number')
        return pi

    def leibniz(self):
        """
        Function for calculation pi number using Leibnitz formula(row)
        It works till accuracy 6. After 6 it takes ages to finish. Don`t use it.
        :return:
        """
        result = 0
        pi = round(3.1415926535897932384626433832795, self.accuracy)
        iterations = 1
        tic = time.perf_counter()
        while round(result, self.accuracy) != pi:
            a = (iterations + (iterations - 1))
            result += (4 / a)
            b = iterations + (iterations - 1) + 2
            result -= (4 / b)
            iterations += 2
        toc = time.perf_counter()
        print(f'{round(result, self.accuracy)} - Calculeited Pi number with Leibniz formula')
        print(f'{iterations} - Number of iterations for Leibniz formula')
        print(f'{toc - tic:0.4f}s - Time for calculations')
        return iterations

    def nilakanta(self):
        """
        Function for calculation pi number using Nilakanta formula(row)
        It works till accuracy 6. After 6 it do not proceed. Seems, my code is awfull.
        :return:
        """
        result = 3
        pi = round(3.1415926535897932384626433832795, self.accuracy)
        iterations = 1
        tic = time.perf_counter()
        while round(result, self.accuracy) != pi:
            a = 2 * iterations
            b = a + 2
            result += 4 / (a * (a + 1) * (a + 2))
            result -= 4 / (b * (b + 1) * (b + 2))
            iterations += 2
        toc = time.perf_counter()
        print(f'{round(result, self.accuracy)} - Calculeited Pi number with Nilakata formula')
        print(f'{iterations} - Number of iterations for Nilakata formula')
        print(f'{toc - tic:0.4f}s - Time for calculations')
        return iterations

    def chudnovsky(self):
        """
        Function for calculation pi number using Chudnovskogo formula(summ of factorials).
        Copied it from the internet. Super fast.
        It works till accuracy 26. After it shows an error.
        :return:
        """
        result = Decimal(0)
        i = 0  # iterations
        tic = time.perf_counter()
        while i < self.accuracy:
            result += (Decimal(-1) ** i) * (Decimal(factorial(6 * i)) / ((factorial(i) ** 3) * (factorial(3 * i))) * (
                    13591409 + 545140134 * i) / (640320 ** (3 * i)))
            i += 1
        result = result * Decimal(10005).sqrt() / 4270934400
        result = result ** (-1)
        toc = time.perf_counter()
        print(f'{round(result, self.accuracy)} - Calculeited Pi number with Chudnovskogo formula')
        print(f'{i} - Number of iterations for Chudnovskogo formula')
        print(f'{toc - tic:0.4f}s - Time for calculations')
        return result

    # def info(self):
    #     print(self.accuracy)


d = int(input('Enter accuracy: '))

number1 = Number()
number2 = Number(d)
number3 = Number(d)
number1.reference()
number1.leibniz()
print()
number2.reference()
number2.nilakanta()
print()
number3.reference()
number3.chudnovsky()
