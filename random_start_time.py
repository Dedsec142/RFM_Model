from random import randrange
from datetime import timedelta
from datetime import datetime


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


for i in range(1000):
    e1 = datetime.strptime('1/1/2015 1:30 PM', '%m/%d/%Y %I:%M %p')
    e2 = datetime.strptime('12/31/2017 4:50 AM', '%m/%d/%Y %I:%M %p')
    random_date(e1, e2)
