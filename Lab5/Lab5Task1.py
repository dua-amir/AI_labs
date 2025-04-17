def check_attendance(roll_number, present_students):
    if roll_number in present_students:
        return "Present"
    else:
        return "Absent"

present_students_list = [47849, 46462, 46484, 47789, 43507]
roll_no = int(input("Enter roll number: "))
attendence = check_attendance(roll_no, present_students_list)
print(f"Student with roll number {roll_no} is {attendence}.")

