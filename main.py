import math


def main():
    a = input("Введите A = ")
    b = input("Введите B = ")
    x = input("Введите X = ")
    y = 0

    try:
        a = float(a)
        b = float(b)
        x = float(x)
        y = float(y)

        if math.isnan(a) or math.isnan(b) or math.isnan(x) or math.isinf(a) or math.isinf(b) or math.isinf(x):
            print("Ошибка!!! Введено слишком большое число")
        else:
            if (x >= 5):
                y = (5 * (a * a + b * b)) / (x - 4)
            else:
                y = 6 * a * b - 5 * x
            if (math.isnan(y)):
                print("Нет решения")
            elif (math.isinf(y)):
                print("Бесконечность")
            else:
                print("y = %.1f" % y)
                # print(y)

    except ValueError:
        if a.isalpha():
            print("Ошибка!!! Буквы нельзя вводить")
        else:
            print("Ошибка!!! Введены непонятные символы")


if __name__ == '__main__':
    main()
