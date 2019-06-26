from configparser import ConfigParser

def take_file_name():
    name = input("Please enter your File name :- ")
    return name

def print_data_options():
    config = ConfigParser()
    config.read("../Configuration.cfg")
    print("Please enter your data columns- Enter more than 1 by using ,")
    for data in config.items('DataDetails'):
        print(data[0] + " =  " + (data[1].replace("_"," ").replace("get","").replace('()','')).capitalize())


def take_country_name():
    print("Please enter your country name-")
    print("United States")
    print("France")
    print("Canada")
    print("Gernmany")
    print("UK")
    countryName = input("Please enter your country : - ")
    return countryName

def take_number_of_records():
    count = (input("Please enter number of records : -  "))
    try:
        count = int(count)
    except:
        print("********* your number is incorrect ********")
        exit(0)
    return count


def take_column_details():
    dataname = input("Please enter your columns : - ")
    allColumns = dataname.split(",")
    for z in range (0, len(allColumns)):
        allColumns[z] = allColumns[z].strip()
    return allColumns
