
import math

def powerSum(total, power, num):
    value = total - math.pow(num, power)

    if value < 0:
        return 0
    elif value == 0:
        return 1
    else:
        return powerSum(value, power, num+1) + powerSum(total, power, num+1)

if __name__ == '__main__':
    # total = int(input())
    # power = int(input())
    total = 100
    power = 2

    result = powerSum(total, power, 1)

    print(result)