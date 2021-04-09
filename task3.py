"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
(__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, chromosome):
        self.chromosome = chromosome

    def __add__(self, other):
        return Cell(self.chromosome + other.chromosome)

    def __sub__(self, other):
        if self.chromosome - other.chromosome > 0:
            return Cell(self.chromosome - other.chromosome)
        else:
            return f'cell goes away'

    def __mul__(self, other):
        return Cell(self.chromosome * other.chromosome)

    def __truediv__(self, other):
        return Cell(self.chromosome // other.chromosome)

    def __str__(self):
        return f'{self.chromosome}'

    def make_order(self, number):
        return ('*' * number + '\n') * (self.chromosome // number) + ('*' * abs(self.chromosome % number) + '\n')


cl1 = Cell(int(input('Enter quantity of chromosomes into the first cell: ')))
cl2 = Cell(int(input('Enter quantity of chromosomes into the second cell: ')))
print(f'cl1 + cl2 = {cl1 + cl2}')
print(f'cl1 - cl2 = {cl1 - cl2}')
print(f'cl2 - cl1 = {cl2 - cl1}')
print(f'cl1 * cl2 = {cl1 * cl2}')
print(f'cl1 / cl2 = {cl1 / cl2}')
print()
a = Cell(int(input('Enter quantity of chromosomes into the cell: ')))
num = int(input('Enter number of chromosomes into the row: '))
print(a.make_order(num))
