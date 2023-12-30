

def factorial(obj: int) -> int:
    factorial_num = obj
    if factorial_num <= 1:
        return 1
    return factorial(obj-1) * factorial_num

while True:
    print(factorial(int(input('Введите число для факториала \n'))))
    if str(input('Хотите продолжить? y/n \n')).lower() == 'n':
        exit()
