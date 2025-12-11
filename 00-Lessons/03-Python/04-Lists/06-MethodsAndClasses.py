listVar = [1, "Python", [list(range(5))], 3.14, True]
listVar_copy = listVar.copy() #using methods copy

print('Before modifying:')
print(f'listVar: {listVar}')
print(f'listVar_copy: {listVar_copy}')

listVar.append("New Element") #using methods append (add at the end of the list)

print('\nAfter modifying:')
print(f'listVar: {listVar}')
print(f'listVar_copy: {listVar_copy}')


listVar_number = list(range(5))  # [0, 1, 2, 3, 4]
print(f'Before modifying: {listVar_number}')

listVar_number.extend([5, 6 ,7]) # using methods extend
print(f'After extending: {listVar_number}')

languages = ['Python', 'R', 'Java', 'C++', 'JavaScript', 'java']
print(f'Original list: {languages}')
print(languages.index('Java'))  # using methods index (return the index of the first occurrence of the value)


print(languages.pop())  # using methods pop (removes the last item if index is not specified)
print(f'After pop: {languages}')
languages.pop(0) # using methods pop with index
print(f'After popping index 0: {languages}')

languages.remove('R')  # using methods remove (removes the first occurrence of the value)
print(f'After removing R: {languages}')

languages.sort()  # using methods sort (sorts the list in place)
print(f'After sorting: {languages}')

languages.sort(reverse=True)  # using methods sort with reverse parameter
print(f'After sorting in reverse: {languages}')

languages.sort(key=lambda x: x.lower())  # using methods sort with key parameter (case insensitive sort)
print(f'After case insensitive sorting: {languages}')

languages.sort(key= lambda x: len(x))  # using methods sort with key parameter (sort by length of string)
print(f'After sorting by length: {languages}')

languages.sort(key= lambda x: len(x), reverse=True)  # using methods sort with key and reverse parameter (sort by length of string in reverse)
print(f'After sorting by length in reverse: {languages}')

languages.reverse()  # using methods reverse (reverses the list in place)
print(f'After reversing: {languages}')

len(languages)  # using methods len (returns the number of items in the list)
print(f'Length of languages list: {len(languages)}')
print(f'Count of Java in languages list: {languages.count("Java")}')  # using methods count (returns the number of occurrences of a value)


sorted(languages, key=lambda x: len(x))  # using built-in function sorted (returns a new sorted list)
print(f'Original list after using sorted function: {languages}')
new_sorted_languages = sorted(languages, key=lambda x: len(x))
print(f'New sorted list by length: {new_sorted_languages}')
