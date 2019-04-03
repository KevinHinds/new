"""
Replace the contents of this module docstring with your own details
Name: Kevin Hinds
Date started: 29/03/2019
GitHub URL:
"""
menu = """L - List places
   A - Add new place
   M - Mark a place as visited
   Q - Quit"""


def main():
    print("Travel Tracker 1.0 - by Kevin Hinds")
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("list")
        elif choice == "A":
            print("add")
        elif choice == "M":
            print("mark")
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>> ").upper()
# print("{} places saved to places.csv".format(total_number_places_visited) )
    print("Have a nice day :)")


main()
