
import matplotlib.pyplot as plot
import numpy as np

from constants import graph_colors, all_sorting_algorithms_rus_name, variations_rus
from tools import read_ready_data_from_file

def plot_graphs(parametrs, filename, regression_type=False):
    """
    Функция для построения графиков и сохранения их в отдельную папку.
    """
    title = None
    plot.figure()

    if parametrs[0][0] == parametrs[1][0]:
        title = all_sorting_algorithms_rus_name[parametrs[0][0]] + ". \nСравнение различных случаев."
        type_graph = "Сортировки"
    elif parametrs[0][1] == parametrs[1][1]:
        title = variations_rus[parametrs[0][1]] + ". \nСравнение различных сортировок."
        type_graph = "Массивы"

    for i in parametrs:
        dots = read_ready_data_from_file(i[0], i[1])
        x = [dot[0] for dot in dots]
        y = [dot[1] for dot in dots]
        print(i[0], i[1], parametrs[0][1] == parametrs[1][1])




        if regression_type:
            coefficients = np.polyfit(x, y, 2)
            polynomial = np.poly1d(coefficients)
            x_fit = np.linspace(min(x), max(x), 1000)
            y_fit = polynomial(x_fit)

            if type_graph == "Сортировки":
                label = variations_rus[i[1]]
                color = graph_colors[i[1]]
            elif type_graph == "Массивы":
                label = all_sorting_algorithms_rus_name[i[0]]
                color = graph_colors[i[0]]

            plot.plot(x_fit, y_fit, color=color, label=label)
        else:
            if type_graph == "Сортировки":
                label = variations_rus[i[1]]
                color = graph_colors[i[1]]
            elif type_graph == "Массивы":
                label = label = all_sorting_algorithms_rus_name[i[0]]
                color = graph_colors[i[0]]

            plot.plot(x, y, 'o', color=color)
            plot.plot(x, y, '-', color=color, label=label)

    plot.xlabel('n, количество элементов в массиве')
    plot.ylabel('t, время, затраченное на обработку массива')
    plot.grid(True)
    plot.legend()
    plot.title(title)

    plot.savefig(filename)
    # plot.show()
    plot.close()


def create_once_sort_plot():
    for i in [[True, "Регрессия"], [False, ""]]:
        for j in range(9):
            data = []
            for k in range(4):
                data.append([j, k])
            filename = f"experimental_graph/once_sorts/{all_sorting_algorithms_rus_name[j]} {i[1]}.png"
            plot_graphs(data, filename, i[0])

def create_more_sort_plot():
    data = []
    for i in range (9):
        data.append([i,2])
    filename = filename = f"experimental_graph/more_sorts/Все.png"
    plot_graphs(data, filename, True)

    filename = filename = f"experimental_graph/more_sorts/Логарифмические.png"
    plot_graphs([[3,2],[7,2],[8,2]], filename, True)

    quad = []

    for i in [0,1,2,4,5,6]:
        quad.append([i,2])
    filename = filename = f"experimental_graph/more_sorts/Квадратичные.png"
    plot_graphs(quad, filename, True)




