import random
import pandas as pd

# List Comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
# new_list = []
# for n in numbers:
#     new_list.append(n + 1)
# print(new_numbers)

# Using list comprehension with a string
name = "Alberto"
name_letters = [letter for letter in name]
# print(name_letters)

# Using list comprehension with range
double = [number*2 for number in range(1, 5)]
# print(double)

# List Comprehension with conditional
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)
long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)

# Dictionary comprehension
# new_dict = {new_key: new_value for item in iterable}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in students}
# print(students_scores)
approved_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(approved_students)

# Looping through dictionaries:
student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}
# for (key, value) in student_dict.items():
#     print(value)

# Looping through a data frame:
student_df = pd.DataFrame(student_dict)
# print(student_df)
#
# for (key, value) in student_df.items():
#     print(value)

# Looping through rows of a data frame:
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)
        # print(row) <- this is a series
