
class Flight:
    def __init__(self, code, source, destination, seats, fare):
        self.code = code
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare


class Passenger:
    def __init__(self, name, age, ptype):
        self.name = name
        self.age = age
        self.ptype = ptype

    def get_discount(self):
        if self.ptype == "student":
            return 10
        return 0


class FlightBooking:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PH303", "Pune", "Hyderabad", 15, 3000)
        ]
        self.booking = None

    def view_flights(self):
        for f in self.flights:
            print(f.code, f.source, "to", f.destination,
                  "Seats:", f.seats, "Fare:", f.fare)

    def book_flight(self):
        code = input("Enter flight code: ")

        flight = None
        for f in self.flights:
            if f.code == code:
                flight = f

        if flight is None:
            print("Invalid flight code")
            return

        name = input("Enter passenger name: ")

        try:
            age = int(input("Enter age: "))
            ptype = input("Enter passenger type (student/regular): ").lower()
            tickets = int(input("Enter number of tickets: "))

            if name.strip() == "" or age <= 0 or tickets <= 0:
                print("Invalid passenger details")
                return

            if ptype not in ["student", "regular"]:
                print("Invalid passenger type")
                return

            if tickets > flight.seats:
                print("Not enough seats available")
                return

            passenger = Passenger(name, age, ptype)

            subtotal = flight.fare * tickets
            discount = subtotal * passenger.get_discount() / 100
            total = subtotal - discount

            flight.seats -= tickets

            self.booking = {
                "id": "BK1001",
                "flight": flight,
                "passenger": passenger,
                "tickets": tickets,
                "subtotal": subtotal,
                "discount": discount,
                "total": total
            }

            print("\nBooking Confirmed!")
            self.view_booking()

        except ValueError:
            print("Please enter valid numbers")

    def view_booking(self):
        if self.booking is None:
            print("No booking found")
            return

        b = self.booking
        print("Booking ID:", b["id"])
        print("Passenger:", b["passenger"].name)
        print("Age:", b["passenger"].age)
        print("Flight:", b["flight"].source, "to", b["flight"].destination)
        print("Tickets:", b["tickets"])
        print("Subtotal:", b["subtotal"])
        print("Discount:", b["discount"])
        print("Total Fare:", b["total"])

    def run(self):
        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.view_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you! Goodbye!")
                break
            else:
                print("Invalid choice")


app = FlightBooking()
app.run()

