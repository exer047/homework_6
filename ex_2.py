# найти сумму положительных элементов списка


element_list = [-1, -2, 3, 5, -5, -6, -2, 11]


def positive_summ(list):
    numbers_summ = 0
    for i in range(len(list)):
        if list[i] > 0:
            positive = list[i]
            numbers_summ += positive
    return numbers_summ


print(positive_summ(element_list))
