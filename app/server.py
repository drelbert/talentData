from flask import Flask, render_template, redirect, request
from model import *


app = Flask(__name__)

@app.route('/index')
def index():
    name = ''
    instructorLed = getInstructorLed()
    instructorLedHours = getInstructorLedHours()
    virtualCoursesDelivered = getVirtualCoursesDelivered()
    virtualClassParticipants = getVirtualClassParticipants()
    virtualCourseHours = getVirtualCourseHours()
    lmsCourses = getLmsCourses()
    lmsCoursePersonCount = getLmsCoursePersonCount()
    lmsCourseHoursCount = getLmsCourseHoursCount()
    poCourseCount = getPoCourseCount()
    poCourseAttendanceCount = getPoCourseAttendanceCount()
    poCourseHours = getPoCourseHours()
    return render_template('index.html', username=name, instructorLed=instructorLed, instructorLedHours=instructorLedHours, virtualCoursesDelivered=virtualCoursesDelivered, virtualClassParticipants=virtualClassParticipants, virtualCourseHours=virtualCourseHours, lmsCourses=lmsCourses, lmsCoursePersonCount=lmsCoursePersonCount, lmsCourseHoursCount=lmsCourseHoursCount, poCourseCount=poCourseCount, poCourseAttendanceCount=poCourseAttendanceCount, poCourseHours=poCourseHours)

@app.route('/people')
def people():
    #people is the identifier name
    #the parameter would go in ()'s'
    #the argument is people=people
    people = getAllPeople()
    return render_template('people.html',
        people=people)


@app.route('/people/<hhs_id>')
def person(hhs_id):
    person = getPersonOrganization(hhs_id)
    personCompleted = getPersonCompleted(hhs_id)
    return render_template('person.html',  person=person, personCompleted=personCompleted)



@app.route('/courses')
def courses():
    courses = getAllCourses()
    courseCount = getCourseCount()
    return render_template('allCourses.html', courses=courses, courseCount=courseCount)

@app.route('/courses/<course_id>')
def course(course_id):
    course = getCourseInformation(course_id)
    offerings = getCourseOfferings(course_id)
    return render_template('course.html', course=course, offerings=offerings)

@app.route('/courses/<course_id>/<offering_id>')
def courseOffering(course_id, offering_id):
    offeringStudents = getOfferingStudents(offering_id)
    return render_template('courseOffering.html',  offeringStudents=offeringStudents)



@app.route('/projectOfficer')
def projectOfficer():
    projectOfficerCount = getProjectOfficerCount()
    boList = getBoList()
    return render_template('projectOfficer.html', projectOfficerCount=projectOfficerCount, boList=boList)

@app.route('/boProjectOfficers/<bo>/')
def boProjectOfficers(bo):
    boProjectOfficers = getBoProjectOfficers(bo)
    return render_template('boProjectOfficers.html', boProjectOfficers=boProjectOfficers)

@app.route('/supervisor')
def supervisor():
    supervisorCount = getSupervisorCount()
    supervisorList = getSupervisorList()

    return render_template('supervisor.html', supervisorCount=supervisorCount, supervisorList=supervisorList)



app.run(debug=True, port=5000)
