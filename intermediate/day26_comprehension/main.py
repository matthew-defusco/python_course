import random

# numbers = [1, 2, 3]
# new_list = [num + 1 for num in numbers]
# print(new_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
# short_names = [name.upper() for name in names if len(name) <= 4]
# print(short_names)

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)
