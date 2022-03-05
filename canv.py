from secrets import API_TOKEN, LINK
from canvasapi import Canvas
from datetime import datetime
from dateutil import parser
from pytz import timezone

def get_anouncement(course_id):
    """
    This function gets the most recent anouncement of the course.

    """
    canvas = Canvas(LINK, API_TOKEN)
    course = canvas.get_course(course_id)
   
    announce = canvas.get_announcements([course_id])

    return announce[0]

def get_anouncements(course_id):
    """
    This function gets the most recent anouncement of the course.
    Returns as a paginated list.

    """
    canvas = Canvas(LINK, API_TOKEN)
    course = canvas.get_course(course_id)
   
    announce = canvas.get_announcements([course_id])

    return announce

def get_next_assignment(course_id):
    """
    This function gets the next assignment of the course.
    Use <assignment>.due_at to get the due date.
    Use <assignment>.name to get the name of the assignment.
    
    """
    canvas = Canvas(LINK, API_TOKEN)
    course = canvas.get_course(course_id)
   
    assignments = course.get_assignments()

    current = datetime.now()
    current = current.astimezone(timezone('US/Pacific'))

    next_assignment = assignments[0]
    for i in assignments:
        if(i.due_at != None):
            time = parser.parse(i.due_at)
            time = time.astimezone(timezone('US/Pacific'))
            if(time > current):
                next_assignment = i
                break

    return next_assignment

def get_next_assignments(course_id):
    """
    Returns a list of assignments that are due after the current time.
    Use <assignment>[i].due_at to get the due date.
    Use <assignment>[i].name to get the name of the assignment.
    
    """
    canvas = Canvas(LINK, API_TOKEN)
    course = canvas.get_course(course_id)
   
    assignments = course.get_assignments()

    current = datetime.now()
    current = current.astimezone(timezone('US/Pacific'))

    next_assignments = []
    for i in assignments:
        if(i.due_at != None):
            time = parser.parse(i.due_at)
            time = time.astimezone(timezone('US/Pacific'))
            if(time > current):
                next_assignments += [i]

    return next_assignments