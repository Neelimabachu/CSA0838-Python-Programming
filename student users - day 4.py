#program to find student users



total_users=int(input("Enter Total Users: "))
staff_users=int(input("Enter Staff Users: "))
if total_users>0 and staff_users>0:
    non_teaching=staff_users//3
    staff_users=staff_users+non_teaching
    student_users=total_users-staff_users
    print("Student Users= ",student_users)
elif total_users==0 or staff_users==' ':
    print("enter valid input")
else:
    print("enter valid input")
