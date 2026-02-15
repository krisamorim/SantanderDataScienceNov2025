#relationship cardinality
#one to one (1:1)
class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport
class Passport:
    def __init__(self, number, country):
        self.number = number
        self.country = country

#one to many (1:N)
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
class Book:
    def __init__(self, title):
        self.title = title


#many to many (M:N)
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)
class Course:
    def __init__(self, title):
        self.title = title
        self.students = []
