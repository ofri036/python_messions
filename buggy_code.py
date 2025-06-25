list1 = [2, 4, 6, 8]
list2 = [10, 20, 30, 40]
the_list = list1 + list2

def sum_list(list):
    '''
    this function gets a list and sums it
    :parm list
    :type list
    :return: list
    :rtype: list
    '''
    sum = 0
    for number in the_list:
        sum += number
    return sum

def element_count(list) :
    '''
    this function gets a list and counts elements
    :parm list
    :type list
    :return: number of elements
    :rtype: int
    '''
    amount = 0
    for element in the_list:
        amount += 1
    return amount

def average_list():
    ''''
    this function gets the sum of the list,and the number of its elements, and averages it.
    :return: None
    '''
    the_average = sum_list(the_list) / element_count(the_list)
    print(f"the average is {the_average}")

def main():
    average_list()

if __name__ == '__main__':
    main()