
from tools import reading_working_time, read_array_from_file
from constants import variations, all_sorting_algorithms

def sort_all_arrays():
    """
    Функция запускает все сортировки на заранее созданных массивах
    """
    for i in all_sorting_algorithms:

        file = open(f"ready_data/{i.__name__}.txt", "w", encoding="UTF-8")

        for j in range(4):
            file.write(variations[j] + "\n")
            for k in range(1, 11):
                length = k * 10 ** 4
                arr = read_array_from_file(f"raw_data/{variations[j]}/{length}.txt")
                file.write(f"{reading_working_time(i, arr, i.__name__, False)}\n")
        file.close()
