"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
 классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    def __init__(self):
        self.__clothes_list = list()
        self.__class_lookup = {'Suit': Suit, 'Coat': Coat}

    def clothes_list(self, name='', measure=0.0):
        self.__clothes_list.append([name.capitalize(), measure])

    def cloth_measure(self):
        __total = 0
        for __elm in self.__clothes_list:
            __a = self.__class_lookup[__elm[0]](__elm[1])
            __value = __a.value
            __total += __value
            print(f'{__elm[0]}, {__elm[1]}, {__value:.2f}')
        return __total


class Suit:
    def __init__(self, height=0.0):
        self.__height = height

    @property
    def value(self):
        return 2 * self.__height + 0.3


class Coat:
    def __init__(self, size=0.0):
        self.__size = size

    @property
    def value(self):
        return self.__size / 6.5 + 0.5


source_list = (['suit', 52], ['suit', 56], ['Coat', 178], ['Suit', 54], ['coat', 190])
# result_list = list()
order = Clothes()
for el in source_list:
    order.clothes_list(el[0], el[1])
print(f'total: {order.cloth_measure():.2f}')
