#Proszę posortować podaną listę po drugim elemencie każdej listy, a w przypadku, kiedy są równe to po trzecim elemencie:

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]

def sortBySecondElement(element):
    return element[1]

def sortByThirdElement(element):
    return element[2]

print("Unsorted List:")
list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 0, 3]]
print(list_to_sort)

list_to_sort.sort(key=sortByThirdElement)
print("List sorted by the Third Element:")
print(list_to_sort)

list_to_sort.sort(key=sortBySecondElement)
print("List sorted by the Second Element:")
print(list_to_sort)
