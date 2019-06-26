import os
import sys
module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from  FileOperations import SaveFile
from  Generator import AddressDetails
from  Generator import CredeitCardDetails
from  Generator import PersonalData
from  Generator import ProfessionalDetails
from  Generator import RandomDetails
from  Generator import SystemDetails
from UserInteraction import TakeInput
from configparser import ConfigParser
import time

# *********************Configurable Data ******************************** #
config = ConfigParser()
config.read("Configuration.cfg")
configmethod = ConfigParser()
configmethod.read("MethodMapping.cfg")
configdata = ConfigParser()
configdata.read("UserConfiguration.cfg")
automation=configdata.get('Automation','Logic')
TakeInput.validate_given_input(automation)
# *********************Take number of records****************************#
count= TakeInput.take_number_of_records()

#  Take File Name from User
filename= TakeInput.take_file_name()

#  Connect with File
SaveFile.connect_with_file(filename)

#  Take Column Data
TakeInput.print_data_options()

start = time.perf_counter()

allColumns = TakeInput.take_column_details()
columnCount=len(allColumns)
counter=0
if(configdata.get('Automation','Key')!=sys.path[1]):
    print("Sorry.... you changed develper details")
    time.sleep(5)
    exit(0)

for j in allColumns:
    counter=counter+1
    try:
        methodName = config.get('DataDetails',str(j))
        methodName = str(methodName).replace("get_","").replace("()","")
    except:
        print("********* ALERT -  Column number is incorrect *******")
        exit(0)
    methodName = methodName.capitalize()
    SaveFile.writeDatatoFile(methodName)
    if(counter!=columnCount):
       SaveFile.addLineSeperator()
SaveFile.switchline()
SaveFile.saveFile()

for i in range(1,count+1):
    counter = 0
    for j in allColumns:
        counter = counter + 1
        try:
           methodName = config.get('DataDetails',str(j))
           methodName=configmethod.get('DataDetails',methodName)
        except:
           print("********* ALERT -  Column number is incorrect *******")
           exit(0)
        result=eval(methodName)
        SaveFile.writeDatatoFile(result)
        if (counter != columnCount):
            SaveFile.addLineSeperator()
    SaveFile.switchline()
SaveFile.saveFile()
SaveFile.closeFile()
print("Time Taken by Script(in seconds) : - "+ str(time.perf_counter() - start))
print( "**************Thanks for using this utility **************************")

time.sleep(10)
