# p11.py
'''
Write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
'''

def binary_search(sorted_list, search_item):
    lower, upper = 0, len(sorted_list)
    while lower <= upper:
        mid_index = (lower + upper) // 2 # // will only retuen int after division
        mid_item = sorted_list[mid_index]
        if search_item == mid_item:
            return mid_index + 1
        if mid_item > search_item:
            upper = mid_index - 1
        else:
            lower = mid_index + 1
    return -1

sorted_list = input("Enter list items [in sorted order] : ")
search_item = int(input("Enter the element to search : "))
sorted_list = sorted_list.split(' ')
sorted_list = list(map(int, sorted_list))   # converts elements from string to integers
result = binary_search(sorted_list, search_item)
if result is -1:
    print("Element not found")
else:
    print(search_item, "found at position ", result)

#############################################
