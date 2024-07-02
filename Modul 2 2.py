First = int(input('Введите первое число: '))
Second = int(input('Введите второе число: '))
Third = int(input('Введите третье число: '))
print('Ваши числа:', First, ',', Second, ',', Third)

if First == Second and Second == Third:
    print(3)
elif First == Second or Second == Third or First == Third:
    print(2)
else:
    print(0)