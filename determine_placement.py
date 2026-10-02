def determine_placement(age, marks, attendance, experience, has_backlog):
	placement_eligible = marks >= 60 and attendance >= 75 and not has_backlog

	if experience == 0:
		candidate_category = "fresher"
	elif 1 <= experience <= 2:
		candidate_category = "junior"
	elif experience > 2:
		candidate_category = "experienced"
	else:
		raise ValueError("Experience cannot be negative")

	return {
		"placement eligible": "yes" if placement_eligible else "no",
		"candidate category": candidate_category,
	}


age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
experience = int(input("Enter years of experience: "))
has_backlog = input("Does the candidate have a backlog? (true/false): ").strip().lower() == "true"

result = determine_placement(age, marks, attendance, experience, has_backlog)
for label, value in result.items():
	print(f"{label}: {value}")