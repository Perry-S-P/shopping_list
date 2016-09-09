""" Scott Pete Perry, 09/09/2016
    This is a shopping list program that allows the user to read and write to a .csv file in python.
    https://github.com/Perry-S-P/shopping_list
"""
import csv


def list_items_required():
    with open("items.csv") as file_object:
        reader = csv.DictReader(file_object, delimiter=',')
        line_count = 0
        for line in reader:
            if line["item_required"] == "r":
                line_count += 1
                print("{}.{}   ${}".format(line_count, line["item_name"], line["item_cost"]))
            else:
                print("There are no completed items.")


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
            print("list of items. new line 1, new line 2")
        elif menu_choice.lower() == 'a':
            print("Item name:")
        elif menu_choice.lower() == 'q':
            loop = False
        else:
            input("Input Error! Enter any key to try again.")

    print("Program exiting")


def print_menu():
    print("Menu:")
    print("R - List required items")
    print("C - List completed items")
    print("M - Mark an item as completed")
    print("A - Add new items")
    print("Q - Quit")
    print("Please select an option from above")


main()