# p17.py
'''
(Find the index of the smallest element) Write a function that returns the index of the smallest element in a list of integers. If the number of such elements is greater than 1, return the smallest index.
Use the following header: def indexOfSmallestElement(lst):
Write a test program that prompts the user to enter a list of numbers, invokes this function to return the index of the smallest element, and displays the index.
'''
def indexOfSmallestElement(lst):
    LENGTH = len(lst)
    small_element, small_index = lst[0], 0
    for i in range(LENGTH):
        if lst[i] < small_element:
            small_element = lst[i]
            small_index = i
    return small_index + 1

#test
element_list = input("Enter list items : ")
# Convert list elements to int
element_list = element_list.split(' ')
print(element_list)
element_list = list(map(int, element_list))
print("Index of smallest element : ", indexOfSmallestElement(element_list))

#############################################

