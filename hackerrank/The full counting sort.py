# arr = [1,1,6,7]
# arr_index = [0]*(max(arr)+1)
# # print(arr_index)
# for i in arr:
#     arr_index[i] = arr_index[i]+1
# # print(arr_index)
# new_arr = []
# for index,val in enumerate(arr_index):
#     if val > 0:
#         new_arr.extend([index]*val)
# print(new_arr)