list1 = [4, 8, 1, 9, 5]
list2 = [1, 4, 2, 6, 7, 9]

sub_list = []

if len(list1) != len(list2):
    print('В списках разное количество элементов')
else:
    zip_object = zip(list1, list2)

    for list1_i, list2_i in zip_object:
        sub_list.append(list1_i - list2_i)

    print(sub_list)