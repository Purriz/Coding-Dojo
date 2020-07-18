# # Countdown - Create a function that accepts a number as an input. 
# # Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# # def countdown(num):

#     # nums_list = []
#     # for val in range(num, -1, -1):
#     #     print(val)
#     #     nums_list.append(val)
#     # return nums_list

# # print(countdown(12))
# # print(countdown(5))

# # [5,4,3,2,1,0]

# # Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

# # def print_and_return(nums_list):
# #     print(nums_list[0])
# #     return nums_list[1]

# # (print_and_return([10,12]))

# # def first_plus_length(nums_list):
# # get the first value first
# #     first_val = nums_list[0]
# # get the length of the list
# #     length_of_list = len(nums_list)
# # add them together
# #     return first_val + length_of_list
# # print(first_plus_length([1,2,3,4,5]))

# def values_greater_than_second(orig_list):
#     new_list = []
# #     # get the second value in the original list
# #     second_val = orig_list[1]
# #     # scan through the original list, find values greater than second value and add them to the new list
# #     for idx in range(0,len(orig_list)):
# #         if orig_list[idx] > second_val:
# #             new_list.append(orig_list[idx])
# #         print(len(new_list))
# #     return new_list
# #         # print(orig_list[idx])
# #     # print('########')
# #     # for val in orig_list:
# #         # print(val)
# # values_greater_than_second([5,2,3,2,1,4])

# def length_and_value(size,value):
#     new_list = []
#     for num_times in range(size):
#         new_list.append(value)
#     return new_list

# result = length_and_value(4,7)
# print(result)
# print(values_greater_than_second(result))