#!/usr/bin/python3
import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5

    result_add = calculator_1.add(a, b)
    result_sub = calculator_1.sub(a, b)
    result_mul = calculator_1.mul(a, b)
    result_div = calculator_1.div(a, b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))
