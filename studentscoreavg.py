# CALCULATING THE AVERAGE OF 3 ACVITY
def calcu_average(score1, score2, score3):
    total = (score1 + score2 + score3)
    average = total / 3
    return average


def main():
    print("--- Student Activity Score System ---")

# ASKING IF HOW MANY STUDENTS OR USER WILL CALCULATE.
student_cnt = int(input("Enter the number of students: "))
while student_cnt < 3:
    print("Enter atleast 3 students")
    student_cnt = int(input("Enter the number of students: "))

print()

# LOOP TO PROCESS EACH STUDENT'S INPUT
for i in range(1, student_cnt + 1):
    print("Student", i)

    name = input("Student Name: ")
    act1 = float(input("Activity 1 Score: "))
    act2 = float(input("Activity 2 Score: "))
    act3 = float(input("Activity 3 Score: "))

    # CALCULATING THE STUDENT'S AVERAGE SCORE USING THE CALCU_AVERAGE ABOVE
    overall_avg = calcu_average(act1, act2, act3)

# STUDENT SCORE STATUS. if, elif, else statements
if overall_avg >= 90:
    status = "Excellent!"
elif overall_avg >= 80:
    status = "Very Good!"
elif overall_avg >= 75:
    status = "Passed!"
else:
    status = "Failed"

print()

# PRINTING THE AVERAGE AND STATUS
print("Average: ", overall_avg)
print("Status: ", status)

# EXECUTING THE MAIN PROGRAM IN "def main():
if name == "main":
    main()