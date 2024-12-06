#File name "pyhtonassessment2"
# author- Sahaj Balguhar
# Description : Hotel management for Langham Hotels
# Dated 06/12/2024

import os
import time

# Global variables
rooms = []
allocations = []

# Function to display the main menu
def display_menu():
    print("\n--- Hotel Management Menu ---")
    print("1. Add Room")
    print("2. Delete Room")
    print("3. Display Room Details")
    print("4. Allocate Room")
    print("5. Display Room Allocation Details")
    print("6. Billing & De-Allocation")
    print("7. Save Room Allocation to File")
    print("8. Show Room Allocation from File")
    print("9. Backup Allocation Data")
    print("0. Exit")

# Function to add a room
def add_room():
    try:
        room_number = int(input("Enter room number: "))
        room_type = input("Enter room type (Single/Double/Suite): ")
        room_price = float(input("Enter room price: "))
        rooms.append({"Room Number": room_number, "Room Type": room_type, "Price": room_price})
        print("Room added successfully!")
    except ValueError as e:
        print(f"ValueError: {e} - Invalid input. Please enter correct values.")

# Function to delete a room
def delete_room():
    try:
        room_number = int(input("Enter room number to delete: "))
        for room in rooms:
            if room["Room Number"] == room_number:
                rooms.remove(room)
                print(f"Room {room_number} deleted successfully!")
                return
        print(f"Room {room_number} not found.")
    except ValueError as e:
        print(f"ValueError: {e} - Invalid input. Please enter a valid room number.")
    except IndexError as e:
        print(f"IndexError: {e} - The room number is out of the list bounds.")

# Function to display room details
def display_room_details():
    if rooms:
        for room in rooms:
            print(f"Room Number: {room['Room Number']}, Type: {room['Room Type']}, Price: {room['Price']}")
    else:
        print("No rooms available.")

# Function to allocate a room
def allocate_room():
    try:
        room_number = int(input("Enter room number to allocate: "))
        customer_name = input("Enter customer name: ")
        for room in rooms:
            if room["Room Number"] == room_number:
                allocations.append({"Room Number": room_number, "Customer Name": customer_name})
                print(f"Room {room_number} allocated to {customer_name}.")
                return
        print(f"Room {room_number} not available.")
    except ValueError as e:
        print(f"ValueError: {e} - Invalid input. Please enter correct values.")
    except TypeError as e:
        print(f"TypeError: {e} - Incorrect data type used for room allocation.")

# Function to display room allocation details
def display_room_allocation():
    if allocations:
        for allocation in allocations:
            print(f"Room {allocation['Room Number']} allocated to {allocation['Customer Name']}.")
    else:
        print("No rooms allocated.")

# Function to handle billing and de-allocation
def billing_and_deallocation():
    try:
        room_number = int(input("Enter room number to bill: "))
        for allocation in allocations:
            if allocation["Room Number"] == room_number:
                allocations.remove(allocation)
                print(f"Room {room_number} de-allocated successfully!")
                return
        print(f"Room {room_number} not allocated.")
    except ValueError as e:
        print(f"ValueError: {e} - Invalid input. Please enter correct values.")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e} - An attempt was made to divide by zero.")

# Function to save room allocation to a file
def save_room_allocation():
    try:
        with open("LHMS_Studentid850001645.txt", "w") as file:
            for allocation in allocations:
                file.write(f"Room {allocation['Room Number']} allocated to {allocation['Customer Name']}\n")
        print("Room allocation saved successfully to file.")
    except IOError as e:
        print(f"IOError: {e} - Error writing to the file.")

# Function to show room allocation from a file
def show_room_allocation():
    try:
        with open("LHMS_Studentid850001645.txt", "r") as file:
            print("Room Allocation from File:")
            for line in file:
                print(line.strip())
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e} - The file was not found. Please make sure the file exists.")
    except IOError as e:
        print(f"IOError: {e} - Error opening the file.")

# Function to backup room allocation data
def backup_allocation_data():
    try:
        backup_file_name = f"LHMS_Studentid850001645_Backup_{time.strftime('%Y%m%d_%H%M%S')}.txt"
        with open("LHMS_Studentid850001645.txt", "r") as file:
            content = file.read()
        with open(backup_file_name, "w") as backup_file:
            backup_file.write(content)
        with open("LHMS_Studentid850001645.txt", "w") as file:
            file.truncate(0)  # Clearing content of the original file
        print(f"Backup created successfully as {backup_file_name}. Original file cleared.")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e} - The file was not found. Backup could not be created.")
    except IOError as e:
        print(f"IOError: {e} - Error during backup operation.")
    except OverflowError as e:
        print(f"OverflowError: {e} - File size too large for backup.")

# Main function to control the flow of the program
def main():
    while True:
        try:
            display_menu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_room()
            elif choice == 2:
                delete_room()
            elif choice == 3:
                display_room_details()
            elif choice == 4:
                allocate_room()
            elif choice == 5:
                display_room_allocation()
            elif choice == 6:
                billing_and_deallocation()
            elif choice == 7:
                save_room_allocation()
            elif choice == 8:
                show_room_allocation()
            elif choice == 9:
                backup_allocation_data()
            elif choice == 0:
                print("Exiting application...")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError as e:
            print(f"ValueError: {e} - Invalid input. Please enter a number between 0 and 9.")
        except NameError as e:
            print(f"NameError: {e} - A variable was referenced before it was defined.")
        except IndexError as e:
            print(f"IndexError: {e} - Attempted to access an index outside the range.")
        except TypeError as e:
            print(f"TypeError: {e} - A function received an argument of an incorrect type.")
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e} - Division by zero occurred.")
        except SyntaxError as e:
            print(f"SyntaxError: {e} - There was an issue with the syntax in your code.")
        except ImportError as e:
            print(f"ImportError: {e} - A module import failed.")
        except EOFError as e:
            print(f"EOFError: {e} - End of file condition was reached unexpectedly.")
        except OverflowError as e:
            print(f"OverflowError: {e} - A calculation exceeded the numeric data type limits.")
        except IOError as e:
            print(f"IOError: {e} - There was an error with file input/output operations.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
