import random

CAB_NAMES = {"1": "Auto", "2": "Sedan", "3": "SUV"}
CAB_RATES = {"1": 12, "2": 18, "3": 25}

ROUTES = {
    "1": ("Pune Station", "Shivajinagar", 5),
    "2": ("Swargate", "Kothrud", 8),
    "3": ("Hinjawadi", "Wakad", 10),
}

def book_ride():
    print("\n--- Choose Cab Type ---")
    print("1. Auto   (Rs. 12/km)")
    print("2. Sedan  (Rs. 18/km)")
    print("3. SUV    (Rs. 25/km)")
    cab_choice = input("Enter your choice (1-3): ").strip()

    if cab_choice not in CAB_NAMES:
        print("Invalid cab choice! Returning to main menu.")
        return

    cab_name = CAB_NAMES[cab_choice]
    rate = CAB_RATES[cab_choice]

    print("\n--- Choose Route ---")
    for number, (source, destination, distance) in ROUTES.items():
        print(f"{number}. {source} to {destination} ({distance} km)")
    route_choice = input("Enter route number (1-3): ").strip()

    if route_choice not in ROUTES:
        print("Invalid route choice! Returning to main menu.")
        return

    source, destination, distance = ROUTES[route_choice]

    fare = rate * distance
    print("\n========== Ride Summary ==========")
    print(f"Cab Type    : {cab_name}")
    print(f"Source      : {source}")
    print(f"Destination : {destination}")
    print(f"Distance    : {distance} km")
    print(f"Rate        : Rs. {rate}/km")
    print(f"Total Fare  : Rs. {distance} x {rate} = Rs. {fare}")
    print("==================================")

    print("\nYou can cancel the ride only BEFORE the OTP is shared.")
    print("1. Confirm & Share OTP")
    print("2. Cancel Ride")
    confirm = input("Enter your choice (1-2): ").strip()

    if confirm == "1":
        otp = random.randint(1000, 9999)  
        print(f"\nOTP shared with you: {otp}")
        print("NOTE: OTP has been shared. This ride can NO LONGER be cancelled.")
        print(f"Booking confirmed! Your {cab_name} from {source} to {destination} is on the way.")
    elif confirm == "2":
        print("\nRide cancelled. No OTP was shared. Returning to main menu.")
    else:
        print("\nInvalid choice! Booking not confirmed and no OTP shared. Returning to main menu.")


def main():
    print("Welcome to the Cab Booking Chatbot!")

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Book Ride")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            book_ride()
        elif choice == "2":
            print("Thank you for using the Cab Booking Chatbot. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()