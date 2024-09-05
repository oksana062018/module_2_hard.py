x = int(input('Введите целое число от 3 до 20: '))
def get_password(number):
    password = ' '
    for i in range(1, number +1):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password


result = get_password(x)
print('Ваш пароль', result)