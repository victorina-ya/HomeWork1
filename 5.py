my_list = [7, 5, 3, 3, 2]
new_n = int(input("Введите число"))
i = 0
for n in my_list:
    if new_n <= n:
        i += 1
my_list.insert(i, int(new_n))
print(my_list)

# Есть ли разница в данном случае между использованием int и float???????