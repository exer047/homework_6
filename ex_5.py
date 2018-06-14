# найти сумму и произведение элементов списка


element_list = [1, -5, 1, 3, -4]


def summ_and_composition(list):
    element_composition = 1
    element_summ = sum(list)
    for i in range(len(list)):
        element_composition *= list[i]
    return element_summ, element_composition


print(summ_and_composition(element_list))