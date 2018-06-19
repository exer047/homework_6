# количество элементов которые больше двух соседей


def more_then_neighbor(element_list):
    counter = 0
    for i in range(len(element_list)):
        if i == len(element_list) - 1:
            break
        elif element_list[i] > element_list[i - 1] and element_list[i] > element_list[i + 1]:
            counter += 1
    return counter

if __name__ == "__main__":
    element_list = [1, 3, 2, 4, 9, 6, 7]
    print(more_then_neighbor(element_list))