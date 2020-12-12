# Первая задача. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_int = 40
my_float = 80.5
my_str = "I love John Lennon"
my_list = ["John", "Paul", "Ringo", "George", 4]
my_tuple = ("love and peace")
my_set = ("McCartney")
my_dict = {"music": "love", "Love": "peace"}

#Способ первый, в котором я не очень уверена, потому что он слишком большой
all_types_list = [my_int, my_float, my_str, my_list, my_tuple, my_set, my_dict]
print(all_types_list[0])
print(all_types_list[1])
print(all_types_list[2])
print(all_types_list[3])
print(all_types_list[4])
print(all_types_list[5])
print(all_types_list[6])

# Способ 2, с for и in
for element in all_types_list:
    print(element)
    print(f"{type(element)}")

# Способ 3 его я не очень понимаю, но для эксперимента написала
for i in all_types_list:
    print(f"{i} is {type(i)}")

#мне кажется, что второй и третий получились похожими, потому что там где-то есть ошибка