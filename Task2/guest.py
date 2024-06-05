from user import *
from booking import *
class Guest(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.bookings = []

    def book_property(self, property, check_in_date, check_out_date):
        if property.availability:
            booking = Booking("Rose Cotage","New York","A cozy apartment in downtown", 100)
            self.bookings.append(booking)
            property.availability = False
            return booking
        else:
            print("Property is not available for booking.")