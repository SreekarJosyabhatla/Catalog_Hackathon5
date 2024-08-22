from charging_station import ChargingStation
from booking_manager import list_stations, book_slot, cancel_booking

def initialize_stations():
    return [
        ChargingStation("S1", "Yendada", "Fast", 5, 2.5),
        ChargingStation("S2", "Car Shed", "Slow", 3, 5.0),
        ChargingStation("S3", "MVP Colony", "Fast", 2, 1.8),
    ]

def main():
    stations = initialize_stations()
    while True:
        print("\n1. List Stations")
        print("2. Book Slot")
        print("3. Cancel Booking")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_stations(stations)
        elif choice == "2":
            book_slot(stations)
        elif choice == "3":
            cancel_booking(stations)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
