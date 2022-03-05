import canv
from secrets import API_TOKEN, LINK
from canvasapi import Canvas

course_id = "23263"
canvas = Canvas(LINK, API_TOKEN)

# # Get the course
# next_assign = canv.get_next_assignment(course_id)
# # Get the next assignment
# print(next_assign.name + " is due at: " + str(next_assign.due_at))
# # Print the name of the next assignment and the due date
# print("Latest anouncement: " + str(canv.get_anouncement(course_id)))

next_assignments = canv.get_next_assignments(course_id)
for i in next_assignments:
    print(i.name + " is due at: " + str(i.due_at))