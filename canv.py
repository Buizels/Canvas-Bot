from secrets import API_TOKEN, LINK
from canvasapi import Canvas
from datetime import datetime
from dateutil import parser
from pytz import timezone
import re


"""
ANOUNCEMENT FUNCTIONS

"""

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
    # course = canvas.get_course(course_id)
   
    announce = canvas.get_announcements([course_id])

    return announce

def get_anouncement_content(announce):
    """
    This function gets the content of the anouncement.
    !TODO: Properly clean up message content
    Currently only removes html tags and returns a string

    """
    CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    # return re.sub(CLEANR, '', announce)
    return CLEANR.sub('', announce)


"""
ASSIGNMENT FUNCTIONS

"""

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

def get_all_assignments(course_id):
    """
    This function gets all assignments of the course.
    Use <assignment>[i].due_at to get the due date.
    Use <assignment>[i].name to get the name of the assignment.
    
    """
    canvas = Canvas(LINK, API_TOKEN)
    course = canvas.get_course(course_id)
   
    assignments = course.get_assignments()

    return assignments

def convert_to_pst(date_string):
    """
    This function converts a string to a datetime object in PST.
    Returns a datetime object.

    """
    date = parser.parse(date_string)
    date = date.astimezone(timezone('US/Pacific'))
    return date