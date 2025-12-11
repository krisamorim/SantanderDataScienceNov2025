import sys
choice = input("\nRun loop? (y/n): ").strip().lower()
if choice == 'y':
    print('\nWhithout "continue"')
for i in range(5):
    if choice == 'y':
        print(f"Iteration {i+1}: Loop is running.")
    else:
        print("Loop not executed.")
        break


if choice != 'y':
    sys.exit()
print("\nWith 'continue'(skip number 3)")
for i in range(5):
    if choice == 'y':
        if i == 2:
            continue #<---- Using continue to skip iteration when i equals 2        
    print(f"Iteration {i+1}: Loop is running.")