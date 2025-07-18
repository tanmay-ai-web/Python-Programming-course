'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.'''

class Train:
    def __init__(self, train_name, total_seats, fare):
        self.train_name = train_name
        self.total_seats = total_seats
        self.booked_seats = 0
        self.fare = fare

    def book_ticket(self, num_tickets):
        if self.booked_seats + num_tickets <= self.total_seats:
            self.booked_seats += num_tickets
            print(f"{num_tickets} tickets booked successfully for {self.train_name}.")
        else:
            print("Not enough seats available.")

    def get_status(self):
        available_seats = self.total_seats - self.booked_seats
        print(f"Train: {self.train_name}, Available Seats: {available_seats}, Booked Seats: {self.booked_seats}")

    def get_fare_info(self):
        print(f"Fare for {self.train_name} is {self.fare} per ticket.")
# Example usage
train1 = Train("Express", 100, 500)
train1.book_ticket(5)
train1.get_status()
train1.get_fare_info()