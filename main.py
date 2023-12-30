

def factorial(obj: int) -> int:
    factorial_num = obj
    if factorial_num <= 1:
        return 1
    return factorial(obj-1) * factorial_num


while True:
    number = int(input('Введите число для факториала \n'))
    result = factorial(number)
    print(f"Факторіал числа {number} дорівнює {result}")
    if str(input('Хотите продолжить? y/n \n')).lower() == 'n':
        exit()
