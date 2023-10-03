#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Bankomat:
    def __init__(self, number, actual_sum, min_sum, max_sum):
        self.number = number
        self.actual_sum = actual_sum
        self.min_sum = min_sum
        self.max_sum = max_sum

    def load_money(self, banknotes):
        for nominal, count in banknotes.items():
            self.actual_sum += nominal * count

    def get_money(self, summ):
        if self.min_sum <= summ <= self.max_sum:
            if self.actual_sum >= summ:
                self.actual_sum -= summ
                return "Деньги успешно сняты."
            else:
                return "Недостаточно средств в банкомате."
        else:
            return "Некорректная сумма снятия."

    def toString(self):
        nominals = [1000, 500, 100, 50, 10]
        counts = []
        for nominal in nominals:
            count = self.actual_sum // nominal
            counts.append(count)
            self.actual_sum -= nominal * count
        return f"В банкомате осталось:\n{counts[0]} купюр номиналом 1000\n{counts[1]} купюр номиналом 500\n{counts[2]} купюр номиналом 100\n{counts[3]} купюр номиналом 50\n{counts[4]} купюр номиналом 10"


if __name__ == "__main__":
    bankomat = Bankomat("1234", 10000, 100, 1000)
    print(bankomat.toString())

    banknotes = {1000: 5, 500: 10, 100: 20, 10: 50}
    bankomat.load_money(banknotes)
    print(bankomat.toString())

    summ = 500
    message = bankomat.get_money(summ)
    print(message)
    print(bankomat.toString())