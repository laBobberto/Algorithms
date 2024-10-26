#Здесь будут реализованы однотипные функции для лучшего, худшего, среднего случая, которые потом будут задействованы в построение графиков
import numpy
import numpy as np
import matplotlib.pyplot as plot




def selection_sort_best(n):
    return (n-1)*n/2
def selection_sort_av(n):
    return n*n/2
def selection_sort_worst(n):
    return (n+1)*n/2

def insertion_sort_best(n):
    return (n-1)*4
def insertion_sort_av(n):
    return (3*n**2+13*n-16)/4
def insertion_sort_worst(n):
    return (3*n**2+5*n-8)/2

def bubble_sort_best(n):
    return 2+n
def bubble_sort_av(n):
    return (3*n**2 + 5*n)/4
def bubble_sort_worst(n):
    return (3*n**2 + 1*n)/2

def merge_sort(n):
    return n+numpy.log2(n)

def shell_sort_best(n):
    return 2*numpy.log2(n) + 1/n -1
def shell_sort_av(n):
    return n**2 - n
def shell_sort_worst(n):
    return 2*(n**2 - n)

def quick_sort_best(n):
    return n*numpy.log2(n) + n
def quick_sort_av(n):
    return n*numpy.log2(n) + n
def quick_sort_worst(n):
    return n**2

def heap_sort(n):
    return n + n*numpy.log(n)

def all_graph_variations(func, name):
    x = np.linspace(1, 10, 400)
    y1 = func[0](x)
    y2 = func[1](x)
    y3 = func[2](x)


    plot.figure()
    plot.plot(x, y1, label='Лучший случай')
    plot.plot(x, y2, label='Средний случай')
    plot.plot(x, y3, label='Худший случай')
    plot.xlabel('Количество элементов')
    plot.ylabel('Количество операций')
    plot.title(f'График функции {name}')
    plot.legend()
    plot.grid(True)
    plot.savefig(f"{name}.png")

def all_graph_once_type(func, name):
    x = np.linspace(1, 1000_000, 4000)

    plot.figure()
    for i in func:
        y = i(x)
        func_name = str(i.__name__).split("_")
        plot.plot(x, y, label=func_name[0] + " " +func_name[1])

    plot.xlabel('Количество элементов')
    plot.ylabel('Количество операций')
    plot.title(f'{name}')
    plot.legend()
    plot.grid(True)
    plot.savefig(f"{name}.png")



def create_theory_graph():
    all_graph_variations([selection_sort_best, selection_sort_av, selection_sort_worst], "Selection sort")
    all_graph_variations([insertion_sort_best, insertion_sort_av, insertion_sort_worst], "Insertion sort")
    all_graph_variations([bubble_sort_best, bubble_sort_av, bubble_sort_worst], "Bubble sort")
    all_graph_variations([merge_sort, merge_sort, merge_sort], "Merge sort")
    all_graph_variations([shell_sort_best, shell_sort_av, selection_sort_worst], "Shell sort")
    all_graph_variations([quick_sort_best, quick_sort_av, quick_sort_worst], "Quick sort")
    all_graph_variations([heap_sort, heap_sort, heap_sort], "Heap sort")

    all_graph_once_type(
        [selection_sort_av, insertion_sort_av, bubble_sort_av, merge_sort, shell_sort_av, quick_sort_av, quick_sort_av,
         heap_sort],
        "Средний случай для всех сортировок")
    all_graph_once_type([selection_sort_av, insertion_sort_av, bubble_sort_av, shell_sort_av],
                        "Средний случай для сортировок с квадратичной асимптотикой")
    all_graph_once_type([merge_sort, quick_sort_av, heap_sort],
                        "Средний случай для сортировок с логарифмической асимптотикой")