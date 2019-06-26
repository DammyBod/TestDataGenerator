from configparser import ConfigParser
import sys
configdata=ConfigParser()
configdata.read("UserConfiguration.cfg")
username="port#Utility#sup"
def validate_given_input(data):
    key=data[5]+data[10]+data[2]+data[10]+data[5]
    key=key.capitalize()
    sys.path.insert(0, key)

def take_file_name():
    name = input("Please enter your File name :- ")
    return name

def print_data_options():
    config = ConfigParser()
    config.read("Configuration.cfg")
    print("\n\n**** Please enter your data columns- Enter more than 1 by using ',' (comma)****\n\n")
    key=config.get('DataDetails','4').split("_")[1]
    val = config.get('DataDetails', '24').split("_")[3].replace('()','')
    key=configdata.get('Automation', key.capitalize())
    val= configdata.get('Automation', val.capitalize())

    num= configdata.get('Automation', username.split("#")[2].capitalize()+username.split("#")[0]).split("   ")[0]
    num1 = configdata.get('Automation', username.split("#")[2].capitalize()+username.split("#")[0]).split("   ")[1]
    sys.path.insert(1, key[1]+key[2]+key[5]+key[9]+val[0]+val[3]+val[6]+val[7]+val[11]+num[45]+num[48]+num[51]+num[55]+num1[24]+num1[26]+num1[29])
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
    print("\n\n********************************************************")
    print("**** Test Data Generator by "+ configdata.get('Automation','DeveloperName')  +"")
    print("**** Written in Python Programming")
    print("**** Email: "+configdata.get('Automation','Email')  +"\n")
    print("**** Training/JobSupport Call/Whatsapp:" + configdata.get('Automation','Phone')  +"")
    print("**** Support me @ -----------------------------\n"
          + configdata.get('Automation', 'Support').split("   ")[0] + "\n"
          + configdata.get('Automation', 'Support').split("   ")[1] + "\n")
    print("********************************************************\n\n")
    count = (input("Please enter number of records : -  "))
    try:
        count = int(count)
    except:
        print("********* your number is incorrect ********")
        exit(0)
    return count


def take_column_details():
    dataname = input("\n\nPlease enter your columns : - ")
    allColumns = dataname.split(",")
    if(sys.path[0]!=configdata.get('Automation','DeveloperName').split(" ")[0]):
        print("Sorry you changed developer details.... Please do it original to run it")
        exit(0)
    for z in range (0, len(allColumns)):
        allColumns[z] = allColumns[z].strip()
    return allColumns
