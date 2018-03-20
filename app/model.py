from sqlalchemy import create_engine
import pandas as pd


dbconn = create_engine('mysql+mysqlconnector://root:root@localhost/talentdataone')

def getInstructorLed():
    """
    total count of instructor led courses
    """
    query = """
    select COUNT(DISTINCT courseId) as mycount
    from course_offering
    where deliveryType = 'Instructor led'
    and courseId like 'HRSA%'
    """
    instructorLed = pd.read_sql(query, dbconn)

    return instructorLed

def getInstructorLedHours():
    """
    total hours for instructor led by HRSA
    """
    query = """
    select sum(duration) div 60 as mycount
    from course_offering
    where (deliveryType = 'Instructor led'
    and courseId like 'HRSA%')
    """
    instructorLedHours = pd.read_sql(query, dbconn)

    return instructorLedHours


def getVirtualCoursesDelivered():
    """
    Count of virtual courses delivered.
    """
    query = """
    select COUNT(DISTINCT courseId) as mycount
    from course_offering
    where deliveryType = 'Virtual Class'
    and courseId like 'HRSA%'
    """
    virtualCoursesDelivered = pd.read_sql(query, dbconn)

    return virtualCoursesDelivered

def getVirtualClassParticipants():
    """
    total number of attendees to HRSA virtual classes
    """
    query = """
    select count(distinct course_offering.courseId, course_offering.deliveryType, transcript.offeringId, transcript.hhsId) as virtcount
    from course_offering
    join transcript on course_offering.offeringId = transcript.offeringId
    where deliveryType = 'Virtual Class'
    or deliveryType = 'Webinar'
    or deliveryType = 'Recorded Training'
    """
    virtualClassParticipants = pd.read_sql(query, dbconn)

    return virtualClassParticipants

def getVirtualCourseHours():
    """
    virtual class hours total
    """
    query = """
    select sum(duration) div 60 as mycount
    from course_offering
    where deliveryType = 'Virtual Class'
    and courseId like 'HRSA%'
    """
    virtualCourseHours = pd.read_sql(query, dbconn)

    return virtualCourseHours

def getLmsCourses():
    """
    total number of lms courses taught
    """
    query = """
    select count(*) as mycount
    from course_offering
    where courseId like 'HRSAHLILMS%'
    """
    lmsCourses = pd.read_sql(query, dbconn)

    return lmsCourses

def getLmsCoursePersonCount():
    """
    count of employees who completed lms trianing
    """
    query = """
    select count(distinct course_offering.offeringId, course_offering.courseId, transcript.offeringId, transcript.hhsId) as lmscount
    from course_offering
    join transcript on course_offering.offeringId =     transcript.offeringId
    where courseId like 'HRSAHLILMS%'
    """
    lmsCoursePersonCount = pd.read_sql(query, dbconn)

    return lmsCoursePersonCount

def getLmsCourseHoursCount():
    """
    count of courses about the lms in hours
    """
    query = """
    select sum(duration) div 60 as mycount
    from course_offering
    where courseId like 'HRSAHLILMS%'
    """
    lmsCourseHoursCount = pd.read_sql(query, dbconn)

    return lmsCourseHoursCount

def getCourseFosCredits():
    """
    number of instructor led with fos credits
    """
    query = """
    select count(fosCredits) as mycount
    from course_offering
    inner join course_offering on course.courseId = course_offering.courseId
    where course_offering.deliveryType = 'Instructor led'
    """
    coursesFosCredits = pd.read_sql(query, dbconn)

    return coursesFosCredits



def getVirtualFosCredits():
    """
    number of instructor led with fos credits
    """
    query = """
    select count(fosCredits) as mycount
    from course
    inner join course_offering on course.courseId = course_offering.courseId
    where course_offering.deliveryType = 'Virtual class'
    """
    virtualFosCredits = pd.read_sql(query, dbconn)

    return virtualFosCredits

def getAllPeople():
    """
    get all of the people who have taken courses in the last 6 months
    """
    query = """
        select *
        from person
        order by lastName ASC
        """
    people = pd.read_sql(query, dbconn)

    return people

def getPersonOrganization(hhs_id):
    """
    get the organization of each person
    """
    query = """
        select organization.orgCode, organization.bo, organization.orgName, person.lastName, person.firstName, person.orgCode
        from organization
        left join person on organization.orgCode = person.orgCode
        where hhsId = %(hhsId)s
        """
    person = pd.read_sql(query, dbconn, params = {'hhsId':hhs_id})
    person = person.iloc[0]
    return person

def getPersonCompleted(hhs_id):
    """
    get the all courses completed by person
    """
    query = """
        select distinct course_offering.offeringId, course.courseId, courseTitle, transcript.hhsId
        from course_offering
        inner join course on course_offering.courseId = course.courseId
        inner join transcript on course_offering.offeringId = transcript.offeringId
        where transcript.hhsId = {}
        """.format(hhs_id)
    personCompleted = pd.read_sql(query, dbconn)
    return personCompleted


def getAllCourses():
    query = """
    select courseId, courseTitle
    from course
        """
    courses = pd.read_sql(query, dbconn)

    return courses


def getCourseCount():
    """
    total count of courses
    """
    query = """
        select count(*) as mycount
        from course
        """
    courseCount = pd.read_sql(query, dbconn)

    return courseCount


def getCourseInformation(course_id):
    """
    general info about the course
    """
    query = """
    select *
    from course
    where  courseId = %(course_id)s

    """
    course = pd.read_sql(query, dbconn, params={'course_id':course_id})
    course = course.iloc[0]
    return course

def getCourseOfferings(course_id):
    """
    what are all the offerings of a course
    """
    query = """
    select *
    from course_offering
    where courseId = %(course_id)s
    """
    offerings = pd.read_sql(query, dbconn, params={'course_id':course_id})
    return offerings

def getOfferingStudents(offering_id):
    """
    get all employees who completed offering
    """
    query = """
    select distinct transcript.hhsId, transcript.offeringId, person.lastName, person.firstName
    from transcript
    left join person on transcript.hhsId = person.hhsId
    where offeringId = %(offering_id)s
    """
    offeringStudents = pd.read_sql(query, dbconn, params={'offering_id':offering_id})
    return offeringStudents

def getProjectOfficerCount():
    """
    total count of project officers
    """
    query = """
        select count(*) as mycount
        from project_officers
        """
    projectOfficerCount = pd.read_sql(query, dbconn)

    return projectOfficerCount

def getBoList():
    """
    list of the bo's with proj officers
    """
    query = """
        select distinct bo
        from project_officers
        """
    boList=pd.read_sql(query, dbconn)

    return boList

def getBoProjectOfficers(bo):
    """
    list of po's by bo's
    """
    query = """
        select p.firstName, p.lastName, p.hhsId, o.bo
        from person p , project_officers o
        where p.firstName = o.firstName
        and p.lastName = o.lastName
        and o.bo = %(bo)s
    """
    boProjectOfficers=pd.read_sql(query, dbconn, params={'bo':bo})

    return boProjectOfficers

def getPoCourseCount():
    """
    total count of courses completed by PO's
    """
    query = """
        select count(distinct offeringId) as mycount
        from course_offering
        where program like 'HRSA Project Officer%'
        """
    poCourseCount = pd.read_sql(query, dbconn)

    return poCourseCount

def getPoCourseAttendanceCount():
    """
    number of PO's who completed PO CE's
    """
    query = """
         select count(distinct c.offeringId, c.program, t.offeringId) as mycount
         from course_offering as c
         join transcript as t on c.offeringId = t.offeringId
         where program like 'HRSA Project Officer%'
         """
    poCourseAttendanceCount=pd.read_sql(query, dbconn)

    return poCourseAttendanceCount

def getPoCourseHours():
    """
    sum of PO course hours
    """
    query = """
        select sum(duration) div 60 as mycount
        from course_offering
        where program like 'HRSA Project Officer%'
        """
    poCourseHours=pd.read_sql(query, dbconn)

    return poCourseHours

def getSupervisorCount():
    """
    count of supervisors
    """
    query = """
        select count(lastName) as mycount
        from supervisors
        """
    supervisorCount=pd.read_sql(query, dbconn)

    return supervisorCount

def getSupervisorList():
    """
    list of all Supervisors
    """
    query = """
        select orgCode, lastName, firstName, title
        from supervisors
        """
    supervisorList=pd.read_sql(query, dbconn)

    return supervisorList
