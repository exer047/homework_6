# удалить все четные элементы


def delete_even_i(element_list):
    new_list = []
    for i in range(len(element_list)):
        if (i + 1) % 2 != 0:
            new_list.append(element_list[i])
    return new_list

if __name__ == "__main__":
    element_list = [1, 2, 3, 4, 5, 6, 7, "game", "game"]
    print(delete_even_i(element_list))
