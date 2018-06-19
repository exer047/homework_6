# удалить все повторяющиеся элементы


def delete_repeats(element_list):
    new_list = []
    for i in element_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    element_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 7, "game", "game"]
    print(delete_repeats(element_list))


