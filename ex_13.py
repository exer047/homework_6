# вывсети значения которые есть в обоих списках


def same_elements(list_1, list_2):
    new_list = []
    for i in list_1:
        for j in list_2:
            if i == j:
                new_list.append(i)
                break
    return new_list


if __name__ == "__main__":
    list_1 = [1, 3, 5, 8, "game", [1, 2], [2, 3], 4, 10]
    list_2 = [1, 2, 3, 4, "game", "name", [1, 2], [13, 0], 0]
    print(same_elements(list_1, list_2))