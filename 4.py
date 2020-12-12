something_from_the_user = input("Введите, что вашей душе угодно, но только с пробелами, пожалуйста:").split()
for n, i in enumerate(something_from_the_user, 1):
    print(n, i) if len(i) <= 10 else print(n, i[:10])