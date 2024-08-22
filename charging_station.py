class ChargingStation:
    def __init__(self, station_id, location, charger_type, total_slots, distance):
        self.station_id = station_id
        self.location = location
        self.charger_type = charger_type
        self.total_slots = total_slots
        self.available_slots = total_slots
        self.distance = distance  # Distance from user's location
        self.bookings = []

    def book_slot(self, user_id):
        if self.available_slots > 0:
            self.available_slots -= 1
            booking_id = f"{self.station_id}_{len(self.bookings) + 1}"
            self.bookings.append((booking_id, user_id))
            print(f"Slot booked successfully! Booking ID: {booking_id}")
        else:
            print("No slots available!")

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking[0] == booking_id:
                self.bookings.remove(booking)
                self.available_slots += 1
                print(f"Booking {booking_id} canceled successfully!")
                return
        print("Booking ID not found.")

    def __str__(self):
        return (f"[{self.station_id}] {self.location} - {self.charger_type} Charger | "
                f"Distance: {self.distance} km | Available Slots: {self.available_slots}/{self.total_slots}")
