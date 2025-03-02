# lab5.1.4_StudentInfo.py
# This program stores student information in a list of dictionaries & prints out the student information.
# author: Niamh Hogan

student = {
    "name": "Mary",
    "modules": [
        {
            "courseName": "Programming",
            "grade": 45
        },
        {
            "courseName": "History",
            "grade": 99
        }
    ]
}
print (f"Student: {student['name']}")
for module in student["modules"]:
    print (f"\t{module['courseName']}: {module['grade']}")