import canv
from secrets import API_TOKEN, LINK
from canvasapi import Canvas

course_id = "23263"
canvas = Canvas(LINK, API_TOKEN)

next_assign = canv.get_next_assignment(course_id)
print(next_assign.name + " is due at: " + str(next_assign.due_at))
print("Latest anouncement: " + str(canv.get_anouncement(course_id)))