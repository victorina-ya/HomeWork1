month = int(input("Введите номер месяца:"))
my_l = ["Зима", "Весна", "Лето", "Осень"]
my_dict = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень", }
if month > 12 or month <= 0:
    print("Какойто-то странный месяц, я такого не знаю.")

if month == 1 or month == 12 or month == 2:
    print(my_dict.get(1))
if month == 3 or month == 4 or month == 5:
    print(my_dict.get(2))
if month == 6 or month == 7 or month == 8:
    print(my_dict.get(3))
if month == 9 or month == 10 or month == 11:
    print(my_dict.get(4))

# Я хотела сделать защиту, чтобы при введении числа меньше 0 или больше 12 выводилаcm снова строка ввода, но у меня не получилось это реализовать