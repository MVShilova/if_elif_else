print('Введите 3 числа: ')
first = int(input())
second = int(input())
third = int(input())
if first == second and second == third:
    print("3")
elif first or second == third:
    print("2")
else:
    print("0")