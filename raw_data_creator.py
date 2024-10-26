import random
from tools import write_array_to_file, create_array


def create_row_data():
    """
    Функция создает массивы от 10 000 до 100 000 элементов с шагом 10 000 для последующей обработки.
    Массивы хранятся в папке raw_data
    в папке correct хранятся массивы отсортированные от большего к меньшему
    в папке nearly хранятся массивы, где 90% элементов хранятся на сових местах
    в папке random хранятся массивы, где элементы рандомно перемешаны
    в папке reverse хранятся массивы, где элементы располагаются от большего к меньшему элементу
    """


    for i in range(1,11):
        lenght = i*10**4
        arr = [x for x in range(lenght)]
        write_array_to_file(arr, f"raw_data/correct/{lenght}.txt")

        random_arr = [random.randint(0, i*10**4) for _ in range(lenght)]
        write_array_to_file(random_arr, f"raw_data/random/{lenght}.txt")

        reverse_arr = [x for x in range(lenght-1, -1, -1)]
        write_array_to_file(reverse_arr, f"raw_data/reverse/{lenght}.txt")

        nearly_arr = create_array(lenght)
        write_array_to_file(nearly_arr, f"raw_data/nearly/{lenght}.txt")

    print("Массивы для сортировок созданы.")


