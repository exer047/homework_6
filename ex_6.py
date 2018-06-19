# найти все элементы, которые больше пред

element_list = [2, 3, 100, 4]


def more_then_last(element_list):
    for i in range(len(element_list)):
        if element_list[i] < element_list[i + 1]:
            return element_list[i + 1: len(element_list)]

print(more_then_last(element_list))