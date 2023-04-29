import csv

# stores each line from the csv file
eachLineList = []

# opening sql file where queries will be inserted to write to it
queryInserter = open('insertCourseOfStud.sql', 'w+')

# opening the csv file to read from it
with open('student_courses.csv', mode = "r") as csvFile:
    courseOfStudCsvFile = csv.reader(csvFile)

    # Ensuring no null values are entered in the Profession column
    
    for line in courseOfStudCsvFile:
        #print(line)
        eachLineList.append(line)
    

# Inserting the queries into the sql file
value = "INSERT INTO CourseOfStud VALUES"
queryInserter.write(value)
currLine = 1
for line in eachLineList[1:]:
    #print(line)
    if currLine != 506773:
        # given these aren't the last line in the query then they are separated by commas
        value = "("+line[0].strip() + ',' + '"' + line[1].strip() + '"' + "),\n" 
        #print(value)
        queryInserter.write(value)
    else:
        # ensures that the last line ends with a semi-colon (to complete the query) instead of a comma
        value = "("+line[0].strip() + ',' + '"' + line[1].strip() + '"' + ");\n" 
        #print(value)
        queryInserter.write(value)
        
        break # the table repeats itself after line 1250th tuple
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
