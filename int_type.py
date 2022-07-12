# def sort(unsort_list):
#     loop_number = len(unsort_list)
#
#     for compare_index in range(loop_number):
#         compare_value = unsort_list[compare_index]
#         prev_position = compare_index - 1
#
#         if prev_position >= 0 and unsort_list[prev_position] >= compare_value:
#             unsort_list[prev_position + 1] = unsort_list[prev_position]
#         prev_position = prev_position - 1
#     return unsort_list
#
# test_arr = [5, 3, 1, 6, 7, 13]
# print(sort(test_arr))

# dict = {}
# dict['네이버'] = 'https://www.naver.com/'
# dict['다음'] = 'https://www.daum.net/'
# dict['구글'] = 'https://www.google.com/'
# dict.pop('네이버')
# print(dict)


# def func_1():
#     global test_data
#     test_data = 7
# func_1()
# print(test_data)

# str_data = 'python programming'
# cap_str_data = str_data.capitalize()
# print(cap_str_data)

def value_list(list_1):
    result_value = list_1[0]
    result_list_value = list_2[0]
    for list_test in list_1:
        if list_test < result_list_value:
            result_list_value = list_test
    return result_list_value

list_1 = [1, 55, 23, 2]
list_2 = [4, 24, 78, 6, 21]

print("first value in list_1 is ", value_list(list_1))
print("second value in list_2 is ", value_list(list_2))