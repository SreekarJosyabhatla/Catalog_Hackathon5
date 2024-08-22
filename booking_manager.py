def list_stations(stations):
    sorted_stations = sorted(stations, key=lambda station: station.distance)
    print("\nAvailable Charging Stations:")
    for station in sorted_stations:
        print(station)
    print("\n")

def book_slot(stations):
    station_id = input("Enter Station ID: ")
    user_id = input("Enter User ID: ")
    for station in stations:
        if station.station_id == station_id:
            station.book_slot(user_id)
            break
    else:
        print("Station not found.")

def cancel_booking(stations):
    booking_id = input("Enter Booking ID: ")
    for station in stations:
        station.cancel_booking(booking_id)
