from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    students = relationship("Student", cascade="all,delete", back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey(Group.id, ondelete="CASCADE"))
    group = relationship("Group", cascade="all,delete", back_populates="students")
    grades = relationship("Grade", cascade="all,delete", back_populates="student")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    subjects = relationship("Subject", cascade="all,delete", back_populates="teacher")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="CASCADE"))
    teacher = relationship("Teacher", cascade="all,delete", back_populates="subjects")
    grades = relationship("Grade", cascade="all,delete", back_populates="subject")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE"))
    date_of = Column(DateTime, nullable=False)
    grade = Column(Integer, CheckConstraint("grade > 0 AND grade <= 100"), nullable=False)
    student = relationship("Student", cascade="all,delete", back_populates="grades")
    subject = relationship("Subject", cascade="all,delete", back_populates="grades")