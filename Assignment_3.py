university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}
# Q1: Print all student names and their majors
print("Student Names and Majors")
for sid, info in university_data.items():
    print(f"{info['name']} - {info['major']}")

# Q2: Average score per course per student
print("\nAverage Score Per Course Per Student")
for sid, info in university_data.items():
    print(f"\n{info['name']}:")
    for course, scores in info["courses"].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course} - Average: {avg:.2f}")

# Q3: Find students who scored >90 in final of Python101
print("\nStudents with >90 in final of Python101")
for sid, info in university_data.items():
    courses = info["courses"]
    if "Python101" in courses and courses["Python101"]["final"] > 90:
        print(f"  {info['name']} - Final: {courses['Python101']['final']}")

# Q4: Add new course AI101 for student S101
university_data["S101"]["courses"]["AI101"] = {"midterm": 89, "final": 91, "project": 93}
print("\nAdded course AI101 for student S101.")

# Q5: Print average score for each course (all students combined)
from collections import defaultdict

course_totals = defaultdict(lambda: {"total": 0, "count": 0})

for sid, info in university_data.items():
    for course, scores in info["courses"].items():
        avg = sum(scores.values()) / len(scores)
        course_totals[course]["total"] += avg
        course_totals[course]["count"] += 1

print("\n Average Score for Each Course Across All Students:")
for course, data in course_totals.items():
    course_avg = data["total"] / data["count"]
    print(f"  {course} - Average: {course_avg:.2f}")

