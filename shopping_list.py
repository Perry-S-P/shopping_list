""" Scott Pete Perry, 09/09/2016
    This is a shopping list program that allows the user to read and write to a .csv file in python.
    https://github.com/Perry-S-P/shopping_list
"""
import csv


def main():
    loop = True
    while loop:
        print_menu()
        menu_choice = str(input())
        if menu_choice.lower() == 'r':
            print("Required Items:")
            list_items_required()
        elif menu_choice.lower() == 'c':
            print("Completed Items:")
            list_items_completed()
        elif menu_choice.lower() == 'm':
            list_items_required()
            mark_item_completed()
        elif menu_choice.lower() == 'a':
            add_item()
        elif menu_choice.lower() == 'q':
            loop = False
        else:
            input("Input Error! Enter any key to try again.")
    print("Program exiting")


def list_items_required():
    with open("items.csv") as file_object:
        reader = csv.DictReader(file_object, delimiter=',')
        line_count = 0
        for line in reader:
            if line["item_required"] == "r":
                line_count += 1
                print("{}.{}   ${}".format(line_count, line["item_name"], line["item_cost"]))
            else:
                print("There are no required items.")


def list_items_completed():
    with open("items.csv") as file_object:
        reader = csv.DictReader(file_object, delimiter=',')
        line_count = 0
        for line in reader:
            if line["item_completed"] == "c":
                line_count += 1
                print("{}.{}   ${}".format(line_count, line["item_name"], line["item_cost"]))
            else:
                print("There are no completed items.")


def mark_item_completed():
    line_count = 0
    marked_item = int(input("Enter the item number:"))
    with open("items.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        title = next(reader)  # title
        idx = title.index("item_required")

        lines = []
        for line in reader:
            if line[idx] == 'r':
                line_count += 1
                if marked_item == line_count:
                    line[idx] = 'x'
            lines.append(line)

    with open("items.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(title)
        writer.writerows(lines)


# user input to add new item to csv
def add_item():
    print("Item name:")
    item_name = str(input())
    print("Cost:")
    item_cost = float(input())
    print("Priority: 1, 2, or 3:")
    item_priority = int(input())
    add_item_list = [item_name, item_cost, item_priority, 'r']
    print(add_item_list)
    with open("items.csv", 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(add_item_list)


def print_menu():
    print("Menu:")
    print("R - List required items")
    print("C - List completed items")
    print("M - Mark an item as completed")
    print("A - Add new items")
    print("Q - Quit")
    print("Please select an option from above")


main()
