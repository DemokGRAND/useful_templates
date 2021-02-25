import numpy as np

stuff = {'a': (3,75),
         'b': (2,80),
         'c': (4,100),
         'd': (2,75),
         'e': (5,120)}
N = len(stuff)
def spilt_stuff(stuff): # функция для разделения словаря на отдельные составляющие
    area = [stuff[key][0] for key in stuff.keys()]
    value = [stuff[key][1] for key in stuff.keys()]
    keys = stuff.keys()
    return area,value,keys

def get_matrix(stuff, A = 9): # функция для формирования матрицы (динамической) A - количество свободного места


    matrix = np.zeros((N+1,A+1))
    for index in range(N + 1):
        for current_area in range(A + 1):

            if current_area == 0 or index == 0:
                matrix[index][current_area] = 0

            elif areas[index-1] <= current_area:
                matrix[index][current_area] = max(matrix[index-1][current_area],values[index-1] + matrix[index-1][current_area - areas[index-1]])
            else:
                matrix[index][current_area] = matrix[index-1][current_area]

    result = matrix[N][A] # максимальное значение, которые смогли вместить в рюкзак
    return matrix,result

def get_items(stuff, matrix, result, N, A):
    items =[]
    for index in range(N ,1,-1):
        if(result == matrix[index - 1][A]):
            continue
        if(result <= 0):
            break
        else:
            items.append((areas[index - 1],values[index - 1]))
            A -= areas[index - 1]
            result -= values[index - 1]

    return items

areas,values,keys = spilt_stuff(stuff)
matrix,result = get_matrix(stuff)
items_list = get_items(stuff,matrix,result,N,9)

selected_stuff = []

for search in items_list:
    for key, value in stuff.items():
        if value == search:
            selected_stuff.append(key)

print(selected_stuff)






