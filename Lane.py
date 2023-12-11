import time
import datetime
class Lane:
    def __init__(self,lane_type,status):
        self.lane_type = lane_type
        self.status = status
        self.timestamp = datetime.datetime.now()
        self.customer = []
    def add_customer_to_lane(self, custmoer):
        self.customer.append(custmoer)