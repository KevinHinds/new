"""
Replace the contents of this module docstring with your own details
Name: Kevin Hinds
Date started: 29/03/2019
GitHub URL:
"""


MENU = """L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""

in_file = open("temp.csv", 'r')


def main():
    places = in_file.readlines()
    print("Travel Tracker 1.0 - by Kevin Hinds")
    count = 0
    for i in places:
        count += 1
    print("{} places loaded from places.csv".format(count))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            for place in places:
                print(place)
        elif choice == "A":
            new_place = input("Name: ")
            while new_place == "":
                print("Input can not be blank")
                new_place = input("Name: ")
            new_country = input("Country: ")
            while new_country == "":
                print("Input can not be blank")
                new_country = input("Name: ")
            finished = False
            while not finished:
                try:
                    new_priority = int(input("Priority: "))
                    finished = True
                except ValueError:
                    print("Please enter a valid integer.")
            while new_priority <= 0:
                print("Number must be > 0")
                new_priority = int(input("Priority: "))
            print("{} in {} (priority {}) added to Travel Tracker".format(new_place, new_country, new_priority))
            new_entry = [new_place, new_country, new_priority, "n"]
            print(new_entry)
            places.extend(new_entry)
            print(places)
        elif choice == "M":
            print("mark")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    # print("{} places saved to places.csv".format(total_number_places_visited) )
    print("Have a nice day :)")






main()
