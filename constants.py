from all_sorts.bubble_sort import bubble_sort
from all_sorts.heap_sort import heap_sort
from all_sorts.insertion_sort import insertion_sort
from all_sorts.merge_sort import merge_sort
from all_sorts.quick_sort import quick_sort
from all_sorts.selection_sort import selection_sort
from all_sorts.shell_sort import shell_sort
from all_sorts.shell_sort_hibbard import shell_sort_hibbard
from all_sorts.shell_sort_pratt import shell_sort_pratt

all_sorting_algorithms = [selection_sort, insertion_sort, bubble_sort, merge_sort, shell_sort, shell_sort_hibbard, shell_sort_pratt, quick_sort, heap_sort]
all_sorting_algorithms_rus_name = ["Сортировка выбором", "Сортировка вставками", "Пузырьковая сортировка", "Сортировка слиянием", "Сортировка Шелла", "Сортировка Шелла (Хиббард)", "Сортировка Шелла (Пратт)", "Быстрая сортировка", "Пирамидальная сортировка"]

variations = ["correct", "nearly", "random", "reverse"]
variations_rus = ["Отсортированный массив", "Частично отсортированный массив", "Массив со случайными элементами", "Массив с элементами в обратном порядке"]

graph_colors = [
    'blue',        # Синий
    'green',       # Зеленый
    'red',         # Красный
    'cyan',        # Голубой
    'magenta',     # Пурпурный
    'yellow',      # Желтый
    'black',       # Черный
    'orange',      # Оранжевый
    'purple'       # Фиолетовый
]
