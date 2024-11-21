
def are_equal(list1, list2):
    return list1 == list2

list1 = [int(x) for x in input("Enter elements of first list separated by space: ").split()]
list2 = [int(x) for x in input("Enter elements of second list separated by space: ").split()]

print("The lists are equal." if are_equal(list1, list2) else "The lists are not equal.")

