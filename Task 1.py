# Hotel Management System


rooms = []  # List for room details
allocations = {}  # Dictionary to manage room allocations

def display_menu():
    # For Displaying the main menu.
    print("\nWelcome to LANGHAM Hotel ")
    print("1. Add a Room")
    print("2. Delete a Room")
    print("3. Display all the Room Details")
    print("4. Allocate a Room")
    print("5. Display the Room Allocation Details")
    print("6. Billing & De-Allocation for the room")
    print("0. Exit the Application")

    
def add_room():
    # For Adding a new room to the list.
    try:
        room_number = input("Enter Room Number: ")
        if any(room['room_number'] == room_number for room in rooms):
            print("Room already exists.")
            return
        room_type = input("Enter Room Type (e.g., Deluxe, Suite): ")
        price = float(input("Enter Room Price: "))
        rooms.append({'room_number': room_number,'price': price, 'room_type': room_type })
        print("Room added successfully.")
    except ValueError:
        print("Invalid input. Please enter valid data.")

def delete_room():
    # For Deleting a room from the list.
    room_number = input("Enter Room Number to delete: ")
    global rooms
    rooms = [room for room in rooms if room['room_number'] != room_number]
    allocations.pop(room_number, None)
    print("Room deleted successfully.")

def display_rooms():
    # Displays information related to available rooms.
    if not rooms:
        print("No rooms available.")
        return
    print("\nRoom Details:")
    for room in rooms:
        print(f"Room Number: {room['room_number']}, Type: {room['room_type']}, Price: {room['price']}")

def allocate_room():
    # For Allocating a room to a customer.
    room_number = input("Enter Room Number to allocate: ")
    if room_number in allocations:
        print("Room is already allocated.")
        return
    customer_name = input("Enter Customer Name: ")
    allocations[room_number] = customer_name
    print(f"Room {room_number} allocated to {customer_name}.")

def display_allocations():
    # For Displaying allocation details.
    if not allocations:
        print("No rooms allocated.")
        return
    print("\nRoom Allocations:")
    for room_number, customer_name in allocations.items():
        print(f"Room Number: {room_number}, Allocated to: {customer_name}")

def billing_and_deallocation():
    # For Billing the customer and deallocating the room.
    room_number = input("Enter Room Number to bill and deallocate: ")
    if room_number not in allocations:
        print("Room is not allocated.")
        return
    customer_name = allocations.pop(room_number)
    room = next((room for room in rooms if room['room_number'] == room_number), None)
    if room:
        print(f"Billing Details for {customer_name}:")
        print(f"Room Number: {room_number}, Price: {room['price']}")
    print("Room deallocated.")


 
    
# For Main function to run the application.
def main():
    while  True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            choice = -1    
            if choice == 0:
                print("Exiting application. Goodbye!")
                break
            elif choice == 1:
                add_room()
            elif choice == 2:
                delete_room()
            elif choice == 3:
                display_rooms()
            elif choice == 4:
                allocate_room()
            elif choice == 5:
                display_allocations()
            elif choice == 6:
                billing_and_deallocation()
            else:
                print("Invalid choice. Please try again.")
        

            

if __name__ == "__main__":
    main()
