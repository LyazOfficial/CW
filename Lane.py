import time
import datetime
import Customer


class Lane:
    def __init__(self, lane_type):
        self.lane_type = lane_type
        self.status = "Closed"
        self.timestamp = datetime.datetime.now()
        self.customer = []

    def add_customer_to_lane(self, customer):
        self.customer.append(customer)


class RegularLane(Lane):
    def __init__(self):
        super().__init__("Regular")
        self.till = 1


class SelfServiceLane(Lane):
    def __init__(self):
        super().__init__("SelfService")
        self.till = 8


Lane1 = RegularLane()
print(Lane1)

Lane2 = SelfServiceLane()
print(Lane2)


