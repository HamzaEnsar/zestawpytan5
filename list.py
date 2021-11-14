list1 = [6, 2, 5, 4, 1, 3]
list2 = [1, 2, 5, "a"]
list3 = []
list4 = [3.2, 4.5, 5]
list5 = [3.2, 4.5, 5, "adfs"]
list6 = [2, 3]


def validate_list(array):
    try:
        assert len(array) != 0, 'error nie ma '

        for i in range(0, len(array)):
            if (not isinstance(array[i], int)) and (not isinstance(array[i], float)):
                raise ValueError('string error')

        array.sort()
        min_array = array[0]
        max_array = array[-1]
        sum_array = sum(array)
        tuple1 = (min_array, max_array, sum_array)
        print(tuple1)

    except AssertionError:
        print('nie ma liczb')
    except ValueError:
        print('string error')


validate_list(list1)
