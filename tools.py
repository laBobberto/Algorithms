import random
import time
from constants import variations, all_sorting_algorithms, all_sorting_algorithms_rus_name, variations_rus


def write_array_to_file(array, filename):
    """
    Функция записи данных в файл
    """
    with open(filename, 'w') as file:
        for i in array:
            file.write("%s\n" % i)
    file.close()

def read_array_from_file(filename):
    """
    Функция чтения данных из файла
    """
    array = []
    with open(filename, 'r') as file:
        for line in file:
            array.append(int(line.strip()))
    file.close()
    return array

def create_array(n):
    """
    Функция создает массив, где 90% элементов на сових местах
    """
    array = list(range(n))

    shuffle_count = int(0.05 * n)

    for _ in range(shuffle_count):
        i, j = random.sample(range(n), 2)
        array[i], array[j] = array[j], array[i]

    return array

def reading_working_time(sort, arr, func_name, data_print):
    """
    Считываем время работы сортировки, выводит в консоль информацию, если data_print true
    """
    timer = time.time()
    sort(arr)
    timer = time.time() - timer

    if data_print: print(func_name, timer)
    return timer

def read_ready_data_from_file(sort_type, array_type):
    """
    Функция чтения готовых данных из файла
    """
    filename = f"ready_data/{all_sorting_algorithms[sort_type].__name__}.txt"
    array = []
    data_find = False
    num = 0
    with open(filename, 'r') as file:
        for line in file:
            if line == variations[array_type] + "\n":
                data_find = True
                continue

            if data_find:
                num += 1
                array.append([num * 10 ** 4, float(line)])
            if num == 10:
                file.close()
                return array
        print(f"Ошибка чтения данных. {all_sorting_algorithms_rus_name[sort_type]}, {variations_rus[array_type]}")
        file.close()
        return 0






