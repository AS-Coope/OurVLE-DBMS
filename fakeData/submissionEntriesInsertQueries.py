import csv

# stores each line from the csv file
eachLineList = []
necessaryNo = 1760131

submitYear = 2023
submitMonth = 5
submitDay = 20

'''
firstListCut = [:500000]
SecondListCut = [500000:1000000]
finalListCut = [1000000:1760131]
'''
# submissionentries format = spID, studID, itemSub, subDate, seID
# saving the new assignment names here
assignmentTag = "ASG"
assignmentList = []
assignmentDict = {} # Dictionary for assignments
count = 1 # used to ignore the headings in the csv files

# dictionary that stores assignment No's already saved to ensure no assignment for a course is duplicated

# opening the csv file to read from it
with open('student_enrollment.csv', mode = "r") as csvFile:
    studentEnrolCsvFile = csv.reader(csvFile)
    
    for line in studentEnrolCsvFile:
        #print(line)
        if count == 1:
            count += 1
            pass
        else:
            asgnName = f"{assignmentTag}{line[1]}_{line[2]}"
            asgnKey = line[1] + line[2]
            #print(asgnName)
            count += 1
            if asgnKey in assignmentDict:
                pass
            else:
                assignmentDict[asgnKey] = asgnName
                #assignmentList.append(asgnName)
            eachLineList.append(line)
    # this works, no need to print anymore, that takes up time
    # print(assignmentDict) # uncomment if you want to see the contents of the dictionary
csvFile.close() # we are done using the csv file to store the assignments in the dictionary


print("#############################################################")
################################ START OF INSERTING INTO SQL FILE ######################################
def submissionEntriesFirstFile():
    # opening sql file where queries will be inserted to write to it
    queryInserter = open('insertSubmissionEntries1.sql', 'w+')

    # opening the csv file to read from it
    with open('student_enrollment.csv', mode = "r") as csvFile:
        studentEnrollmentCsvFile = csv.reader(csvFile)

        #numRowsInStudentEnrollmentCsv = 0
        for line in studentEnrollmentCsvFile:
            #print(line)
            eachLineList.append(line)
            # numRowsInStudentEnrollmentCsv += 1
        # print(numRowsInStudentEnrollmentCsv) # this tells how many lines are in the student_enrollment.csv, currently 1760132


    # Inserting the queries into the sql file
    value = "INSERT INTO SubmissionEntries VALUES"
    queryInserter.write(value)
    currLine = 1
    seIDIncrementVal = 0
    courseAssignmentCheckDict = {} # this does a check to ensure that the same course assignment does not get put in an insert statement multiple times

    # do not need to have eachLineList[1:] because the heading was not added to eachLineList 
    for line in eachLineList:
        #print(line)
        
        currentCourseAssignment = line[1] + line[2]

        # This if-else statement is only necessary once currLine is to exceed 3899 lines
        #if currentCourseAssignment == 'CourseIDAssigmentNo':
         #   print(currentCourseAssignment, "got checked on current line:", currLine)
        #else:
            #print(currentCourseAssignment)
            #print(courseAssignmentCheckDict)
        if currLine != 499999:
            # given these aren't the last line in the query then they are separated by commas
            # value = "(" + '"' + assignmentDict[currentCourseAssignment] + '"' + ',' + "Assignment " + '"' + line[2].strip + '"' + ' for ' + '"' + line[1].strip + '"' + ',' + '"' + str(yearOfDate) + "-" + str(monthOfDate) + "-" + str(dayOfMonth) + '"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + "),\n"
            # NOTE: In relation to the database schema, the attrbiute name spID is equivalent to the value returned by assignmentDict[currentCourseAssignment]
            # value = "(" + '"' + assignmentDict[currentCourseAssignment] + '"' + ',' + '"' + line[0].strip() + '"' + ',' + '" "' + "),\n" # in case itemsubmit needs an empty string
            value = "(" + str(seIDIncrementVal) + ',' + line[0].strip() + ',' + '"SUBMITTED"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + str(seIDIncrementVal) + "),\n"
            #print(value)
            queryInserter.write(value)
            courseAssignmentCheckDict[currentCourseAssignment] = assignmentTag + currentCourseAssignment
        else:
            # ensures that the last line ends with a semi-colon (to complete the query) instead of a comma
            value = "(" + str(seIDIncrementVal) + ',' + line[0].strip() + ',' + '"SUBMITTED"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + str(seIDIncrementVal) + ");\n"  
            #print(value)
            queryInserter.write(value)
            courseAssignmentCheckDict[currentCourseAssignment] = assignmentTag + currentCourseAssignment
            #print('inside else', value, currLine)
            break
        currLine += 1
        seIDIncrementVal += 1
    #print(currLine)
        
    csvFile.close()
    queryInserter.close()

def submissionEntriesSecondFile():
    # opening sql file where queries will be inserted to write to it
    queryInserter = open('insertSubmissionEntries2.sql', 'w+')

    # opening the csv file to read from it
    with open('student_enrollment.csv', mode = "r") as csvFile:
        studentEnrollmentCsvFile = csv.reader(csvFile)

        #numRowsInStudentEnrollmentCsv = 0
        for line in studentEnrollmentCsvFile:
            #print(line)
            eachLineList.append(line)
            # numRowsInStudentEnrollmentCsv += 1
        # print(numRowsInStudentEnrollmentCsv) # this tells how many lines are in the student_enrollment.csv, currently 1760132


    # Inserting the queries into the sql file
    value = "INSERT INTO SubmissionEntries VALUES"
    queryInserter.write(value)
    currLine = 1
    seIDIncrementVal = 499999
    courseAssignmentCheckDict = {} # this does a check to ensure that the same course assignment does not get put in an insert statement multiple times

    # do not need to have eachLineList[1:] because the heading was not added to eachLineList 
    for line in eachLineList[499999:]:
        #print(line)
        
        currentCourseAssignment = line[1] + line[2]

        # This if-else statement is only necessary once currLine is to exceed 3899 lines
        #if currentCourseAssignment == 'CourseIDAssigmentNo':
         #   print(currentCourseAssignment, "got checked on current line:", currLine)
        #else:
            #print(currentCourseAssignment)
            #print(courseAssignmentCheckDict)
        if currLine != 500000:
            # given these aren't the last line in the query then they are separated by commas
            # value = "(" + '"' + assignmentDict[currentCourseAssignment] + '"' + ',' + "Assignment " + '"' + line[2].strip + '"' + ' for ' + '"' + line[1].strip + '"' + ',' + '"' + str(yearOfDate) + "-" + str(monthOfDate) + "-" + str(dayOfMonth) + '"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + "),\n"
            # NOTE: In relation to the database schema, the attrbiute name spID is equivalent to the value returned by assignmentDict[currentCourseAssignment]
            # value = "(" + '"' + assignmentDict[currentCourseAssignment] + '"' + ',' + '"' + line[0].strip() + '"' + ',' + '" "' + "),\n" # in case itemsubmit needs an empty string
            value = "(" + str(seIDIncrementVal) + ',' + line[0].strip() + ',' + '"SUBMITTED"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + str(seIDIncrementVal) + "),\n"
            #print(value)
            queryInserter.write(value)
            courseAssignmentCheckDict[currentCourseAssignment] = assignmentTag + currentCourseAssignment
        else:
            # ensures that the last line ends with a semi-colon (to complete the query) instead of a comma
            value = "(" + str(seIDIncrementVal) + ',' + line[0].strip() + ',' + '"SUBMITTED"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + str(seIDIncrementVal) + ");\n"  
            #print(value)
            queryInserter.write(value)
            courseAssignmentCheckDict[currentCourseAssignment] = assignmentTag + currentCourseAssignment
            #print('inside else', value, currLine)
            break
        currLine += 1
        seIDIncrementVal += 1
    #print(currLine)
        
    csvFile.close()
    queryInserter.close()

def submissionEntriesThirdFile():
    # opening sql file where queries will be inserted to write to it
    queryInserter = open('insertSubmissionEntries3.sql', 'w+')

    # opening the csv file to read from it
    with open('student_enrollment.csv', mode = "r") as csvFile:
        studentEnrollmentCsvFile = csv.reader(csvFile)

        #numRowsInStudentEnrollmentCsv = 0
        for line in studentEnrollmentCsvFile:
            #print(line)
            eachLineList.append(line)
            # numRowsInStudentEnrollmentCsv += 1
        # print(numRowsInStudentEnrollmentCsv) # this tells how many lines are in the student_enrollment.csv, currently 1760132


    # Inserting the queries into the sql file
    value = "INSERT INTO SubmissionEntries VALUES"
    queryInserter.write(value)
    currLine = 1
    seIDIncrementVal = 999999
    courseAssignmentCheckDict = {} # this does a check to ensure that the same course assignment does not get put in an insert statement multiple times

    # do not need to have eachLineList[1:] because the heading was not added to eachLineList 
    for line in eachLineList[999999:]:
        #print(line)
        
        currentCourseAssignment = line[1] + line[2]

        # This if-else statement is only necessary once currLine is to exceed 3899 lines
        #if currentCourseAssignment == 'CourseIDAssigmentNo':
         #   print(currentCourseAssignment, "got checked on current line:", currLine)
        #else:
            #print(currentCourseAssignment)
            #print(courseAssignmentCheckDict)
        if currLine != 760132:
            # given these aren't the last line in the query then they are separated by commas
            # value = "(" + '"' + assignmentDict[currentCourseAssignment] + '"' + ',' + "Assignment " + '"' + line[2].strip + '"' + ' for ' + '"' + line[1].strip + '"' + ',' + '"' + str(yearOfDate) + "-" + str(monthOfDate) + "-" + str(dayOfMonth) + '"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + "),\n"
            # NOTE: In relation to the database schema, the attrbiute name spID is equivalent to the value returned by assignmentDict[currentCourseAssignment]
            # value = "(" + '"' + assignmentDict[currentCourseAssignment] + '"' + ',' + '"' + line[0].strip() + '"' + ',' + '" "' + "),\n" # in case itemsubmit needs an empty string
            value = "(" + str(seIDIncrementVal) + ',' + line[0].strip() + ',' + '"SUBMITTED"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + str(seIDIncrementVal) + "),\n"
            #print(value)
            queryInserter.write(value)
            courseAssignmentCheckDict[currentCourseAssignment] = assignmentTag + currentCourseAssignment
        else:
            # ensures that the last line ends with a semi-colon (to complete the query) instead of a comma
            value = "(" + str(seIDIncrementVal) + ',' + line[0].strip() + ',' + '"SUBMITTED"' + ',' + '"' + str(submitYear) + "-" + str(submitMonth) + "-" + str(submitDay) + '"' + str(seIDIncrementVal) + ");\n"  
            #print(value)
            queryInserter.write(value)
            courseAssignmentCheckDict[currentCourseAssignment] = assignmentTag + currentCourseAssignment
            #print('inside else', value, currLine)
            break
        currLine += 1
        seIDIncrementVal += 1
    #print(currLine)
        
    csvFile.close()
    queryInserter.close()

def runAllSubmissionFiles():
    submissionEntriesFirstFile() # populates the first file
    submissionEntriesSecondFile() # populates the second file
    submissionEntriesThirdFile() # populates the third file

runAllSubmissionFiles()
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
