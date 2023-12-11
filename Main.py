import random
import time
import Lane
import Custmoer
t = "Open"
if t == "Open":
    custmor_pool = []
    for i in range(random.randint(0,10)):
        custmor_pool.append(random.randint(0,30))
    lane1 = Lane.Lane("Regular","Open")
    for i in custmor_pool:
        lane1.add_customer_to_lane(i)
    