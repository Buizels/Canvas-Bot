from secrets import API_TOKEN 
from secrets import LINK
from canvasapi import Canvas

def get_anouncement(course_id):
    """
    This function gets the most recent anouncement of the course.
    
    """
    canvas = Canvas(LINK, API_TOKEN)
    course = canvas.get_course(course_id)
   
    announce = canvas.get_announcements([course_id])

    return announce[0]

