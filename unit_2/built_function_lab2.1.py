def sum(numbers):
    added_value = 0
    for num in numbers:
        num_val = int(num)
        added_value = added_value + num_val
    return added_value




num = []

while True:
    entries = input("Enter a number or 'done' to quit: ")
    if entries.lower() == 'done':
        print('Goodbye')
        break
    elif entries.lower() != 'done':
            num.append(entries)


print(f'Sum: {sum(num)}')







