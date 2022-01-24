#Miłosz Błachowiak
def bubble_sort(unsorted_list: list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                swapped = True

    return unsorted_list
