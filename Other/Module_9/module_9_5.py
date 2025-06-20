# Домашнее задание по теме "Итераторы"

class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()
        return self.pointer


try:
    iter1 = Iterator(100, 110, 0)
    for i in iter1:         # цикл не будет выполнен, т.к. при step=0 произойдет переход к обработке исключения
        print(i, end=' ')
except StepValueError:
    print('Шаг не может равняться нулю')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)     # неправильные границы при шаге "1" по-умолчанию
for i in iter2:
    print(i, end=' ')   # -4 -3 -2 -1 0 1
print()
for i in iter3:
    print(i, end=' ')   # 8 10 12 14
print()
for i in iter4:
    print(i, end=' ')   # 4 3 2 1
print()
for i in iter5:         # произойдет выход из цикла при попытке первой итерации (без сообщения об ошибке)
    print(i, end=' ')
print()


