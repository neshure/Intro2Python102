def remove_all(numbers, target):
    for items in target:
        print([numbers])
        numbers.remove(items)
        print(items)
        print(numbers)
        break
   



numbers = [2, 3, 4]
target = [2]
remove_all(numbers, target)