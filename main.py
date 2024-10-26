from data_to_graph_translate import create_once_sort_plot, create_more_sort_plot
from raw_data_creator import create_row_data
from raw_data_processor import sort_all_arrays
from theory.theory_graphs import create_theory_graph

# Создаем теоретические графики и сохраняем их
create_theory_graph()

# Создаем массивы
create_row_data()

# Сортируем все массивы всеми сортировками, записывая время
sort_all_arrays()

#Создаем и сохраняем графики
create_once_sort_plot()
create_more_sort_plot()
