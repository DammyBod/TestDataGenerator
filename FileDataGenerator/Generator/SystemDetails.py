from faker import Faker
global obj
obj = Faker()

def get_firefox():
    return obj.firefox()

def get_chrome():
    return obj.chrome(version_from=13, version_to=63, build_from=800, build_to=899)

def get_internet_explorer():
    return obj.internet_explorer()

def get_linux_processor():
    return obj.linux_processor()