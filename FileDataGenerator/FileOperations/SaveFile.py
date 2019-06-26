import os
def connect_with_file(filename):
    global file
    path=os.path.dirname(os.path.abspath(__file__))
    path=path.replace("FileOperations","").replace("\FileDataGenerator","")
    print(path+filename+".txt")
    file = open(path+filename+".txt", 'w')

def writeDatatoFile(data):
    file.write(str(data))

def switchline():
    file.write("\n")

def addLineSeperator():
    file.write(",")

def saveFile():
    file.flush()

def closeFile():
    file.close()