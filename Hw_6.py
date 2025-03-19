def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a
numbers = [20, 30, 10, 2, 3, 0, -10, -1000]
print(bubble_sort(numbers))


def  binary_search(list, value):
    n = len(list)
    ResultOk = False
    first = 0
    last = n - 1
    pos = None

    while first < last:
        middle = (first + last) // 2
        if value == list[middle]:
            first = middle
            last = first
            ResultOk = True
            pos = middle
        else:
            if value > list[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if ResultOk == True:
        print('Элемент найден')
        return pos


    else:
        print('Элемент не найден')


index = binary_search([12,34,56,90,100,500,600,700], 500)
print(f'Элемент в списке имеет индекс {index}!')

