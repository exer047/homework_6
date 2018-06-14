# заменить элементы списка на противоположные


element_list = [1, -5, 0, 3, -4]


def convert_numbers(list):
    for i in range(len(list)):
        if list[i] != 0:
            list[i] = list[i] * -1
    return list


print(convert_numbers(element_list))