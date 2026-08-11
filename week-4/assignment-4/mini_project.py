students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
# 1. Find the top scorer
top_score = 0
top_scorer = ""

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_scorer = student["name"]


# 2. Calculate the class average
total_score = 0

for student in students:
    total_score += student["score"]

class_average = total_score / len(students)


# 3. Find all unique subjects
subjects = set()

for student in students:
    subjects.add(student["subject"])


# 4. Find students who scored above 75
high_scorers = []

for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])


# Print the results
print("Top scorer:", top_scorer, "(", top_score, ")")
print("Class average:", class_average)
print("Subjects offered:", subjects)
print("High scorers:", high_scorers)