#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Para:
    def __init__(self, first, second):
        if isinstance(first, float) and isinstance(second, float):
            self.first = first
            self.second = second
        else:
            print("Ошибка! Значения полей должны быть дробными числами.")

    def read(self):
        self.first = float(input("Введите значение первого поля: "))
        self.second = float(input("Введите значение второго поля: "))

    def display(self):
        print("Значение первого поля:", self.first)
        print("Значение второго поля:", self.second)

    def root(self):
        if self.second != 0:
            return -self.first / self.second
        else:
            print("Ошибка! Коэффициент В не может быть равен нулю.")


def make_para(first, second):
    return Para(first, second)


if __name__ == "__main__":
    para = make_para(2.5, 3.5)
    para.display()

    rootv = para.root()
    if rootv is not None:
        print("Корень линейного уравнения:", rootv)

    para.read()
    para.display()

    rootv = para.root()
    if rootv is not None:
        print("Корень линейного уравнения:", rootv)