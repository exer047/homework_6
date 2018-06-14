# найти в списке максимальный и минимальный элементы и поменять их местами


element_list = [1, -5, 0, 3, -4]


def swap_minmax(list):
    maximal = max(list)
    minimal = min(list
    for i in range(len(list)):
        if list[i] == max(list):
            list[i] = minimal
        elif list[i] == min(list):
            list[i] = maximal
    return list


print(swap_minmax(element_list))