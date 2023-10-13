#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Bancomat:
    def __init__(self, number, maxs, mins):
        self.banknotes = {"10": 0, "100": 0, "500": 0, "1000": 0}
        self.number = number
        self.maxs = maxs
        self.mins = mins

    @property
    def total_sum(self):
        total = 0
        for nominals, count in self.banknotes.items():
            total += int(nominals) * count
        return total

    def LoadMoney(self, taple):
        for nominal, count in taple.items():
            self.banknotes[nominal] += count
        print("Остаток в банкомате: ", self.total_sum)

    def GetMoney(self, sum_tuple):
        if (
            self.total_sum >= self.CheckSum(sum_tuple) >= self.mins
            and self.CheckSum(sum_tuple) <= self.maxs
        ):
            for nominal, count in sum_tuple.items():
                self.banknotes[nominal] -= count
            print("Остаток в банкомате:", self.total_sum)
        else:
            print("Error!")

    def CheckSum(self, tuple):
        total = 0
        for nominals, count in tuple.items():
            total += int(nominals) * count
        return total


if __name__ == "__main__":
    obj = Bancomat("123", 1000, 100)
    summ = {"10": 1, "1000": 1, "500": 20}
    obj.LoadMoney(summ)
    print(obj.banknotes)
    summ = {"10": 1, "1000": 0, "500": 1}
    obj.GetMoney(summ)
    print(obj.banknotes)
