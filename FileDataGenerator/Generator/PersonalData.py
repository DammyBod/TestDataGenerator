from faker import Faker
global obj
obj = Faker()

# Fake :-  Personal details
def get_name():
    return obj.name()

def get_name_male():
    return obj.name_male()

def get_name_female():
    return obj.name_female()

def get_phone_number():
    return obj.phone_number()

def get_profile():
    return obj.profile(fields=None, sex=None)

def get_ssn():
    return obj.ssn(taxpayer_identification_number_type="SSN")

def get_ein():
    return obj.ein()

def get_itin():
    return obj.itin()