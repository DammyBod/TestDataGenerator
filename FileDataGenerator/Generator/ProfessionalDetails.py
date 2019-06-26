from faker import Faker
global obj
obj = Faker()

def get_job():
    return obj.job()

def get_company():
    return obj.company()

def get_ascii_company_email():
    return obj.ascii_company_email()

def get_ascii_free_email():
    return obj.ascii_free_email()
