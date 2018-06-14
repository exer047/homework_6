# найти номер и значение положительного элемента списка


element_list = [-1, -2, 3, -5, -5, -6, -2, 11]


def number(list):
    for i in range(len(list)):
        if list[i] > 0:
            print(i, list[i])
            break



number(element_list)
