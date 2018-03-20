SQL

code to confirm no hhsId duplicates
SELECT hhsId
FROM person
GROUP BY hhsId
HAVING count(* ) > 1
returns 0 records and no errors


//index or overview page
for total hours instructor led HRSA only
select sum(duration) div 60 as Totalhours
from course
#returns 8685
where deliveryType = 'Instructor led'
# returns 7616
and courseId like 'HRSA%'
# returns 808 with 'HRSAHLI'
# returns 1427 with 'HRSA%'


//allCourses page

//person page

select distinct course_offering.offeringId, course.courseId, courseTitle, transcript.hhsId
from course_offering
inner join course on course_offering.courseId = course.courseId
inner join transcript on course_offering.offeringId = transcript.offeringId
where transcript.hhsId = {}

//course info and offering info
  answers how many offerings of a course were completed
  select courseId, count(*)
  from course_offering
  group by courseId
  order by count(*) desc



//Additional Examples
searching on two keys
SELECT field1_index, field2_index
FROM test_table
WHERE field1_index = '1' OR  field2_index = '1'





//project officers page
these two queries represent
original
select person.lastName, person.hhsId, project_officers.firstName, project_officers.bo
from person
left join project_officers on person.lastName = project_officers.lastName
where bo = %(bo)s and person.firstName = project_officers.firstName

updated w abbreviations and different columns
SELECT p.firstName, p.lastName, p.hhsId, o.bo
FROM person p , project_officers o
WHERE p.firstName = o.firstName
AND p.lastName = o.lastName
AND o.bo = %(bo)s
