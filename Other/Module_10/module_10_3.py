# Домашнее задание по теме "Блокировки и обработка ошибок"

import random
import time
import threading


class Bank:
    """Класс для симуляции операций с банковским счетом, используя операции пополнения и снятия как отдельные потоки"""

    _balance: int = 0            # Текущий баланс счета
    _lock = threading.Lock()     # Объект-замок для блокировки потоков
    _max_operations: int = 100   # Максимальное количество успешных транзакций, отдельно для каждого вида
                                    # операций (пополнения, снятия)
    _pause: float = 0.01         # значение задержки в секундах для имитации времени выполнения операций
    _deposit_is_finished = False    # флаг об окончании пополнений, нужен для устранения deadlock-а

    # Метод совершает 100 транзакций пополнения средств
    def deposit(self):
        for i in range(self._max_operations):
            increment = random.randint(50, 500)
            self._balance += increment
            print(f'Пополнение №{i+1}: {increment}. Баланс: {self._balance}')
            time.sleep(self._pause)
            if self._balance >= 500 and self._lock.locked():
                self._lock.release()
        self._deposit_is_finished = True

    # Метод совершает 100 попыток снятия средств
    def take(self):
        for i in range(self._max_operations):
            decrement = random.randint(50, 500)
            print(f'Запрос №{i+1} на {decrement}')
            if decrement > self._balance:
                print('Запрос отклонён, недостаточно средств')
                time.sleep(self._pause)
                if not self._deposit_is_finished:  # Устанавливать блокировку можно только, если депозиты
                    self._lock.acquire()           # не закончились, иначе это приведет к deadlock
            else:
                self._balance -= decrement
                print(f'Снятие: {decrement}. Баланс: {self._balance}')
                time.sleep(self._pause)


bk = Bank()
# Т.к. методы Bank.deposit и Bank.take принимают self,
# в потоки в качестве аргумента нужно передать сам объект bk класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk._balance}')