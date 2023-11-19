from datetime import datetime
from random import randint, choice

from faker import Faker

from connection_db import session
from models import Group, Student, Teacher, Subject, Grade


NUMBER_GROUPS = 3
NUMBER_STUDENTS = 45
NUMBER_SUBJECTS = 7
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20


fake_data = Faker()


def fill_groups():
    return ["Gryffindor", "Ravenclaw", "Slytherin"]


def fill_students():
    result = []

    for _ in range(NUMBER_STUDENTS):
        result.append(fake_data.name())

    return result


def fill_subjects():
    return ["Defence Against the Dark Arts", "Astronomy", "Transfiguration", "Charms", "Potions", "History of Magic", "Herbology"]


def fill_teachers():
    result = []

    for _ in range(NUMBER_TEACHERS):
        result.append(fake_data.name())

    return result


def add_groups_to_db():
    groups_list = fill_groups()

    count = 0
    for group_name in groups_list:
        group = Group(name=group_name)
        session.add(group)
        count += 1
    
    session.commit()
    
    return count
    
    
def add_students_to_db():
    students_list = fill_students()

    groups = session.query(Group).all()

    count = 0
    while len(students_list):
        for group in groups:
            student_name = choice(students_list)
            student = Student(name=student_name, group_id=group.id)
            session.add(student)
            students_list.remove(student_name)
        
            count += 1
    
    session.commit()
    
    return count


def add_teachers_to_db():
    teachers_list = fill_teachers()

    count = 0
    for teacher_name in teachers_list:
        teacher = Teacher(name=teacher_name)
        session.add(teacher)
        count += 1
    
    session.commit()
    
    return count


def add_subjects_to_db():
    subjects_list = fill_subjects()

    techers = session.query(Teacher).all()

    count = 0
    for subject_name in subjects_list:
        teacher = choice(techers)
        subject = Subject(name=subject_name, teacher_id=teacher.id)
        session.add(subject)
        count += 1
    
    session.commit()
    
    return count


def add_grades_to_db():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    
    count = 0
    for student in students:
        grades_count = randint(10, 20)
        while grades_count:
            subject = choice(subjects)
            date = datetime(2023, randint(10, 11), randint(1, 30)).date()
            grade_value = randint(50, 100)
            grade = Grade(student_id=student.id, subject_id=subject.id, date_of=date, grade=grade_value)
            session.add(grade)
            count += 1
            grades_count -= 1
    
    session.commit()

    return count


if __name__ == "__main__":
    gp_num = add_groups_to_db()
    print(f"Added {gp_num} groups to DB")

    st_num = add_students_to_db()
    print(f"Added {st_num} students to DB")

    tr_num = add_teachers_to_db()
    print(f"Added {tr_num} teachers to DB")

    sb_num = add_subjects_to_db()
    print(f"Added {sb_num} subjects to DB")

    gd_num = add_grades_to_db()
    print(f"Added {gd_num} grades to DB")