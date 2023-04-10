from faker import Faker
import random
import csv

fake = Faker()

""" Generate unique Student first,middle and last names lists """
sFns = [fake.unique.first_name() for i in range(250)]
sMns = [fake.unique.first_name_nonbinary() for i in range(500)]
sLns = [fake.unique.last_name() for i in range(450)]

""" Generate unique Lecturer first,middle and last names lists """
lFns = [fake.unique.first_name() for i in range(25)]
lMns = [fake.unique.first_name_nonbinary() for i in range(50)]
lLns = [fake.unique.last_name() for i in range(50)]

""" Generate unique Admin first,middle and last names  list """
aFuName = [fake.unique.first_name() +" "+fake.first_name_nonbinary()+" " +fake.unique.last_name() for i in range(100)]




""" lists for  courses and course codes """
cNames = ["Algebra","Geometry","Content and Pedagogy for Selected Topics in Mathematics","Psychological Issues in the Classroom","Introduction to Teaching and Learning","Introduction To Curriculum Studies","Action Research for School and Classroom Managers","Orientation to Guidance and Counselling","The Nature Of History","The Teaching Of Literature","The Language-Structure Content Of English Teaching","Learner Processes, Teacher Processes & the Development of Literacy","Introductory Calculus","Analytical Geometry and Trigonometry","The Nature and Scope of Mathematics","Analysis & Teaching of Math","Classroom Testing & Evaluation (Basic)","Probability & Statistics","Motivation and the Teacher","Research Design in Education","Enquiry Methods in Teaching Social Studies","Practice in Planning Learning Experiences for Social Studies","Introduction To Computer Technology in Education","Art and Drama in Education","Management Of Human Resources & Interpersonal Relations","School and Classroom Management A","Principles & Practices of School Finance","Fieldwork/Practicum (Educational Administration)","The Study","Teaching History in Secondary Schools","Methodologies for Teaching Info Technology & Computer Science","Instructional Website Design, Development & Integration into Curriculum","Literature for Children in the Primary School","Content and Pedagogy for CXC English Language A","Teaching the Structure of English","Advanced Study Of Assessment Of Literacy","Investigations and Problem Solving","Linear Algebra","Abstract Algebra","Report","Sociology of Science Teaching and Learning","Introduction To Secondary Science Practicals","Secondary Schools Social Studies Research and Selection","Teaching Geography in the Caribbean Classroom","Educational Technology","Culminating school-based experience: Clinical Practice","Pre-Practicum","Field Study","Content and Pedagogy for Selected Topics in Mathematics","Planning for Teaching and Learning","Introduction To Educational Administration","Local and Community Studies","Issues in Information Technology","Educational Software Design and Development","Teaching in a Networked Environment","Assessing Information Technology","Language Structure Content Of English Teaching in the Caribbean","Text, Analysis Of Discourse And The Acquisition Of Literacy","Research Perspectives in the Study of Literacy","Children Learning Mathematics","Discrete Mathematics","Issues and Perspectives in Education","Teaching Methodologies in Science","Introduction to the Learner in Difficulty","Basic Geographic Skills for the Social Studies Teacher","Special Problems in School Administration","School and Classroom Management B","The Study","Assessment of Achievement in History","Selecting Methods & Resources for Instruction in Caribbean and World History","The Teaching of English Literature in the Secondary School","Content and Pedagogy for CXC English Language A","Writing in the Secondary School","Teaching Caribbean Poetry","Advanced Study Of Assessment Of Literacy","Writing as Literacy Development in the Primary School","Calculus II","Assessing Mathematics Learning","Classroom Testing and Evaluation Advance","Teaching Mathematics in Grades 10 and 11","Research Methods (II)","Report","Assessment in Science Teaching","Environmental Education","Science Teaching and the History of Science","The Role Of Soc. Studies/Geo. In Secondary Education","Intro to Computing I","Intro to Computing II","Object-oriented Programming","Math for Computing","Computing and Society","Discrete Mathematics for Computer Science","Analysis of Algorithms","Digital Logic Design","Software Engineering","Object Technology","Net-Centric Computing","Computer Organisation","Operating Systems","Introduction to Artificial Intelligence","Database Management Systems","Language Processors","Theory of Computation","Real-Time Embedded Systems","Group Project","Internship in Computing I","Internship in Computing II","Computer Systems Administration","Information Systems in Organisations","Computer & Network Security for IT","Database Management Systems","User Interface Design for IT","Dynamic Web Development II","e-Commerce","Requirement Engineering","Software Project Management","Software Modeling","Software Testing","Software Reliability and Formal Methods","Capstone Project (Software Engineering)"," Numerical Methods for Differential Equations"," Multivariate Statistical Analysis"," Introduction of Stochastic Processes"," The Analysis of Time Series"," The Analysis of Time Series"," Mechanics of Interacting Particles"," A Course in Algebraic Number Theory"," A course in the History of Mathematics"," Differential Geometry"," Differential Equations"," Complex Analysis and Applications","Principles of Economics I","Mathematics for Social Sciences I","Mathematics for Social Sciences II","Introduction to Statistics","Principles of Economics II","Intermediate Microeconomics I","Intermediate Microeconomics II","Intermediate Macroeconomics I","Intermediate Macroeconomics II","Social & Economic Accounting","Statistical Methods I","Statistical Methods II","Statistical Computing","Sampling Methods for Business and Social Sciences","Matrix Algebra for Business and Social Sciences","Calculus Social Sciences","Caribbean Economy","International Economic Relations I","International Economic Relations II","Economics of Sport","Game theory","Monetary Theory and Policy","International Trade Theory & Policy","International Finance","History of Economic Thought","Finance & Development","Economics of Financial Institutions","Public Finance I","Selected Topics in Economics","Probability and Distribution Theory for Business & Social Sciences","Statistical Estimation and Inference","Environmental Economics","Operations Research I","Non-Parametric Statistics","Econometrics","Applied Econometrics","Development Economics","Financial Markets","Credit Analysis and Lending"," Introductory Linear Algebra & Analytic Geometry"," Calculus I"," Calculus II"," Introduction to Formal Mathematics"," Elements of Mathematical Analysis"," A First Course in Linear Algebra"," Introduction to Probability Theory"," Introduction to Abstract Algebra"," Multivariable Calculus"," Ordinary Differential Equations"," Complex Variables"," Advanced Linear Algebra"," A course on Metric Spaces & Topology"," Research Project"," Regression Analysis"," Some Topics in Functional Analyses"," Introduction to the Theory of Integration"," Advanced Abstract Algebra"," Introduction to Differential Geometry with Maple"," Time Series","Selected Topics in Operations Research"," Partial Differential Equations"," Mathematical Modelling"," Numerical Methods","Electrical Circuits","Mechanics","Waves, Optics and Thermodynamics","Electricity and Magnetism","Modern Physics","Physics for Engineers","Introduction to Engineering","Electrical Circuit Analysis And Devices","Mathematics for Scientists and Engineers","Practices in Basic Electronics","Engineering Science and Technology","Introduction to Programming","Engineering Circuit Analysis and Devices","Radiation Biology and Protection","Biomedical Statistics and Informatics","Basic Medical Electronics and Instrumentation","Fundamentals of Radiation Physics and Dosimetry","Physics of the Human Body","Anatomy and Physiology for Medical Physicists","Radiation Safety and Protection","Radiation Therapy 2: Physics, Equipment and Applications","Radiation Therapy 1: Physics, Equipment and Applications","Radiation Biology","Biomedical Statistics","Information Technology and Equipment in Radiation Medicine","Fundamentals of Clinical Radiation Physics and Dosimetry","Anatomy and Physiology for Clinical Medical Physicists","Diagnostic Radiology Physics, Equipment and Applications","Nuclear Medicine: Physics, Equipment and Applications","Non-Ionization Radiation: Physics, Equipment and Applications","Computer Applications in Physics","Practices in Electronics Designs 1","Practices in Basic Electronics 2","Signals and Systems","Electric Circuit Analysis","Communication Systems","Analysis and Designs of Analog Circuits","Digital Electronics and Systems","Embedded Systems","Introduction to Semiconductor Devices","Fundamentals of Materials Science","Fluid Dynamics","Physics of the Human Body","Practices in Medical Physics 1","Electromagnetism and Optics","Quantum Mechanics and Nuclear Physics","General Physics Lab 1","Fluid Dynamics and Environmental Physics Laboratory","Materials Science Laboratory 1","Speech Processing","Microprocessors and Computer Architecture","Fundamentals of Energy Statistics","Essentials of Renewable Energy Technologies and Solutions","Energy Information Management","Non-Ionization Radiation: Physics, Equipment and Applications","Nuclear Medicine: Physics, Equipment and Applications"]
cCodes = ["EDMC1001","EDMC1002","EDME1103","EDPS1003","EDTL1020","EDCU2013","EDEA2305","EDGC2010","EDHE2912","EDLA2103","EDLA2106","EDLS2605","EDMC2201","EDMC2203","EDMC2214","EDMC2216","EDME2006","EDME2202","EDPS2003","EDRS2007","EDSS2903","EDSS2904","EDTK2025","EDAR3808","EDEA3304","EDEA3306","EDEA3308","EDEA3316","EDEA3320","EDHE3905","EDIT3818","EDIT3822","EDLA3104","EDLA3106","EDLA3109","EDLS3603","EDMA3206","EDMC3201","EDMC3204","EDRS3019","EDSC3410","EDSC3417","EDSS3903","EDSS3911","EDTK3004","EDTL3018","EDTL3020","EDTL3021","EDME1103","EDTL1021","EDEA2304","EDHE2908","EDIT3017","EDIT3821","EDIT3823","EDIT3825","EDLA2105","EDLS2606","EDLS2607","EDMC2213","EDME2204","EDPH2024","EDSC2407","EDSE2712","EDSS2906","EDEA3305","EDEA3307","EDEA3320","EDHE3904","EDHE3908","EDLA3103","EDLA3106","EDLA3110","EDLA3111","EDLS3603","EDLS3612","EDMC3020","EDMC3202","EDME3006","EDME3205","EDRS3008","EDRS3019","EDSC3403","EDSC3408","EDSC3411","EDSS3908","COMP1126","COMP1127","COMP1161","COMP1210","COMP1220","COMP2201","COMP2211","COMP2120","COMP2140","COMP2171","COMP2190","COMP2340","COMP3101","COMP3220","COMP3161","COMP3652","COMP3702","COMP3801","COMP3901","COMP3911","COMP3912","INFO3105","INFO3110","INFO3155","COMP3161","INFO3170","INFO3180","INFO3435","SWEN2165","SWEN3130","SWEN3145","SWEN3165","SWEN3185","SWEN3920","MATH6623","STAT6632","STAT6630","STAT6631","STAT6631","MATH6629","MATH6633","MATH6634","MATH6628","MATH6622","MATH6635","ECON1000","ECON1003","ECON1004","ECON1005","ECON1012","ECON2000","ECON2001","ECON2002","ECON2003","ECON2005","ECON2008","ECON2009","ECON2010","ECON2014","ECON2015","ECON2016","ECON2020","ECON2023","ECON2024","ECON2025","ECON3003","ECON3005","ECON3006","ECON3007","ECON3008","ECON3010","ECON3011","ECON3016","ECON3030","ECON3031","ECON3032","ECON3034","ECON3037","ECON3040","ECON3049","ECON3050","ECON3051","ECON3072","ECON3073","MATH1141","MATH1142","MATH1151","MATH1152","MATH2401","MATH2410","MATH2404","MATH2411","MATH2403","MATH2420","MATH3155","MATH3412","MATH3402","MATH3423","STAT3001","MATH3403","MATH3401","MATH3411","MATH3404","STAT3002","MATH3414","MATH3421","MATH3422","MATH3424","ECNG1000","PHYS1411","PHYS1412","PHYS1421","PHYS1422","ELNG1101","ENGR1000","ELET1500","MATH1185","ELET1405","ECNG1012","ECNG1009","ECSE1102","MDPH6160","MDPH6150","MDPH6140","MDPH6130","MDPH6120","MDPH6110","MDPH6280","MDPH6270","MDPH6260","MDPH6190","MDPH6180","MDPH6170","MDPH6135","MDPH6115","MDPH6215","MDPH6230","MDPH6240","PHYS2396","ELET2405","ELET2415","ELET2460","ELET2470","ELET2480","ELET2410","ELET2530","ELET2450","ELET2420","PHYS2561","PHYS2671","PHYS2296","PHYS2200","PHYS2386","PHYS2351","PHYS2300","PHYS2600","PHYS2500","ELET2210","ELET2570","PHYS2000","PHYS2701","PHYS3000","MDPH6240","MDPH6230"]


""" Dictionary to join course code to course name """
course_dict = {cCodes[i]: cNames[i] for i in range(len(cCodes))}


departments = ["Department of Computing", "Department of Mathematics", "Department of Physics", "Department of Economics", "School of Education"]
dID = [1000,1001,1002,1003,1004]

""" Dictionary to join departmentID to Department name """
dept_dict = {dID[i]: departments[i] for i in range(len(dID))}

#Createing Course Information file
with open('Course_data.csv', 'w',newline='') as csvfile0:
    writer0 = csv.writer(csvfile0)
    writer0.writerow(['CourseCode','CourseName','DepartmentID'])
    for i in range(len(cCodes)):
        if cCodes[i][:2]=='ED':
            writer0.writerow([cCodes[i],cNames[i],dID[4]])
        if cCodes[i][:4]=='COMP' or cCodes[i][:4]=='SWEN' or cCodes[i][:4]=='INFO':
            writer0.writerow([cCodes[i],cNames[i],dID[0]])
        if cCodes[i][:4]=='MATH' or cCodes[i][:4]=='STAT':
            writer0.writerow([cCodes[i],cNames[i],dID[1]])
        if cCodes[i][:4]=='ECON':
            writer0.writerow([cCodes[i],cNames[i],dID[3]])
        if cCodes[i][:4]=='PHYS' or cCodes[i][:4]=='MDPH' or cCodes[i][:4]=='ELET' or cCodes[i][:4]=='ECNG' or cCodes[i][:4]=='ELNG':
            writer0.writerow([cCodes[i],cNames[i],dID[2]])

#Creating Department Information file        
with open('Department_data.csv', 'w',newline='') as csvfile01:
    writer01 = csv.writer(csvfile01)
    writer01.writerow(['DepartmentID','DepartmentName'])
    for i in range(len(dID)):
        writer01.writerow([dID[i],departments[i]])



#ALL THE CODE FRELATED TO STUDENT FAKE DATA. LINES:
""" List that will be used later """ #Students
sFuName= []
sfirstNames= []
slastNames= []
smiddleNames= []
semails = []
sPasswords = []
sAccTypes = []
sAccNos = []
sIDs= []
scount = 0
sCourses = []
sPCourses = []
sDeptID = []

print("Processing Student Data...")

""" Making Student full name from first and last name lists """

for l in sLns:
    for f in sFns:
        sFuName.append(f+" "+random.choice(sMns)+" "+l)

""" Adding student data to variables to popluate csv file later """
""" 'i' in this case would represnt a full name """
#makes sure each course is chosen atleast 10 times
stuCCount = 0
for i in range(2500):
    tCourse = cCodes[stuCCount]
    sPCourses.append(tCourse)
    stuCCount = stuCCount + 1
    if stuCCount == 250:
        stuCCount = 0


for i in sFuName:
    sfname = i.split(" ")[0]
    smname = i.split(" ")[1]
    slname = i.split(" ")[2]
    sfirstNames.append(sfname)
    smiddleNames.append(smname)
    slastNames.append(slname)
    email = f"{sfname}.{slname}@mymona.uwi.jm"
    semails.append(email)
    sid = 620130000+scount
    sIDs.append(sid)
    stupassword = fake.password()
    sPasswords.append(stupassword)
    actype = "Student"
    sAccTypes.append(actype)
    acNo = "STU"+ str(sid)
    sAccNos.append(acNo)
    if scount <= 2499:
        if sPCourses[scount] in cCodes:
            newCodes = cCodes[:]
            newCodes.remove(sPCourses[scount])
        courses = random.sample(newCodes, random.randint(2,5))
        courses.append(sPCourses[scount])
    else:
        courses = random.sample(cCodes, random.randint(3,6))
    sCourses.append(courses)
    department = random.choice(dID)
    sDeptID.append(department)
    scount = scount + 1

#Create student data csv file with courses listed individually
with open('student_data.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['StudentID', 'AccountNumber', 'AccountType', 'FirstName','MiddleName', 'LastName', 'Email','Password','DepartmentID','Course1','Course2','Course3','Course4','Course5','Course6' ])
    for i in range(len(sFuName)):
        if len(sCourses[i]) == 1:
            writer.writerow([sIDs[i],sAccNos[i],sAccTypes[i],sfirstNames[i],smiddleNames[i],slastNames[i],semails[i],sPasswords[i],sDeptID[i],sCourses[i][0]])
        if len(sCourses[i]) == 2:
            writer.writerow([sIDs[i],sAccNos[i],sAccTypes[i],sfirstNames[i],smiddleNames[i],slastNames[i],semails[i],sPasswords[i],sDeptID[i],sCourses[i][0],sCourses[i][1]])
        if len(sCourses[i]) == 3:
            writer.writerow([sIDs[i],sAccNos[i],sAccTypes[i],sfirstNames[i],smiddleNames[i],slastNames[i],semails[i],sPasswords[i],sDeptID[i],sCourses[i][0],sCourses[i][1],sCourses[i][2]])
        if len(sCourses[i]) == 4:
            writer.writerow([sIDs[i],sAccNos[i],sAccTypes[i],sfirstNames[i],smiddleNames[i],slastNames[i],semails[i],sPasswords[i],sDeptID[i],sCourses[i][0],sCourses[i][1],sCourses[i][2],sCourses[i][3]])
        if len(sCourses[i]) == 5:
            writer.writerow([sIDs[i],sAccNos[i],sAccTypes[i],sfirstNames[i],smiddleNames[i],slastNames[i],semails[i],sPasswords[i],sDeptID[i],sCourses[i][0],sCourses[i][1],sCourses[i][2],sCourses[i][3],sCourses[i][4]])
        if len(sCourses[i]) == 6:
            writer.writerow([sIDs[i],sAccNos[i],sAccTypes[i],sfirstNames[i],smiddleNames[i],slastNames[i],semails[i],sPasswords[i],sDeptID[i],sCourses[i][0],sCourses[i][1],sCourses[i][2],sCourses[i][3],sCourses[i][4],sCourses[i][5]])

#Create student data csv file with courses in a single list
with open('student_data2.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['StudentID', 'AccountNumber', 'AccountType', 'FirstName','MiddleName', 'LastName', 'Email','Password','DepartmentID','CoursesTaken' ])
    with open('student_courses.csv', 'w',newline='') as csvfile1:
        writer1 = csv.writer(csvfile1)
        writer1.writerow(['StudentID', 'CourseID'])
        for i in range(len(sFuName)):
            writer.writerow([sIDs[i],sAccNos[i],sAccTypes[i],sfirstNames[i],smiddleNames[i],slastNames[i],semails[i],sPasswords[i],sDeptID[i],sCourses[i]])
            if len(sCourses[i]) == 1:
                writer1.writerow([sIDs[i],sCourses[i][0]])
            if len(sCourses[i]) == 2:
                writer1.writerow([sIDs[i],sCourses[i][0]])
                writer1.writerow([sIDs[i],sCourses[i][1]])
            if len(sCourses[i]) == 3:
                writer1.writerow([sIDs[i],sCourses[i][0]])
                writer1.writerow([sIDs[i],sCourses[i][1]])
                writer1.writerow([sIDs[i],sCourses[i][2]])
            if len(sCourses[i]) == 4:
                writer1.writerow([sIDs[i],sCourses[i][0]])
                writer1.writerow([sIDs[i],sCourses[i][1]])
                writer1.writerow([sIDs[i],sCourses[i][2]])
                writer1.writerow([sIDs[i],sCourses[i][3]])
            if len(sCourses[i]) == 5:
                writer1.writerow([sIDs[i],sCourses[i][0]])
                writer1.writerow([sIDs[i],sCourses[i][1]])
                writer1.writerow([sIDs[i],sCourses[i][2]])
                writer1.writerow([sIDs[i],sCourses[i][3]])
                writer1.writerow([sIDs[i],sCourses[i][4]])
            if len(sCourses[i]) == 6:
                writer1.writerow([sIDs[i],sCourses[i][0]])
                writer1.writerow([sIDs[i],sCourses[i][1]])
                writer1.writerow([sIDs[i],sCourses[i][2]])
                writer1.writerow([sIDs[i],sCourses[i][3]])
                writer1.writerow([sIDs[i],sCourses[i][4]])
                writer1.writerow([sIDs[i],sCourses[i][5]])
            

print("Processing Lecturer Data...")
#ALL THE CODE FRELATED TO Lecturer FAKE DATA. LINES:
""" List that will be used later """ #Lecturer
lFuName= []
lfirstNames= []
llastNames= []
lmiddleNames= []
lemails = []
lPasswords = []
lAccTypes = []
lAccNos = []
lIDs = []
lcount = 0
lCourses = []
lPCourses = []



""" Making Lecturer full name from first and last name lists """
for i in lLns:
    for r in lFns:
        lFuName.append(r+" "+random.choice(lMns)+" "+i)


""" Adding student data to variables to popluate csv file later """
""" 'i' in this case would represnt a full name """
#makes sure each course is chosen atleast 10 times
lecCCount = 0
for i in lFuName:
    tCourse = cCodes[lecCCount]
    lPCourses.append(tCourse)
    lecCCount = lecCCount + 1
    if lecCCount == 250:
        lecCCount = 0


for i in lFuName:
    lfname = i.split(" ")[0]
    lmname = i.split(" ")[1]
    llname = i.split(" ")[2]
    lfirstNames.append(lfname)
    lmiddleNames.append(lmname)
    llastNames.append(llname)
    email = f"{lfname}.{llname}@uwimona.uwi.jm"
    lemails.append(email)
    lid = 300000000+lcount
    lIDs.append(lid)
    lecpassword = fake.password()
    lPasswords.append(lecpassword)
    actype = "Lecturer"
    lAccTypes.append(actype)
    acNo = "LEC"+ str(lid)
    lAccNos.append(acNo)
    if lPCourses[lcount] in cCodes:
        newCodes = cCodes[:]
        newCodes.remove(lPCourses[lcount])
    courses = random.sample(newCodes, random.randint(0,4))
    courses.append(lPCourses[lcount])
    lCourses.append(courses)
    lcount = lcount + 1
   
#Create lecturer data csv file with courses listed individually
with open('lecturer_data.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['LecturerID', 'AccountNumber', 'AccountType', 'FirstName','MiddleName', 'LastName', 'Email','Password','Course1','Course2','Course3','Course4','Course5' ])
    for i in range(len(lFuName)):
        if len(lCourses[i]) == 1:
            writer.writerow([lIDs[i],lAccNos[i],lAccTypes[i],lfirstNames[i],lmiddleNames[i],llastNames[i],lemails[i],lPasswords[i], lCourses[i][0]])
        if len(lCourses[i]) == 2:
            writer.writerow([lIDs[i],lAccNos[i],lAccTypes[i],lfirstNames[i],lmiddleNames[i],llastNames[i],lemails[i],lPasswords[i], lCourses[i][0],lCourses[i][1]])
        if len(lCourses[i]) == 3:
            writer.writerow([lIDs[i],lAccNos[i],lAccTypes[i],lfirstNames[i],lmiddleNames[i],llastNames[i],lemails[i],lPasswords[i], lCourses[i][0],lCourses[i][1],lCourses[i][2]])
        if len(lCourses[i]) == 4:
            writer.writerow([lIDs[i],lAccNos[i],lAccTypes[i],lfirstNames[i],lmiddleNames[i],llastNames[i],lemails[i],lPasswords[i], lCourses[i][0],lCourses[i][1],lCourses[i][2],lCourses[i][3]])
        if len(lCourses[i]) == 5:
            writer.writerow([lIDs[i],lAccNos[i],lAccTypes[i],lfirstNames[i],lmiddleNames[i],llastNames[i],lemails[i],lPasswords[i], lCourses[i][0],lCourses[i][1],lCourses[i][2],lCourses[i][3],lCourses[i][4]])


#Create lecturer data csv file with courses in a single list
with open('lecturer_data2.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['LecturerID', 'AccountNumber', 'AccountType', 'FirstName','MiddleName', 'LastName', 'Email','Password','CoursesTaught'])
    with open('lecturer_courses.csv', 'w',newline='') as csvfile2:
        writer2 = csv.writer(csvfile2)
        writer2.writerow(['LecturerID', 'CourseID'])
        for i in range(len(lFuName)):
            writer.writerow([lIDs[i],lAccNos[i],lAccTypes[i],lfirstNames[i],lmiddleNames[i],llastNames[i],lemails[i],lPasswords[i], lCourses[i]])
            if len(lCourses[i]) == 1:
                writer2.writerow([lIDs[i],lCourses[i][0]])
            if len(lCourses[i]) == 2:
                writer2.writerow([lIDs[i],lCourses[i][0]])
                writer2.writerow([lIDs[i],lCourses[i][1]])
            if len(lCourses[i]) == 3:
                writer2.writerow([lIDs[i],lCourses[i][0]])
                writer2.writerow([lIDs[i],lCourses[i][1]])
                writer2.writerow([lIDs[i],lCourses[i][2]])
            if len(lCourses[i]) == 4:
                writer2.writerow([lIDs[i],lCourses[i][0]])
                writer2.writerow([lIDs[i],lCourses[i][1]])
                writer2.writerow([lIDs[i],lCourses[i][2]])
                writer2.writerow([lIDs[i],lCourses[i][3]])
            if len(lCourses[i]) == 5:
                writer2.writerow([lIDs[i],lCourses[i][0]])
                writer2.writerow([lIDs[i],lCourses[i][1]])
                writer2.writerow([lIDs[i],lCourses[i][2]])
                writer2.writerow([lIDs[i],lCourses[i][3]])
                writer2.writerow([lIDs[i],lCourses[i][4]])
    

print("Processing Admin Data...")
#ALL THE CODE RELATED TO ADMIN FAKE DATA. FOUND ON LINES: 
""" List that will be used later """ #Admins
afirstNames= []
alastNames= []
amiddleNames= []
aemails = []
aPasswords = []
aAccTypes = []
aIDs = []
aAccNos = []
acount = 0

for i in aFuName:
    afname = i.split(" ")[0]
    amname = i.split(" ")[1]
    alname = i.split(" ")[2]
    afirstNames.append(afname)
    amiddleNames.append(amname)
    alastNames.append(alname)
    email = f"{afname}.{alname}@adminmona.uwi.jm"
    aemails.append(email)
    aid = 100000000+acount
    aIDs.append(aid)
    admpassword = fake.password()
    aPasswords.append(admpassword)
    actype = "Admin"
    aAccTypes.append(actype)
    acNo = "ADM"+ str(aid)
    aAccNos.append(acNo)
    acount = acount + 1

with open('admin_data.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['AdminID', 'AccountNumber', 'AccountType', 'FirstName','MiddleName', 'LastName', 'Email','Password'])
    for i in range(len(aFuName)):
        writer.writerow([aIDs[i],aAccNos[i],aAccTypes[i],afirstNames[i],amiddleNames[i],alastNames[i],aemails[i],aPasswords[i]])



