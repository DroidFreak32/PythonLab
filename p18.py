# p18.py
'''
Write the following function that tests whether the list has four consecutive numbers with the same value:
def isConsecutiveFour(values):
Write a test program that prompts the user to enter a series of integers and reports whether the series contains four consecutive numbers with the same value.
'''

def isConsecutiveFour(element_list):
    LENGTH = len(element_list)

    for i in range(LENGTH - 3):
        cur_ele = element_list[i]

        if element_list[i : i + 4] == [cur_ele, cur_ele, cur_ele, cur_ele]:
            return True

    return False


element_list = input("Enter list elements : ")
element_list = element_list.split(' ')
print("occurance of consecutive four in list : ", isConsecutiveFour(element_list))

#valid input : 1 2 2 2 2 3 4 (four consecutive 2s)
#invalid input : 1 2 3 4 5

#############################################
