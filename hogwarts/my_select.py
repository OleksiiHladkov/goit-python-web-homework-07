from sqlalchemy import select, func, desc

from connection_db import session
from models import Group, Student, Teacher, Subject, Grade


def select_1():
    result = (
        session.query(
            Student.id,
            Student.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id, Student.name)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )

    return result


def select_2(subject_id=1):
    result = (
        session.query(
            Student.id,
            Student.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id, Student.name)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )

    return result


def select_3(subject_id=1):
    result = (
        session.query(
            Group.id,
            Group.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .outerjoin(Student, Student.id == Grade.student_id)
        .outerjoin(Group, Group.id == Student.group_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id, Group.name)
        .order_by(desc("avg_grade"))
        .all()
    )

    return result


def select_4():
    result = (
        session.query(func.round(func.avg(Grade.grade), 1).label("avg_grade"))
        .select_from(Grade)
        .all()
    )

    return result


def select_5(teacher_id=1):
    result = (
        session.query(Subject.id, Subject.name)
        .select_from(Subject)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )

    return result


def select_6(group_id=1):
    result = (
        session.query(Student.id, Student.name)
        .select_from(Student)
        .filter(Student.group_id == group_id)
        .all()
    )

    return result


def select_7(group_id=1, subject_id=1):
    result = (
        session.query(Student.id, Student.name, Grade.date_of, Grade.grade)
        .select_from(Grade)
        .outerjoin(Student, Student.id == Grade.student_id)
        .outerjoin(Group, Group.id == Student.group_id)
        .filter(Group.id == group_id, Grade.subject_id == subject_id)
        .order_by(Student.name, Grade.date_of)
        .all()
    )

    return result


def select_8(teacher_id=1):
    result = (
        session.query(
            Subject.id,
            Subject.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .outerjoin(Subject, Subject.id == Grade.subject_id)
        .outerjoin(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Teacher.id == teacher_id)
        .group_by(Subject.id, Subject.name)
        .order_by(desc("avg_grade"))
        .all()
    )

    return result


def select_9(student_id=1):
    result = (
        session.query(Subject.id, Subject.name)
        .select_from(Grade)
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Grade.student_id == student_id)
        .group_by(Subject.id, Subject.name)
        .all()
    )

    return result


def select_10(student_id=1, teacher_id=1):
    result = (
        session.query(Subject.id, Subject.name)
        .select_from(Grade)
        .join(Subject, Subject.id == Grade.subject_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .group_by(Subject.id, Subject.name)
        .all()
    )

    return result


if __name__ == "__main__":
    print(select_10())
