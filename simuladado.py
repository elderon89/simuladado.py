import random


def res():
    return random.randint(1, 6)


def repete(n):
    x1 = x2 = x3 = x4 = x5 = x6 = 0
    for val in range(n):
        x = res()

        if(x == 1):
            x1 += 1
        elif(x == 2):
            x2 += 1
        elif(x == 3):
            x3 += 1
        elif(x == 4):
            x4 += 1
        elif(x == 5):
            x5 += 1
        else:
            x6 += 1

    print("Número 1 saiu ", x1, " vezes = ", (x1/n)*100, "%")
    print("Número 2 saiu ", x2, " vezes = ", (x2/n)*100, "%")
    print("Número 3 saiu ", x3, " vezes = ", (x3/n)*100, "%")
    print("Número 4 saiu ", x4, " vezes = ", (x4/n)*100, "%")
    print("Número 5 saiu ", x5, " vezes = ", (x5/n)*100, "%")
    print("Número 6 saiu ", x6, " vezes = ", (x6/n)*100, "%")


def menu():
    n = int(input('\nQuantos lançamentos de dado você deseja realizar? R: '))
    repete(n)


while True:
    menu()
