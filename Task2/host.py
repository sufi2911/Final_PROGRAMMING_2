from user import *

class Host(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.properties = []

    def list_property(self, property):
        self.properties.append(property)