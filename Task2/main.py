from Property import *
from user import *
from booking import *
from host import *
from guest import *
property1 = Property(1, "Cozy Apartment", "New York", "A cozy apartment in downtown", 100, True)
property2 = Property(2, "Luxury Villa", "Los Angeles", "A luxurious villa with pool", 300, True)

host1 = Host(1, "John Doe", "john@example.com")
print(host1.list_property(property1))
print(host1.list_property(property2))

guest1 = Guest(1, "Alice Smith", "alice@example.com")
booking1 = guest1.book_property(property1, "2024-06-10", "2024-06-15")
print(booking1.cancel_booking())

print(property1.availability)