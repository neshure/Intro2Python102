
first_entry = input('enter the first word: ')
display1 = first_entry
first_entry = list(first_entry)
first_entry.sort()

second_entry = input('enter the second word: ')
display2 = second_entry
second_entry = list(second_entry)
second_entry.sort()


if first_entry != second_entry:
    print(f'{display1} and {display2} are NOT anagrams')

elif first_entry == second_entry:
    print(f'{display1} and {display2} are anagrams')

