# Imports the CSV file into Python
import csv


print("Shopping List 1.0 - by Scott Pete Perry")

with open('items.csv', "r") as f:
    reader = csv.reader(f, delimiter=",")
    data = list(reader)
    row_count = len(data)
print("{} items loaded from items.csv".format(row_count))


def print_menu():
    print("Menu:")
    print("R - List required items")
    print("C - List completed items")
    print("M - Mark and item as completed")
    print("A - Add new items")
    print("Q - Quit")
    print("Please select an option from above")

loop = True
while loop:
    print_menu()
    menu_choice = str(input())
    if menu_choice == 'r':
        print("Required Items:")
    elif menu_choice == 'c':
        print("Completed Items:")
    elif menu_choice == 'm':
        print("list of items. new line 1, new line 2")
    elif menu_choice == 'a':
        print("Item name:")
    elif menu_choice == 'q':
        loop = False
    else:
        input("Input Error! Enter any key to try again.")

print("Program exiting")









