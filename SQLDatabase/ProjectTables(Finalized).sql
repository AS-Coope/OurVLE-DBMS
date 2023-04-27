CREATE DATABASE Project;
USE Project;

-- ######## TABLES THAT DEAL WITH COURSES ########
-- create the Course table
CREATE TABLE Course(
    cID varchar(255) NOT NULL,
    cfName varchar(255) NOT NULL
);

-- creating the LectOfCourse table
CREATE TABLE LectOfCourse(
    cID varchar(255) NOT NULL,
    lID int NOT NULL
);

-- creating CourseInDept table
CREATE TABLE CourseInDept(
    cID varchar(255) NOT NULL,
    deptID int NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE DEPARTMENT #########

-- creating Department table
CREATE TABLE Department(
    deptID int NOT NULL,
    deptName varchar(255) NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE LECTURER #########
-- creating LecturerAccount table
CREATE TABLE LecturerAccount(
    lID int NOT NULL, 
    acNo varchar(255) NOT NULL
);

-- creating Lecturer table
CREATE TABLE Lecturer(
    lID int NOT NULL,
    password varchar(255) NOT NULL,
    email varchar(255) NOT NULL
);

-- creating LectName table
CREATE TABLE LectName(
    lID int NOT NULL,
    lfName varchar(255) NOT NULL,
    lmName varchar(255) NOT NULL,
    llName varchar(255) NOT NULL
);

-- creating LectOfDept table
CREATE TABLE LectOfDept(
    lID int NOT NULL,
    deptID int NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE STUDENTS #########

-- creating Student table
CREATE TABLE Student(
    studID int NOT NULL,
    password varchar(255) NOT NULL,
    email varchar(255) NOT NULL
);

-- creating StudentName table
CREATE TABLE StudentName(
    studID int NOT NULL,
    sfName varchar(255) NOT NULL,
    smName varchar(255) NOT NULL,
    slName varchar(255) NOT NULL
);

-- creating StudentOfDept table
CREATE TABLE StudentOfDept(
    studID int NOT NULL,
    deptID int NOT NULL
);

-- creating StudentAccount table
CREATE TABLE StudentAccount(
    studID int NOT NULL,
    acNo varchar(255) NOT NULL
);

-- creating CourseOfStud table
CREATE TABLE CourseOfStud(
    studID int NOT NULL,
    cID varchar(255) NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE ADMIN #########
-- creating Admin table
CREATE TABLE AdminName(
    aID int NOT NULL,
    afName varchar(255) NOT NULL,
    amName varchar(255) NOT NULL,
    alName varchar(255) NOT NULL
);

-- creating AdminAccount table
CREATE TABLE AdminAccount(
    aID int NOT NULL,
    acNo varchar(255) NOT NULL
);

CREATE TABLE Admin(
    aID int NOT NULL,
    password varchar(255) NOT NULL,
    email varchar(255) NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE ACCOUNT #########
-- creating Account table
CREATE TABLE Account(
    acNo varchar(255) NOT NULL,
    acType varchar(255) NOT NULL,
    ufName varchar(255) NOT NULL,
    umName varchar(255) NOT NULL,
    ulName varchar(255) NOT NULL,
    uPassword varchar(255) NOT NULL,
    dateCreated DATE NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE Discussion Forum #########
-- creating DiscussionForum table
CREATE TABLE DiscussionForum(
    forumNo varchar(255) NOT NULL,
    cID varchar(255) NOT NULL
);

-- creating DiscussionForumContent table
CREATE TABLE DiscussionForumContent(
    forumNo varchar(255) NOT NULL,
    forumTitle varchar(255) NOT NULL,
    forumMessage varchar(255) NOT NULL
);

-- ############ TABLES THAT DEAL WITH THE Discussion Forum Thread ##########
CREATE TABLE DiscussionThread(
    threadNo varchar(255) NOT NULL,
    forumNo varchar(255) NOT NULL
);

CREATE TABLE DiscussionThreadContent(
    threadNo varchar(255) NOT NULL,
    threadTitle varchar(255) NOT NULL,
    threadMessage varchar(255) NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE Calendar Events #########
-- creating CalendarEvents table
CREATE TABLE CalendarEvents(
    calEvNo varchar(255) NOT NULL,
    calEvName varchar(255) NOT NULL,
    calEventContents varchar(255), -- nullable field/attribute
    evDate DATE NOT NULL,
    evTime TIME NOT NULL
);

-- creating CalEventOfCourse table
CREATE TABLE CalEventOfCourse(
    calEvNo varchar(255) NOT NULL,
    cID varchar(255) NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE Section #########
-- creating Section table 
CREATE TABLE Section(
    secNo varchar(255) NOT NULL,
    secName varchar(255) NOT NULL
);

-- creating SecOfCourse table 
CREATE TABLE SecOfCourse(
    secNo int NOT NULL,
    cID varchar(255) NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE Section Item #########
-- creating SectionItem table 
CREATE TABLE SectionItem(
    secItemNo varchar(255) NOT NULL,
    secItemName varchar(255) NOT NULL
);

-- creating SectItemOfSection table 
CREATE TABLE SectItemOfSection(
    secNo varchar(255) NOT NULL,
    secItemNo varchar(255) NOT NULL,
    secContent BLOB -- stores files as binary/ also will store text (character) strings as text
                    -- possible to have it nullable
);

-- ######## TABLES THAT DEAL WITH THE Submission Portal #########

-- creating SubPortOfCourse table
CREATE TABLE SubPortOfCourse(
    spID varchar(255) NOT NULL,
    cID varchar(255) NOT NULL
);

-- creating SubmissionPortal table 
CREATE TABLE SubmissionPortal(
    spID varchar(255) NOT NULL,
    spName varchar(255) NOT NULL,
    dueDate DATE NOT NULL,
    subDate DATE NOT NULL
);

-- creating SubmissionEntries table 
CREATE TABLE SubmissionEntries(
    spID int NOT NULL,
    studID varchar(255) NOT NULL,
    itemSubmit BLOB NOT NULL
);

-- creating SubmissionGrade table
CREATE TABLE SubmissionGrade(
    studID int NOT NULL,
    grade int NOT NULL
);

-- ######## TABLES THAT DEAL WITH THE Link (a type of Section Item) #########
-- creating Link table 
CREATE TABLE Link(
    lkID varchar(255) NOT NULL,
    lkName varchar(255) NOT NULL
);

-- creating SectionLink table 
CREATE TABLE SectionLink(
    lkID varchar(255) NOT NULL, 
    secItemNo varchar(255) NOT NULL
);

-- ################### RELATIONSHIPS ##################
-- creating a user
CREATE TABLE CreateForUser(
    acNo int NOT NULL,
    adID int NOT NULL
);

-- creating a course
CREATE TABLE Creates(
    adID int NOT NULL,
    cID varchar(255) NOT NULL,
    cName varchar(255) NOT NULL
);

-- creating a section item in a section
CREATE TABLE Contain(
    secNo varchar(255) NOT NULL,
    secItemNo varchar(255) NOT NULL
);

-- creating enrolment
CREATE TABLE Enrol(
    cID varchar(255) NOT NULL,
    studID int NOT NULL
);

-- creating comprisedOf (essentially the Members table)
CREATE TABLE ComprisedOf(
    cID varchar(255) NOT NULL,
    acNo varchar(255) NOT NULL,
    acType varchar(255) NOT NULL
);

-- creating startsA
CREATE TABLE StartsA(
    threadNo varchar(255) NOT NULL,
    lID varchar(255)  NOT NULL
);

-- creating startsA2
CREATE TABLE StartsA2(
    threadNo varchar(255)  NOT NULL,
    studID varchar(255)  NOT NULL
);

-- creating repliesTo
CREATE TABLE RepliesTo(
    threadNo varchar(255)  NOT NULL,
    lID varchar(255)  NOT NULL
);

-- creating repliesTo2
CREATE TABLE RepliesTo2(
    threadNo varchar(255) NOT NULL,
    studID varchar(255) NOT NULL
);

-- creating createNew 
CREATE TABLE CreatesNew(
    secNo varchar(255) NOT NULL,
    lID int NOT NULL
);

-- creating createNewSecInfo 
CREATE TABLE CreatesNewSecInfo(
    secNo varchar(255) NOT NULL,
    secName varchar(255) NOT NULL
);

-- creating manages 
CREATE TABLE Manages(
    secItemNo varchar(255) NOT NULL,
    lID int NOT NULL
);

-- creating responsibleFor 
CREATE TABLE ResponsibleFor(
    calEvNo varchar(255) NOT NULL,
    lID int NOT NULL
);

-- creating belongsTo 
CREATE TABLE BelongsTo(
    cID varchar(255) NOT NULL,
    deptID int NOT NULL
);

-- creating belongsTo2 
CREATE TABLE BelongsTo2(
    studID int NOT NULL,
    deptID int NOT NULL
);

-- creating sets table
CREATE TABLE Sets(
    cID int NOT NULL,
    calEvNo varchar(255) NOT NULL
);

-- creating dividedInto 
CREATE TABLE DividedInto(
    cID int NOT NULL,
    sec varchar(255) NOT NULL,
    secNo varchar(255) NOT NULL
);

-- creating includes 
CREATE TABLE Includes(
    forumNo varchar(255) NOT NULL,
    threadNo varchar(255) NOT NULL
);

-- creating holds 
CREATE TABLE Holds(
    cID int NOT NULL,
    forumNo varchar(255) NOT NULL
);