-- Restriction Check Queries

-- Check that no student does more than 6 courses
select studid from courseofstud 
group by studid 
having count(studid) > 6;

-- Check that a student is enrolled in at least 3 courses;
select studid from courseofstud 
group by studid 
having count(studid) < 3;

-- Checks that no lecturer can teach more than 5 courses
select lid from lectofcourse 
group by lid 
having count(lid) > 5;

-- Checks that no lecturer teaches less than 1 course
select lid from lectofcourse 
group by lid 
having count(lid) < 1;

-- Checks that a lecturer teaches 3 or more courses
select lid from lectofcourse 
group by lid 
having count(lid) >= 3;