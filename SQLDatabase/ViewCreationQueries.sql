
-- creates a view showing all the courses with 50 students (shows the course count too)
create view CourseOverFiftyWithCourseCount as 
select count(cid), cid from courseofstud 
group by cid 
having count(cid) >= 50;

-- creates a view showing all the courses with 50 students
create view CourseOverFifty as 
select count(cid), cid from courseofstud 
group by cid 
having count(cid) >= 50;

-- creates a view showing all the students that do 5 or more courses;
create view StudentsFiveOrMoreCourses as 
select studid from courseofstud 
group by studid 
having count(studid) >= 5;

-- creates a view showing the top 10 most enrolled courses
create view TenMostEnrolledCourses as
select count(cid), cid from 
courseofstud group by cid 
order by count(cid) desc 
limit 10;

-- creates a view showing the number of lecturers that teach 3 or more courses;
create view lectOfThreePlusCourses as 
select lid from lectofcourse 
group by lid 
having count(lid) >= 3;

create view topaverages as 
SELECT sg.studID, sn.sfName, sn.smName, sn.slName, avg( sg.grade ) as avg_grade FROM submissiongrade as sg 
join studentname as sn on sg.studID = sn.studID 
group by sn.sfName, sn.smName, sn.slName, sg.studID 
order by avg_grade desc 
limit 10;