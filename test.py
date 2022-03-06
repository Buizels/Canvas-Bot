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

# next_assignments = canv.get_next_assignments(course_id)
# for i in next_assignments:
#     print(i.name + " is due at: " + str(i.due_at))

# next_announce = canv.get_anouncement(course_id)
# content = canv.get_anouncement_content(next_announce)
# print(content)

# Get all assignments

list_assignments = []
assignments = canv.get_all_assignments(course_id)
for i in assignments:
    list_assignments += [i.name]

# Print first 3 assignments
for i in range(3):
    print(list_assignments[i])