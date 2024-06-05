class Booking:
    def __init__(self, property, guest, check_in_date, check_out_date):
        self.booking_id = None  # Generate a unique booking ID
        self.property = property
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = "confirmed"

    def cancel_booking(self):
        self.status = "canceled"
