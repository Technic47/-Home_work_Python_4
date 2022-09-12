# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


def simpl_mults(n):
    """
    Function creates list of simple multipliers for "n" number
    :param n: - number for calculation
    :return: - list of multipliers
    """
    numbers = []
    for i in range(2, n):
        while n % i == 0:
            for j in range(2, i + 1):
                if i % j == 0 and i != j:
                    break
                elif i % j != 0:
                    continue
                else:
                    numbers.append(i)
                    n /= i
    return numbers

n = int(input('Enter your number: '))
numbers = simpl_mults(n)
print(f'{numbers} - minimum multipliers of your number {n}')
