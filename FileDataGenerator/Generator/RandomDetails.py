from faker import Faker
global obj
obj = Faker()

def get_color_name():
    return obj.color_name()

def get_random_digit():
    return obj.random_digit()

def get_null_value():
    return obj.null_value()

def get_date():
    return obj.date(pattern="%Y-%m-%d", end_datetime=None)
