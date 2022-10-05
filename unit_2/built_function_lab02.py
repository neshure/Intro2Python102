# def sum(numbers):
#     added_value = 0
# #     for num in numbers:
# #         num_val = int(num)
# #         added_value = added_value + num_val
# #     return added_value

# # aggregated_number = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]
# # print()
# # print(f'Numbers: {aggregated_number}')
# # print()
# print(f'Sum: {sum(aggregated_number)}')



def GetUserInput():
    user_input =""
    entered_list =[]
    while user_input !="Done":
        user_input = input("Enter number to be added: ")
        if(user_input=="Done"):
            break
        converted_value= int(user_input)
        entered_list.append(converted_value)
    return entered_list

list = GetUserInput()
print(f'sum: {sum(list)}')
