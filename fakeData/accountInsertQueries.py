import csv
import hashlib
import datetime

# calculating the current date
theDate = datetime.datetime.now()
dayOfMonth = theDate.day
monthOfDate = theDate.month
yearOfDate = theDate.year

# carry out hashing for the passwords for every user
hasher = hashlib.new('sha256')
password = 'password'
hasher.update(password.encode())
hashedPass = hasher.hexdigest()

################################################ INSERTING ADMINS INTO TABLE NOW ################################################
# stores each line from the csv file
eachLineList = []

# opening sql file where queries will be inserted to write to it
queryInserter = open('insertAccount.sql', 'w+')

# opening the csv file to read from it
with open('admin_data.csv', mode = "r") as csvFile:
    adminCsvFile = csv.reader(csvFile)

    # Ensuring no null values are entered in the Profession column
    
    for line in adminCsvFile:
        #print(line)
        eachLineList.append(line)
    

# Inserting the queries into the sql file
value = "INSERT INTO Account VALUES"
queryInserter.write(value)
currLine = 1
for line in eachLineList[1:]:
    #print(line)
    if currLine != 101:
        # given these aren't the last line in the query then they are separated by commas
        value = "("+ '"' + line[1].strip() + '"' + ',' + '"' + line[2].strip() + '"' + ',' + '"' + line[3].strip() + '"' + ',' + '"' + line[4].strip() + '"' + ',' + '"' + line[5].strip() + '"' + ',' +'"' + hashedPass + '"' + ',' + '"' + str(yearOfDate) + "-" + str(monthOfDate) + "-" + str(dayOfMonth) + '"' + "),\n" 
        #print(value)
        queryInserter.write(value)
    else:
        break
    currLine += 1
    
csvFile.close()
queryInserter.close()

################################################ INSERTING STUDENTS INTO TABLE NOW ################################################
# stores each line from the csv file
eachLineList = []

# opening sql file where queries will be inserted to write to it
queryInserter = open('insertAccount.sql', 'a')

# opening the csv file to read from it
with open('student_data2.csv', mode = "r") as csvFile:
    studentCsvFile = csv.reader(csvFile)

    # Ensuring no null values are entered in the Profession column
    
    for line in studentCsvFile:
        #print(line)
        eachLineList.append(line)
    

# Inserting the queries into the sql file
# value = "INSERT INTO Account VALUES" 
# queryInserter.write(value)
currLine = 1
for line in eachLineList[1:]:
    #print(line)
    if currLine != 112501:
        # given these aren't the last line in the query then they are separated by commas
        value = "("+ '"' + line[1].strip() + '"' + ',' + '"' + line[2].strip() + '"' + ',' + '"' + line[3].strip() + '"' + ',' + '"' + line[4].strip() + '"' + ',' + '"' + line[5].strip() + '"' + ',' +'"' + hashedPass + '"' + ',' + '"' + str(yearOfDate) + "-" + str(monthOfDate) + "-" + str(dayOfMonth) + '"' + "),\n" 
        #print(value)
        queryInserter.write(value)
    else:
        break
    currLine += 1
    
csvFile.close()
queryInserter.close()

################################################ INSERTING LECTURERS INTO TABLE NOW ################################################
# stores each line from the csv file
eachLineList = []

# opening sql file where queries will be inserted to write to it
queryInserter = open('insertAccount.sql', 'a')

# opening the csv file to read from it
with open('lecturer_data2.csv', mode = "r") as csvFile:
    lecturerCsvFile = csv.reader(csvFile)

    # Ensuring no null values are entered in the Profession column
    
    for line in lecturerCsvFile:
        #print(line)
        eachLineList.append(line)
    

# Inserting the queries into the sql file
# value = "INSERT INTO Lecturer VALUES"
# queryInserter.write(value)
currLine = 1
for line in eachLineList[1:]:
    #print(line)
    if currLine != 1250:
        # given these aren't the last line in the query then they are separated by commas
        value = "("+ '"' + line[1].strip() + '"' + ',' + '"' + line[2].strip() + '"' + ',' + '"' + line[3].strip() + '"' + ',' + '"' + line[4].strip() + '"' + ',' + '"' + line[5].strip() + '"' + ',' +'"' + hashedPass + '"' + ',' + '"' + str(yearOfDate) + "-" + str(monthOfDate) + "-" + str(dayOfMonth) + '"' + "),\n" 
        #print(value)
        queryInserter.write(value)
    else:
        # ensures that the last line ends with a semi-colon (to complete the query) instead of a comma
        value = "("+ '"' + line[1].strip() + '"' + ',' + '"' + line[2].strip() + '"' + ',' + '"' + line[3].strip() + '"' + ',' + '"' + line[4].strip() + '"' + ',' + '"' + line[5].strip() + '"' + ',' +'"' + hashedPass + '"' + ',' + '"' + str(yearOfDate) + "-" + str(monthOfDate) + "-" + str(dayOfMonth) + '"' + ");\n" 
        #print(value)
        queryInserter.write(value)
        break
    currLine += 1
    
csvFile.close()
queryInserter.close()

"""
csvReader = open('Customers.csv')
queryInserter = open('insert.sql', 'w+')
lines = csvReader.readlines()
eachLineList = []
for line in lines[1:]:
    eachLineList.append([line])
    print(eachLineList)
    s= "INSERT INTO CUSTOMERS VALUES("+line.strip()+");\n"
    queryInserter.write(s)
csvReader.close()
queryInserter.close()
"""

