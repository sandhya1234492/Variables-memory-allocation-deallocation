def check_eligibility(marks, attendance, has_backlog):
	if marks >= 60 and attendance >= 75 and not has_backlog:
		return "Eligible"
	return "Not eligible"


marks = float(input("Enter the student's marks: "))
attendance = float(input("Enter the attendance percentage: "))
has_backlog = input("Does the student have a backlog? (true/false): ").strip().lower() == "true"

print(check_eligibility(marks, attendance, has_backlog))