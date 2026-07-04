seats = [0]*10
print("Hello! Welcome to our seat booking program. \n")

def CheckAvailableSeat(arr):
    for i in range (len(arr)):
        if(arr[i]==0):
            print("Seat no.",i+1,"Available")
        else:
            print("Seat no.",i+1,"Not Available")
    print("\n")
        
def BookSeat(arr):
    seat = int(input("Enter the seat no. that you want to book(1-10): "))

    if seat < 1 or seat > len(arr):
        print("Invalid seat number!")
        return
    print("\n")
    if (arr[seat-1]==1):
        print("Sorry this seat is not available.")
    else:
        print("Congratulations!, Seat no.",seat,"has been booked for you. ")
        print("Enjoy your day :)\n")
        arr[seat-1]=1

def Cancel_seat(arr):
    cancelseat = int(input("Enter the seat no. that you want to cancel: "))
    print("\n")
    if(arr[cancelseat-1]==0):
        print("This seat has already vacant. ")
    else:
        print("Your seat has canceled and no refund will be granted :( ")
        arr[cancelseat-1]=0
    print("\n")

while(1):
    print("Type 1 for Checking Available seats. \nType 2 to book any seat. \nType 3 to cancel your seat. \nType 4 to exit. ")
    value = int(input("What do you want? "))
    print("\n")
    match value:
        case 1:
            CheckAvailableSeat(seats)
        case 2:
            BookSeat(seats)
        case 3:
            Cancel_seat(seats)
        case 4:
            print("----Exiting the program----\n")
            break
        case _:
            print("Invalid choice\n")

        